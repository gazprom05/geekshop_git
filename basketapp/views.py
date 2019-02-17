from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from basketapp.models import Basket
from mainapp.models import Product
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import JsonResponse

@login_required
def basket(request):
    title = 'корзина'
    basket_items = Basket.objects.filter(user=request.user). \
        order_by('product__category')

    context = {
        'title': title,
        'basket_items': basket_items,
    }

    return render(request, 'basketapp/basket.html', context)

@login_required
def add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('products:product', args=[pk]))
    product = get_object_or_404(Product, pk=pk)
    old_basket_item = Basket.objects.filter(user=request.user, product=product)

    if old_basket_item:
        old_basket_item[0].quantity += 1
        old_basket_item[0].save()
    else:
        new_basket_item = Basket(user=request.user, product=product, quantity=1)
        new_basket_item.save()
        # Basket.objects.create(user=request.user, product=product, quantity=1)
        # new_basket_item.quantity += 1

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove(request, pk):
    basket_rec = get_object_or_404(Basket, pk=pk)
    basket_rec.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def edit(request, pk, value):
    if request.is_ajax():
        quantity = int(value)
        new_basket_item = Basket.objects.get(pk=int(pk))

        if quantity > 0:
            new_basket_item.quantity = quantity
            new_basket_item.save()
        else:
            new_basket_item.delete()

        basket_items = Basket.objects.filter(user=request.user). \
            order_by('product__category')

        context = {
            'basket_items': basket_items,
        }

        result = render_to_string('basketapp/includes/inc_basket_list.html', \
                                  context)

        return JsonResponse({'result': result})
