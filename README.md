# MusicAPI #

## Summary: ##

A music student want to see all the assignments in one place in one simple view, so these are the server side apis to GET and POST the assignments by user.

Project stack:
    1) Python3
    2) Django
    3) Django REST Framework, rest_auth and allauth


### Here we have: ###

Markup : * An assignment app where user can GET all the assignments in a single view and POST the assignment.

Markup : * To 'register' a user or to 'login' a user we have used rest_auth and all_auth.


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

