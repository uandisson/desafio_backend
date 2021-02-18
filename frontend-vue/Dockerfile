FROM node:14-alpine

LABEL MAINTAINER="Uandisson Miranda <https://www.linkedin.com/in/uandisson | @uandisson>"

RUN mkdir -p /opt/frontend-vue/credito-express-app

WORKDIR /opt/frontend-vue/credito-express-app
        
COPY package*.json ./

RUN npm install

EXPOSE 8080

RUN export HOST=0.0.0.0

CMD ["npm", "run", "dev"]