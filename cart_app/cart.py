
from products_app.models import Product


CART_SESSION_ID="cart"

class Cart:
    def __init__(self,requst):
        self.session=requst.session
        cart=self.session.get(CART_SESSION_ID)
        if not cart:
            cart=self.session[CART_SESSION_ID]={}
        self.cart=cart
        
    def __iter__(self):
        cart=self.cart
        for item in cart.values():
            if 'id' not in item:
                continue
            item['product']=Product.objects.get(id=int(item['id']))
            item['final_price']=Product.objects.get(id=int(item['id'])).final_price()
            item['total_price']=int(item['quntity'])*Product.objects.get(id=int(item['id'])).final_price()
            yield item

    def unique_id_genrator(self,id):
        result=f"{id}"
        return result


    def total(self):
        total=0
        for cart in self.cart.values():
            total+=cart['total_price']
        return total
        
    def clear(self):
        for key in list(self.cart.keys()):  
            del self.cart[key]
        self.save()
        
    def remove(self,product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()
        
    def quantity(self):
        
        return sum(item['quntity'] for item in self.cart.values() if 'quntity' in item)
        
        

    def add(self,prodct,quntity=1,override_quantity=False):
        unique_id=self.unique_id_genrator(id=prodct.id)
        if unique_id not in self.cart:  
            self.cart[unique_id]={"quntity":0,'id':str(prodct.id)} 
        if override_quantity:
            self.cart[unique_id]['quntity']=int(quntity)
        else:
            self.cart[unique_id]['quntity']+=int(quntity) 
        
        print("cartINadd:",self.cart)
        self.save()


    def save(self):
        self.session.modified = True

        