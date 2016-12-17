#!/bin/bash
cd /opt/od
CMDDOCK=$@
if [ -z "$CMDDOCK" ]
then
  if [ ! -f "/opt/od/config.json" ]
  then
    cat /opt/od/config.json.example | sed "s/db_id/root/g" | sed "s/db_id/pass123/g" | sed "s/localhost/oddb/g" > /opt/od/config.json
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    python manage.py runserver
  else
    python manage.py runserver
  fi
else
  $@
fi
