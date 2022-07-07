# When should use static methods 

class Item:
    
    @staticmethod
    
    def is_integer():
        pass

    #This should do something unique relationship to the class but not something unique to per instance
    
    @classmethod
    
    def instantiate_from_something(cls):
        pass
    
    # This should do something that has relationship with class,
    # But usually is used to manupulate different data from Instantiate objects
    # Like you do in csv 