class Item:
    pay_rate = 0.8
    all = []
    def __init__(self,name : str, price : float = 0, quantity =0):
        
        # Validating the input
        assert price >= 0, print(f"the price of {name} cannot be negative.")
        assert quantity >=0, print(f"the quantity of {name} cannot be negative.")
        
        # Setting the values

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

        # calculating the total price
    def calculating_total_price(self):
        return self.price*self.quantity
    
    def apply_discount(self):
        self.price = self.price * Item.pay_rate

    def __repr__(self):
        return f"Item('name = {self.name}',price = {self.price},quantity = {self.quantity})"
        


# Creating the Object and using the methods

item = Item('iPhone',1300,4)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)
# # print('the cost of iphones is ',item.calculating_total_price())
# print(Item.all)

# print(item.all)

for n in Item.all:
    print(n)
