
import csv

class Item:
    
    pay_rate=0.8
    all=[]
    
    # Initialize Object Using Constractor
    def __init__(self, name:str,__price:float,quantity=0):
        self.__name=name  # Prevent access of attribute outside class
        self.__price=__price
        self.quantity=quantity
        
    # Appling Ready Only Decorator
    # Propery decorator== Ready Only Attributies
    
    @property
     
    def price(self):
        
        return self.__price
    
    def calculate_price(self):
        
        return self.__price * self.quantity
    
    def apply_increment(self, increment_value):
        
        self.__price= self.__price + self.__price *increment_value
        
    
        
    
    
    
    @property
    def name(self):
        
        return self.__name
    
    
    @name.setter
    
    def name(self, value):
           
        self.__name= value
    
       
    # Action To Excute 
     
        Item.all.append(self)
    
    
    # Method to calculate __price
      
    
    # Method To Calculate Discount
    def  calculate_discount(self):
        
        
        self.__price= self.__price* self.pay_rate
     
    # Class Method In Action
        
    @classmethod
    def instatiation_csv(cls):
        with open('items.csv', 'r') as f:
            reader=csv.DictReader(f)
            items=list(reader)
        for item in items:
            print(item)
    
    @property
    def read_only_name(self):
        
        return "AAA"
    # Method To show Representable Way
    
    def __repr__(self):
        
        return f"Item('{self.name},{self.__price}, {self.quantity}')"