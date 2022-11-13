from django.shortcuts import render

# Create your views here.
def products(request):
    data = {'title':"Products"}
    return render(request, 'products/products.html', data)