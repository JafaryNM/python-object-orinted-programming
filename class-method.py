class Item:
    
    def calculate_total_price(self,price, quantity):
        return price*quantity
    

item1=Item() 
item1.name='Laptop'
item1.price=500
item1.quantity=3
print(item1.calculate_total_price(500, 7))