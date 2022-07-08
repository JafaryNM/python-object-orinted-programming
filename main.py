from item import Item
from phone import Phone

item1=Item("Laptop",750)
item1.name='Adaptor'
item1.apply_increment(0.2)

print(item1.price)


#### NOT ALLOWED TO UPDATE READ_ONLY_NAME  ########

#item1.read_only_name="BBB"