FROM nginx:alpine
COPY dist/ /usr/share/nginx/html
COPY deploy/nginx-docker.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
