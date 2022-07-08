
from item import Item

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