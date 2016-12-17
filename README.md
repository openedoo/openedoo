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

## Docker Images

### Setup DB
```bash
$ docker run --name od-db -e MYSQL_ROOT_PASSWORD=pass123 -d mariadb
```

### Run And Play
```bash
$ docker run --name od --link openedoodb:openedoodb -p 5000:5000 -it aksaramaya/openedoo bash
# cat config.json
{
    "db":
        {
            "db_engine": "mysql",
            "db_id": "root",
            "db_password" : "pass123",
            "db_host" : "od-db",
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
