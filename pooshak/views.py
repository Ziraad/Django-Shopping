from django.shortcuts import render

from .models import SportSet


def homepage(request):
    sport_set = SportSet.objects.all()
    context = {
        'sport_set': sport_set
    }
    return render(request, 'pooshak/home_page.html', context=context)


def product_details(request, product_id):
    product = SportSet.objects.get(pk=product_id)
    context = {
        'product': product
    }
    return render(request, 'pooshak/product_details.html', context=context)

