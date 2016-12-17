#!/bin/bash
cd /opt/od
CMDDOCK=$@
MYSQL_ADDR="oddb"
MYSQL_PORT="3306"
MYSQL_PASSWORD="pass123"

if [ -z "$CMDDOCK" ]
then
  printf "Waiting database connection"
  until mysql -h"$MYSQL_ADDR" -P "$MYSQL_PORT" -uroot -p "$MYSQL_PASSWORD" &> /dev/null
  do
    printf "."
    sleep 1
  done
  if [ ! -f "/opt/od/config.json" ]
  then
    cat /opt/od/config.json.example | sed "s|your_username|root|g" | sed "s|your_password|pass123|g" | sed "s/localhost/oddb/g" > /opt/od/config.json
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    python manage.py run
  else
    python manage.py run
  fi
else
  $@
fi
