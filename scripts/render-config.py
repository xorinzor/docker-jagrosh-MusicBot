#!/usr/bin/env python

"""
This script renders the MusicBot configuration from environment variables
with a specific prefix. The variables `<prefix>_owner` and `<prefix>_token`
are mandatory.

Note: Environment variable names are case-insensitive and so all option names
that are rendered by this script are rendered as lower case.
"""

MANDATORY_OPTIONS = ['token', 'owner']
DEFAULT_OPTION_VALUES = {'prefix': '!'}

import argparse
import os


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('filename')
  parser.add_argument('--prefix')
  parser.add_argument('--skip-if-exists', action='store_true')
  args = parser.parse_args()

  if args.skip_if_exists and os.path.isfile(args.filename):
    print('note: config file "{}" already exists, not rendering config file')
    exit(0)

  options = DEFAULT_OPTION_VALUES.copy()
  for env_name in os.environ:
    if env_name.startswith(args.prefix):
      option_name = env_name[len(args.prefix):].lower()
      options[option_name] = os.environ[env_name]

  missing_options = set(MANDATORY_OPTIONS) - set(options.keys())
  if missing_options:
    print('error: missing mandatory options {!r}'.format(missing_options))
    exit(1)

  with open(args.filename, 'w') as fp:
    for key, value in options.items():
      fp.write('{} = "{}"\n'.format(key, value))


if __name__ == '__main__':
  main()
