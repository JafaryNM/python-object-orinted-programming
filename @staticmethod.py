
import csv


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
        
        
        
    # Instantiate To Csv 
    # Class Method In Action
    
    @classmethod
    def instatiation_csv(cls):
        with open('items.csv', 'r') as f:
            reader=csv.DictReader(f)
            items=list(reader)
        for item in items:
            print(item)
        
    # Static Method In Action
    
    @staticmethod
    def is_integer(num):
       # We Want To Point Float Which Is Point Zero
       # For Example 5.0 ,10.0
       
       if isinstance(num,float):
           #Count Out float which is point zero
           return num.is_interger()
       elif isinstance(num,int):
           return True
       else :
           return False
    
    def __repr__(self):
        
        return f"Item('{self.name},{self.price}, {self.quantity}')"
         

#### ACCESSING STATIC METHOD #######
print (Item.is_integer(7.0))   

