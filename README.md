# Cloud Note System

+ Run server: `python manage.py runserver`
+ Run app. migration: `python manage.py migrate`
	+ Show Migrations: `python manage.py showmigrations --list`
+ New Django app: `python manage.py startapp <app_name>`
+ Add a view:
	+ **<app_name>/views.py**: Set HttpResponse
	+ **<project_name>/urls.py**: Set urlpatterns
	+ Then visit http://127.0.0.1:8000/hello/  
	  *hello* can be changed by the settings in urlpatterns.
+ Database **<project_name>/settings.py**:
	+ ENGINE: which engine?
		+ MySQL: `django.db.backends.mysql`
		+ SQLite 3: `django.db.backends.sqlite3`
		+ PostgreSQL: django.db.backends.postgresql_psycopg2
	+ NAME: database name
```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

+ Create superuser account: `python manage.py createsuperuser`

