# WELCOME TO OPENEDOO

![N|Solid](http://openedoo.org/images/openedoo.svg)

## how to use

```bash
git clone https://github.com/openedoo/openedoo

pip install -r requirements.txt
```

### Migrate Database
```bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python manage.py --help
```

### Create New Module
```bash
python manage.py create "module_name"
```

### Runserver
```bash
python manage.py runserver
```

## Docker Compose

### Setup
```bash
$ docker-compose up -d
$ curl
```

### Stop Services
```bash
$ docker-compose stop
```

### Run And Play
```bash
$ docker-compose start
```

### Create Module
```bash
$ docker-compose stop od
$ docker-compose run od python manage.py create "test"
$ docker-compose start od
```
