class Item:

    def __init__(self,name : str, price : float, quantity =0):
        
        # Validating the input
        assert price >= 0, print(f"the price of {name} cannot be negative.")
        assert quantity >=0, print(f"the quantity of {name} cannot be negative.")
        
        # Setting the values

        self.name = name
        self.price = price
        self.quantity = quantity

        # calculating the total price
    def calculating_total_price(self):
        return self.price*self.quantity

# Creating the Object and using the methods

item = Item('iPhone',1300,4)

print('the cost of iphones is ',item.calculating_total_price())
