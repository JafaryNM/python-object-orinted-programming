
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
    # Classmethods
    
    @classmethod
    def instatiation_csv(cls):
        with open('items.csv', 'r') as f:
            reader=csv.DictReader(f)
            items=list(reader)
        for item in items:
            print(item)
        
        
         
    # Method To show Representable Way
    
    def __repr__(self):
        
        return f"Item('{self.name},{self.price}, {self.quantity}')"
        

Item.instatiation_csv()