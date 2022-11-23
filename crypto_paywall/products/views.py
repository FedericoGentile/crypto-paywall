from django.shortcuts import render
from .models import Product

# Create your views here.
def products(request):

    products = Product.objects.all()
    data = {'title':"Products", "products":products}
    return render(request, 'products/products.html', data)