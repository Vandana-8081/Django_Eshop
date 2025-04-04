from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product , cart):
    keys = cart.keys()
    for id in cart:
        if int(id) == product.id:
            return True
    return False



@register.filter(name='cart_quantity')
def cart_quantity(product , cart):
    keys = cart.keys()
    for id in cart:
        if int(id) == product.id:
            return cart.get(id)
    return 0


@register.filter(name='price_total')
def price_total(product , cart):
    print(product.price)
    return product.price * cart_quantity(product , cart)
    

