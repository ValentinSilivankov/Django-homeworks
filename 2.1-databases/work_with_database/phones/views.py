from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_pages = request.GET.get('sort', 'name')
    if sort_pages == 'min_price':
        sort_pages = 'price'
    elif sort_pages == 'max_price':
        sort_pages = '-price'
    phone = Phone.objects.order_by(sort_pages).all()
    context = {'phones': phone}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone' : phone }
    return render(request, template, context)