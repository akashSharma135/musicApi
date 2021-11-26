# MusicAPI #

## Summary: ##

A music student want to see all the assignments in one place in one simple view, so these are the server side apis to GET and POST the assignments by user.

Project stack:
    1) Python3
    2) Django
    3) Django REST Framework


### Here we have: ###

* An assignment app where user can GET all the assignments in a single view and POST the assignment.


## Initial Project Setup ##

```bash
cd musicApi
python -m venv env
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Test Case Example:

### Request (POST):

```bash
method: POST
request: http://127.0.0.1:8000/assignment/
```

```bash
{
    "title": "Assignment One",
    "description": "This is a description.",
    "music_genre": "Rock Music",
    "daily_practice_time": "00:08:00",
    "days": 5,
    "days_practiced": 5
}
```

### Response:

```bash
{
    "id": 1,
    "title": "Assignment One",
    "description": "This is a description.",
    "music_genre": "Rock Music",
    "daily_practice_time": "00:08:00",
    "days": 5,
    "days_practiced": 5
}
```

### Request (GET):

```bash
method: GET
request: http://127.0.0.1:8000/assignment/
```

### Response:

```bash
[
    {
        "id": 1,
        "title": "Assignment One",
        "description": "This is a description.",
        "music_genre": "Rock Music",
        "daily_practice_time": "00:08:00",
        "days": 5,
        "days_practiced": 5
    },
    {
        "id": 2,
        "title": "Assignment Two",
        "description": "This is a description.",
        "music_genre": "Soul Music",
        "daily_practice_time": "00:06:00",
        "days": 5,
        "days_practiced": 4
    }
]
```
