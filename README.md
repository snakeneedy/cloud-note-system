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

