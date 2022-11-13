# Crypto Paywall
This tutorial aims to show how to create a crypto paywall using a Metamask wallet interconected to a Django web app.

- Create Django project: `django-admin startproject crypto_paywall`
- Create the Product page: `python manage.py startapp products`
	- Add new file urls.py in products/
	- Modify crypto_paywall/urls.py
	- Create base and products templates
	- Update INSTALLED_APPS in settings.py ('products.apps.ProductsConfig')
	
