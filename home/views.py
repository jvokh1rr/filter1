from django.shortcuts import render
from home.models import Product


def example_new(request):
    product = Product.objects.filter(status='New')
    product_count = product.count()
    context = {
        'product': product,
        'product_count': product_count,
    }
    return render(request, 'new.html', context)


def example_old(request):
    product = Product.objects.filter(status='Old')
    product_count = product.count()
    context = {
        'product': product,
        'product_count': product_count,
    }
    return render(request, 'old.html', context)


def example_broken(request):
    product = Product.objects.filter(status='Broken')
    product_count = product.count()
    context = {
        'product': product,
        'product_count': product_count,
    }
    return render(request, 'broken.html', context)


def example_used(request):
    product = Product.objects.filter(status='Used')
    product_count = product.count()
    context = {
        'product': product,
        'product_count': product_count,
    }
    return render(request, 'used.html', context)
