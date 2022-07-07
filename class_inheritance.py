class Item:
    
    pay_rate=0.8
    all=[]
    
    # Initialize Object Using Constractor
    def __init__(self, name:str,price:float,quantity=0):
        self.name=name
        self.price=price
        self.quantity=quantity
        
    # Action To Excute 
     
        Item.all.append(self)
    
    
    # Method to calculate price
      
    def calculate_price(self):
        
        return self.price * self.quantity
    
    # Method To Calculate Discount
    def  calculate_discount(self):
        
        
        self.price= self.price* self.pay_rate
        
    # Method To show Representable Way
    
    def __repr__(self):
        
        return f"Item('{self.name},{self.price}, {self.quantity}')"
        

class Phone(Item):
    
    all=[]
    
    
     # Instantiation Of An Object
     
    def __init__(self, name:str,price:float,broken_phone=0,quantity=0):
        
    # Call Super Method To Have Access To All Attributies And Method
       super().__init__(
           name, 
           price,
           quantity
       )
    
    
       self.broken_phone=broken_phone
    # Action Should Be Excuted
    
       Phone.all.append(self)

phone1=Phone("nokia",100, 1,7)
phone2=Phone("Sumsang", 790, 2,8)


print(phone1.calculate_price())