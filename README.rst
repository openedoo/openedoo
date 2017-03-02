# WELCOME TO OPENEDOO [![Build Status](https://travis-ci.org/openedoo/openedoo.svg?branch=master)](https://travis-ci.org/openedoo/openedoo)

![N|Solid](http://openedoo.org/images/openedoo.svg)
## openedoo-beta in pip
```
pip install openedoo

and run in your terminal

openedoo install

```
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
python manage.py module create -n "module_name"
```
```bash
python manage.py module create -n "module_name" --remote "github_repo_url"
```

### Runserver
```bash
python manage.py run
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
$ docker-compose exec od python manage.py create "test"
```

### Manage Module
```bash
$ docker-compose stop od
$ docker-compose run od bash
[from_od]$ openedoo module create -n "test"
[from_od]$ opendoo module remove test
[from_od]$ opendoo module install https://github.com/openedoo/module_hello
```
