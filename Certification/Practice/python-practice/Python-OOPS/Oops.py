# Python OOPS concepts

from typing import overload


class Products:
    @overload
    def calc_profit(self):
        return "No profit"
    @overload
    def calc_profit(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        return b*c*0.1


prod = Products()
prod.name = 'Veg Burger'
prod.price = 23.5
prod.quant = 5

# Calculating no profit
print(f"{prod.name} with price = {prod.price} sold quantity = {prod.quant} with profit {prod.calc_profit()}")

prod1 = Products()
prod1.name = 'Ice'
prod1.price = 10
prod1.volume = 90

print(f"{prod1.name} with price = {prod1.price} sold quantity = {prod1.volume} with profit {prod1.calc_profit()}")


# Calculating real profit

realProd = Products()

realProd.name = 'Coke'
realProd.price = 3.24
realProd.quant = 56

print(f"{realProd.name} with price = {realProd.price} sold quantity = {realProd.volume} with profit {realProd.calc_profit(realProd.name,realProd.price,realProd.quant)}")

print(list(prod.__dict__.keys()))
print(list(prod1.__dict__.keys()))