# MusicAPI #

## Summary: ##

A music student want to see all the assignments in one place in one simple view, so these are the server side apis to GET and POST the assignments by user.

Project stack:
    1) Python3
    2) Django
    3) Django REST Framework, rest_auth and allauth


### Here we have: ###

* An assignment app where user can GET all the assignments in a single view and POST the assignment.

* To 'register' a user or to 'login' a user we have used rest_auth and all_auth.


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

### Request:

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

```bash
method: GET
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
