# This is my first python OOPS code

# Aijaz Mobile & Laptop Shop 
# Location : Houston

# calculating the income from mobiles and laptop in a day

product_mob = "Mobile"
quantity_mob = 5
price_mob = 300

product_lap = "Laptop"
quantity_lap = 3
price_lap = 1000


profit_mob = quantity_mob*price_mob

print(f"Revenue from Mobiles {profit_mob}")

print(f"Revenue from Laptop {quantity_lap*price_lap}")

# Creating a Structure

#   Blueprint/Template/Plane of action

class ElectronicShop:
    prod = ''
    quantity = 0 
    price = 0

    def storing_data_prod(self,prod,quantity,price):
        print('Printing self from storing_data_prod = ',self)
        self.prod = prod
        self.quantity = quantity
        self.price = price
    
    def rev_calc(self):
        revenue = self.quantity*self.price
        return revenue

# Using the structure
# Create an object to use the class

# <variable_name> = <ClassNmae()>
#Object Creation
shop = ElectronicShop()
shop.storing_data_prod('Dell Laptop',5,1000)
print('Printing object reference of shop object = ',shop)
revenue_final = shop.rev_calc()
print('********************************')
print('The revenue for the Dell Laptops is ',revenue_final)
print('********************************')

shop = ElectronicShop()
shop.storing_data_prod('Iphone Mobile',100,150)
revenue_final = shop.rev_calc()
print('********************************')
print('The revenue for the Iphone Mobile is ',revenue_final)
print('********************************')