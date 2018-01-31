#!/usr/bin/sh

PIDFILE=/var/log/studentmanager/uwsgi8898.pid
if [ -f $PIDFILE ]; then
    echo "Stop uWSGI"
    uwsgi --stop $PIDFILE
    rm -f $PIDFILE
fi

echo "Start uWSGI"
uwsgi --ini uwsgi8898.ini

echo "Start nginx"
/usr/local/nginx/sbin/nginx
