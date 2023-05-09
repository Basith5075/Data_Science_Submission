class Student:
    
    def __init__(self,name,roll):
        self.__name=name
        self.roll_no = roll
    
    #  This acts as Getter 

    @property
    def name(self):
        return self.__name

    # This is the setter, it will help in setting up the value.
    @name.setter
    def name(self,value):
        if(len(value)>10):
            raise Exception('The String is too Long !!')
        else:
            self.__name = value

stud = Student("sachin",12)
print(stud.name)
stud.name = 'Jaffer'
print(stud.name)