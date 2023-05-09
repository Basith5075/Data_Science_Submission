import csv
from unicodedata import name
class Item:
    all = []
    @classmethod
    def instantiate_with_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            obj = Item(
                 name = item.get('name'),
                 price = float(item.get('price')),
                 quantity = int(item.get('quantity'))
                )
            Item.all.append(obj)
                
    def __init__(self,name: str, price: float, quantity=0):
         # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"
    
    def reading_CSV(self):
        # f = open('test.csv','r')
        # print(f.read())
        # f.close()
        with open('test.csv','r') as file:
            reader = csv.DictReader(file)
            names = list(reader)
            for n in names:
                print('name = ',n.get('Name'),end=" : ")
                print('Address = ',n.get('Address'))
                  
        
# ************************************************
#           Object Creation and calling it

item = Item(name='boston mobile',price = 65.43)
item.instantiate_with_csv()
for obj in Item.all:
    print(obj)
item.reading_CSV()