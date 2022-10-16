# Template Simple API with Flask and SQLAlchemy.

I was in the discord communities and realized that people had difficulty creating an api with these tools, so I developed a simple template to be easy to modify.

## Requirements:

- Python = 3.9
- Pip = 23

## Clone the project

```sh
    git clone https://github.com/AntonioLourencos/template-flask-sqlalchemy
```

## Configure the project

First create `.env` after copying the date from `.env.example` and then put in your settings.

## Installing Dependencies

```sh
   pip install -r requirements.txt
```

or

```sh
  python3.9 -m pip install -r requirements.txt
```

## Running Migration

```sh
   python flask db init
   python flask db migrate
```

or

```sh
   python3.9 flask db init
   python3.9 flask db migrate
```

## Running Project

```sh
   python src/app.py
```

or

```sh
  python3.9 src/app.py
```

## More Info

If you want to learn and improve more follow the links:

- https://flask-migrate.readthedocs.io/
- https://flask-sqlalchemy.palletsprojects.com/
- https://flask.palletsprojects.com/
