#!/bin/bash
cd /opt/od
CMDDOCK=$@
if [ -z "$CMDDOCK" ]
then
  printf "Waiting database connection"
  while ! mysqladmin ping -h oddb -u root -ppass123 2>/tmp/error
  do
    printf "."
    sleep 1
  done
  if [ ! -f "/opt/od/config.json" ]
  then
    cat /opt/od/config.json.example | sed "s|your_username|root|g" | sed "s|your_password|pass123|g" | sed "s/localhost/oddb/g" > /opt/od/config.json
    pip install --editable .
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
