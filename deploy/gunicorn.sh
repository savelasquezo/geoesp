#!/bin/bash

NAME="geoesp"
DJANGODIR=$(dirname $(cd `dirname $0` && pwd))
SOCKFILE=/tmp/gunicorn-geoesp.sock
LOGDIR=${DJANGODIR}/logs/gunicorn.log
USER=root
GROUP=root
NUM_WORKERS=5
DJANGO_WSGI_MODULE=core.wsgi

rm -frv $SOCKFILE
echo $DJANGODIR
cd $DJANGODIR

exec ${DJANGODIR}/venv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=$LOGDIR
