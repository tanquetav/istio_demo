# docker build -t counter:v1 .
FROM node:8-alpine

WORKDIR /work

COPY package.json /work
COPY src /work/src

RUN npm i 

EXPOSE 3000

CMD node src/app.js
