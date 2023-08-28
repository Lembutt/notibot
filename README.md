# Notibot Project

Notibot is a project that provides a convenient and efficient way to notify specific Telegram users using the Telegram API. This bot is designed to be easily integrated into your workflow and is commonly used with Docker.

## Environment variables

### NOTIBOT_ADMINS
  
This variable represents list of notibot admins 

```console
foo@bar:~$ export NOTIBOT_ADMINS=TELEGRAM_ADMIN_ID_1:TELEGRAM_ADMIN_ID_2
```

### NOTIBOT_TOKEN

Token from https://t.me/BotFather

```console
foo@bar:~$ export NOTIBOT_TOKEN=TOKEN
```

## Docker Hub

```console
foo@bar:~$ docker push lembutt/notibot:tagname
```

## Docker Compose Example

```yaml
version: '3'
services:
  php:
    image: php:8.0.5-fpm-alpine
    volumes:
      - './src:/var/www/html'

  nginx:
    image: nginx:latest
    ports: 
      - 89:80
    volumes:
      - './src:/var/www/html'
      - './docker/nginx/conf.d:/etc/nginx/conf.d'

  notibot:
    image: lembutt/notibot:latest
    environment:
      - NOTIBOT_TOKEN
      - NOTIBOT_ADMINS
```

## Nginx config example

```nginx

server {
    listen       80;
    listen  [::]:80;
    server_name  localhost;

    location / {
        root   /var/www/html;
        index  index.php index.htm;
    }

    location /sendMessage {
        proxy_pass http://notibot/notifyAdmins;
    }

    error_page   500 502 503 504  /50x.html;

    location = /50x.html {
        root   /usr/share/nginx/html;
    }

    location ~ \.php$ {
        root           /var/www/html;
        fastcgi_pass   php:9000;
        fastcgi_index  index.php;
        fastcgi_param  SCRIPT_FILENAME $document_root$fastcgi_script_name; #/scripts$fastcgi_script_name;
        include        fastcgi_params;
    }
}
```
