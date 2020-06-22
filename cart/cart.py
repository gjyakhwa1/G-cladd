from decimal import Decimal
from django.conf import settings
from product.models import ProductRegister


class Cart(object):

    def __init__(self, request, mode):

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
            mode = self.session[settings.CART_TYPE_SESSION_ID] = mode

        mode = self.session.get(settings.CART_TYPE_SESSION_ID)
        self.mode = mode
        self.cart = cart

    def add(self, product, price, quantity=1):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(price)
                                     }

        self.cart[product_id]['quantity'] += quantity
        self.save()

    def update(self, product_id, update_value):
        self.session[settings.CART_SESSION_ID][product_id]['quantity'] = update_value
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session[settings.CART_TYPE_SESSION_ID] = self.mode
        self.session.modified = True

    def cartItems(self):
        product_ids = self.cart.keys()
        products = ProductRegister.objects.filter(id__in=product_ids)
        return products

    def __iter__(self):
        product_ids = self.cart.keys()
        products = ProductRegister.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price']*item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.session[settings.CART_TYPE_SESSION_ID] = ''
        self.session.modified = True

    def get_total(self):
        return sum(Decimal(item['price'])*item['quantity'] for item in self.cart.values())
