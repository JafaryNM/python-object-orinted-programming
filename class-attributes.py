class Item:
    
    ############ CLASS ATTRIBUTIES #################
     
    pay_rate=0.8
    
    def __init__(self, name:str,price:float,quantity=0):
        
    ## Constractor Methods is called when object is created
    ## Print(f"Instance is created: {name} ,{price}, {quantity}")
    ## Assign to each object created
    ## Avoid to multipy number by negative number 
    ## Validate data type 
    
    ########## RUN VALIDATE TO INCOMING ARGUMENTS ##########
    
     assert price>=0 , f"Price {price} is not greater than zero!!"
     assert quantity>=0 , f"Quatity {quantity} is not greater than zero !!"
    
    
     
    
    ######### ASSIGN SELF TO OBJECT ##########
     self.name=name
     self.price=price
     self.quantity=quantity
      
      
    ## Modified methods to receive attributies 
    
    def calculate_price(self):
        
        return self.price * self.quantity



item1=Item('Laptop',300,3)
item2=Item('Phone',90,2)
item2.has_numpad=False

print (item1.pay_rate)













