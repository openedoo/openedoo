# WELCOME TO OPENEDOO

![N|Solid](http://openedoo.org/images/openedoo.svg)

<<<<<<< HEAD
## Version 0.1
[![Build Status](https://travis-ci.org/openedoo/openedoo.svg?branch=master)](https://travis-ci.org/openedoo/openedoo)
=======
## how to use
>>>>>>> openedoo-v0.1

```bash
git clone https://github.com/openedoo/openedoo

pip install -r requirements.txt
```

<<<<<<< HEAD
#### Please change config.json

change your configuration with replace your config.json.example to config.json,

###### ALERT if you don't change the configuration your db can be fail

```
{
    "db":
        {
            "db_engine": "mysql",
            "db_id": "db_user",
            "db_password" : "db_password",
            "db_host" : "localhost",
            "db_port" : "3306",
            "db_name" : "openedoo"
        },
    "config": "Development",
    "secret_key" : "aksaramaya_openedoo"
}

```

#### Migrate Database
```
=======
### Migrate Database
```bash
>>>>>>> openedoo-v0.1
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

## Docker Images

### Setup DB
```bash
$ docker run --name openedoodb -e MYSQL_ROOT_PASSWORD=pass123 -d mariadb
```

### Run And Play
```bash
$ docker run --name od --link openedoodb:openedoodb -p 5000:5000 -it aksaramaya/openedoo bash
# cat config.json
{
    "db":
        {
            "db_engine": "mysql",
            "db_id": "openedoodb",
            "db_password" : "pass123",
            "db_host" : "localhost",
            "db_port" : "3306",
            "db_name" : "db_openedoo",
            "db_prefix" : "openedoo"
        },
    "config": "Development",
    "secret_key" : "aksaramaya_openedoo"
}
```

### Remove Image
```bash
docker rm od
```
