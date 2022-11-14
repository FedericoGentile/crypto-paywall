# Crypto Paywall
This tutorial aims to show how to create a crypto paywall using a Metamask wallet interconected to a Django web app.

## Create a database
- [Postgresql tutorial](https://www.youtube.com/watch?v=BLH3s5eTL4Y)
- Log in postgres/admin
- CREATE ROLE fede LOGIN SUPERUSER PASSWORD 'new_password';
- Login again
- CREATE DATABASE database_name ;
- \c database_name
- \c postgres
- DROP DATABASE database_name;

## Create Django webapp
- Create Django project: `django-admin startproject crypto_paywall`
- Create the Product page: `python manage.py startapp products`
	- Add new file urls.py in products/
	- Modify crypto_paywall/urls.py
	- Create base and products templates
	- Update INSTALLED_APPS in settings.py ('products.apps.ProductsConfig')
	

	
