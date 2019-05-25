FROM openjdk:8

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y python3 python3-pip curl bash

# Print the Java and Python version. Useful when inspecting the build logs.
RUN java -version
RUN python3 --version

# Create the application directory and copy files.
RUN mkdir -p /opt/app
WORKDIR /opt/app
COPY scripts/ scripts/

# Download the application.
RUN curl -L https://github.com/jagrosh/MusicBot/releases/download/0.2.2/JMusicBot-0.2.2-Linux.jar > JMusicBot.jar

# Construct the configuration file.
RUN mkdir -p /opt/app/config
WORKDIR /opt/app/config

CMD python3 /opt/app/scripts/render-config.py config.txt --prefix MUSICBOT_ --skip-if-exists && \
    java -Dnogui=true -jar /opt/app/JMusicBot.jar
