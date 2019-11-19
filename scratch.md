# Step-by-step guide of buildling this project
1. new github repo
2. python env - install django and DRF
3. create new app `django-admin startapp quickstart`
4. `.gitignore` env folder
5. sync db for first time - `python manage.py migrate`
6. create super user `createsuperuser --email admin@example.com --username admin`
7. add `rest_framework`,`quickstart` to `INSTALLED_APPS` in `{PROJECT}/settings.py` 
8. add paths to pages in `urls.py`
9. create model for GIFs
10. `python manage.py makemigrations`
11. `python manage.py migrate`
12. `python manage.py shell`