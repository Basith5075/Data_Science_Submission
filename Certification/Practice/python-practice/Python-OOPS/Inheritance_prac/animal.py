class Animal:

    def __init__(self,name,legs, canFly = False, iSDomestic = True):
        self.name = name
        self.legs = legs
        self.canFly = canFly
        self.iSDomestic = iSDomestic
    
    def __repr__(self):
        return f"Animals('{self.name}',{self.legs},{self.canFly},{self.iSDomestic})"

    def animal_name(self):
        print(f"Printing the animal name = {self.name}")

    def sum_of_numbers(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        result = self.num1 + self.num2
        return result

lion = Animal('Lion',4,False,False)

print(lion)
