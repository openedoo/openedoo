# WELCOME TO OPENEDOO

![N|Solid](http://openedoo.org/images/openedoo.svg)

## Version 0.1
[![Build Status](https://travis-ci.org/openedoo/openedoo.svg?branch=master)](https://travis-ci.org/openedoo/openedoo)

#### how to use
```
git clone https://github.com/openedoo/openedoo

pip install -r requirements.txt
```

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
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python manage.py --help
```

#### Create New Module
```
python manage.py create "module_name"
```

#### Runserver
```
python manage.py runserver
```

http://openedoo.org core v0.1 has realease [0]. Hopely, openedoo can build any open platfrom for education, please help me to develope and contribute to openedoo [1] [2] with your idea or code .
[0](https://github.com/openedoo/openedoo/issues)
[1](https://github.com/openedoo/openedoo)
[2](https://telegram.me/openedoo)