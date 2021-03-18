FROM nginx:1.15
LABEL MAINTAINER="Mohsen Mahmoodzadeh | 1mohsen.smm@gmail.com"

COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]