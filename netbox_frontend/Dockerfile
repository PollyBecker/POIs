FROM node:21-alpine

WORKDIR /app

COPY ./poi-app/package*.json ./

RUN npm install

COPY ./poi-app ./

RUN npm run build

RUN npm install -g serve

EXPOSE 3000

CMD ["serve", "-s", "build"]