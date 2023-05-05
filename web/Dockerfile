FROM node:latest as build

# Create app directory
WORKDIR /usr/src/app


# Bundle app source
COPY ./ /usr/src/app


RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
    && nvm install v18.15.0
    && npm install -g npm
    && npm install -g @angular/cli