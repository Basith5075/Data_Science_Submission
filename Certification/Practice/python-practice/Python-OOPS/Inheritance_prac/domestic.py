from animal import Animal

class Domestic(Animal):

    def __init__(self,name,legs,canFly = False, iSDomestic = True, breed = 'NA'):

        super().__init__(name,canFly,iSDomestic)
        self.breed = breed

    def __repr__(self):
        return f"Domestic('{self.name}',{self.legs},{self.canFly},{self.iSDomestic},{self.breed})"
    
    

cat = Domestic('Milaina',4,False,True,'Massakkali')
cat.animal_name()
print("sum of Two Numbers = ",cat.sum_of_numbers(12,14))
print(cat)