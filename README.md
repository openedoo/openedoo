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

### Run and play
```bash
docker run --name od -p 5000:5000 -it aksaramaya/openedoo bash
```

### Remove
```bash
docker rm od
```
