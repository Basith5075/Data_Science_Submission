from Constructor_Prac import Item

print('Please Enter the Price of the Item')
price = float(input())
print('Please Enter the quantity of the Item')
quant = int(input())

newItem = Item('Samsung',price,quant)

print('The price of Samsung mob is =',newItem.calculating_total_price())
