class CarRental:

    def __init__(self):
        self.gallons = 40
        self.tire_press = 35
        self.rate = 60
        self.carList = ['Toyota','Honda','Mercedes','Rolls Royce','Nissan','BMW']
        self.deposit = 600
        self.num_days = 1
        print("calling the __init__ constructor")

    def calculate_rent(self,carlist,deposit,num_days):
               
        if (carlist in self.carList) and (deposit>self.deposit):
            total_rent = self.rate*num_days
            print(f'Your {carlist} total rent is {total_rent} ')
            print(f' ******* Deposit of $ {deposit} will be refunded to you after car inspection')
        elif deposit<self.deposit :
            print('Sorry because of less deposit you cannot rent the car')
        else:
            print(f'Sorry We do not offer {carlist} as of now, please check back later')

car = CarRental()
car.calculate_rent('Toyota_Camry',400,4)


