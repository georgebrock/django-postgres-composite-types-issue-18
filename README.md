# Django Postgres Composite example

This project demonstrates the following issue:
<https://github.com/danni/django-postgres-composite-types/issues/18>

## Assumptions

- Python 3.6
- PostgreSQL

## Setup

1. Install dependencies:

        pip install pipenv
        pipenv install
        pipenv shell

2. Create database

        createdb composite_test
        python manage.py migrate

3. Run the server

        python manage.py runserver

4. Visit <http://localhost:8000/>

5. Follow the instructions on the page
