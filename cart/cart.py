from django.conf import settings 
from decimal import Decimal
from ecomapp.models import Product

class Cart(object):
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_KEY)
        if not cart:
            cart = self.session[settings.CART_SESSION_KEY] = {}
        self.cart = cart
 

    def add(self,product,quantity):
        product_id = str(product.id)
        print(product_id)
    
        if not product_id in self.cart:
            self.cart[product_id] = {'quantity':quantity,'price':str(product.price)}
        else:
      
            self.cart[product_id]['quantity'] += quantity
        self.save()
        
    def save(self):
        self.session.modified = True

    def list(self):
        carts = []
        for product_id in self.cart.keys():
            obj = Product.objects.get(id=product_id)
            tmp_cart = {
                'id':product_id,
                'obj':obj,
                'quantity':self.cart[product_id]['quantity'],
                'price': Decimal(int(self.cart[product_id]['quantity']) * int(obj.price))
            }
            carts.append(tmp_cart)
        return carts

    def get_total_amount(self):
        return sum(float(v['price'] ) for v in self.cart.values())

    def items(self):
        return sum(int(v['quantity']) for v in self.cart.values())
        
    def update(self,quantity,product_id):
        pid = str(product_id)
       
        self.cart[pid]['quantity'] = quantity
        self.save()
        print(self.cart)

    def delete(self,product_id):
        pid = str(product_id)
        del self.cart[pid]
        self.save()
