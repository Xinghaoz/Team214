This repository is for your course final project. Your project team
should complete all project work using this repository.

Before your project demo, add to this file a link to your deployed
web site:  


LINK:
TEAM214.US
http://ec2-54-152-23-241.compute-1.amazonaws.com/
54.152.23.241

Dependency:
sudo pip3 install django
sudo pip3 install pytz
sudo pip3 install Pillow
sudo pip3 install channels
sudo pip3 install asgi_redis
sudo apt install redis-server
sudo apt install redis-tools

redis-server


## Deploy
sudo ln -s /home/ubuntu/webprj/lovelive.conf /etc/nginx/sites-enabled/

Run uWSGI in background:
```bash
uwsgi --ini uwsgi.ini &
```

If we want to Stop uWSGI:
```bash
killall -9 uwsgi
```

2824
python3 manage.py runworker
sudo daphne -b 0.0.0.0 -p 80 webprj.asgi:channel_layer
killall -9 daphne
