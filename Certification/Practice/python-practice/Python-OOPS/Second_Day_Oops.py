class Hotel:

    def rate_finder(self,nights,rate):
        return nights*rate


# / ##############################

hotelObj = Hotel()

hotelObj.nights = 5
hotelObj.rate = 43

var1 = list(hotelObj.__dict__)
print(f"number of variables = {var1}")


print('The total money for stay is = ',hotelObj.rate_finder(hotelObj.nights,hotelObj.rate), '\nHappy stay')

# / ##############################

hotelObj2 = Hotel()

hotelObj2.rooms = 32
hotelObj2.clean_status = 12
hotelObj2.dirty_status = hotelObj2.rooms - hotelObj2.clean_status


var2 = list(hotelObj2.__dict__)
print(f"number of variables of var2 = {var2}")