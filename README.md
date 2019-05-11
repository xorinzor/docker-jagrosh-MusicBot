  [jagrosh/MusicBot]: https://github.com/jagrosh/MusicBot

A Dockerfile for [jagrosh/MusicBot]. Configurable via environment variables.

Example `docker-compose.yml`:

```yml
version: '3.4'
services:
  musicbot:
    build: .
    environment:
      MUSICBOT_token: DISCORD_BOT_TOKEN
      MUSICBOT_owner: 'DISCORD_USER_ID'
      MUSICBOT_prefix: '!'
      MUSICBOT_status: DND
      MUSICBOT_songinstatus: 'true'
```
