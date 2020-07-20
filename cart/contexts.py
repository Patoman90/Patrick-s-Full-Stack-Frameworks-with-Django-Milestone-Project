from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):

    cart = request.session.get('cart', {})

    cart_items = []
    total_items = 0
    product_count = 0
    service_count = 0

    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total_items += quantity * product.price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})

    for id, quantity in cart.items():
        service = get_object_or_404(Product, pk=id)
        total_items += quantity * service.price
        service_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'service': service})

    cart_total = product_count + service_count

    return {'cart_items': cart_items, 'total_items': total_items, 'cart_total': cart_total}
