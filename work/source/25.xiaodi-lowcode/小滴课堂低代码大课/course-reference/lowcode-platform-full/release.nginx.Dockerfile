FROM nginx:1.25.0-alpine

ADD nginx/release.nginx.conf /etc/nginx/nginx.conf

EXPOSE 80