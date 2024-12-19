import unittest
import rent_car_management


class TestCustomer(unittest.TestCase):

    def test_customer_is_underage(self):
        underage_customer = rent_car_management.Customer("Johnny", "Joe", 17, "Fw92322", "1354-5345-9973")
        outcome = underage_customer.check_if_customer_is_underage()
        self.assertEqual(outcome, False)
    
    def test_customer_not_underage(self):
        adult_customer = rent_car_management.Customer("Anthony", "Hopkins", 22, "QW2434532", "0234-6643-9927")
        outcome = adult_customer.check_if_customer_is_underage()
        self.assertEqual(outcome, True)



    def test_customer_registration(self):
        user = rent_car_management.CustomerService("Johnny", "Depp", "44", "B274213412", "3134-4652-6543", 0)
        user.register_client()
        self.assertEqual(len(user.customer_list), 1)


    def test_customer_signing_off(self):
        user = rent_car_management.CustomerService("Brad", "Pitt", "62", "DE12345941", "9713-9077-1112", 2)
        user.register_client()
        self.assertEqual(len(user.customer_list), 0)
    
    def test_add_customer_in_vip_list(self):
        client_vip = rent_car_management.CustomerService("Leo", "Dicaprio", "57", "GW7938274", "1412-0483-0000", 5)
        client_vip.register_client()
        client_vip.add_customer_in_vip()
        self.assertEqual(len(client_vip.customer_vip_list), 1)


    def test_rent_car(self):
        car_1 = rent_car_management.Car("F23", "Diesel", "Automatic", "J837420")
        car_2 = rent_car_management.Car("E214", "Petrol", "Automatic", "DE812331")

        booking = rent_car_management.Booking( "F23", "Diesel", "Automatic", "J837420", 5, "Johnny", "Depp", "44", "B274213412", "3134-4652-6543", 2)
        booking.available_cars = [car_1, car_2]
        booking.rent_car(car_1, "J837420")
        self.assertEqual(len(booking.available_cars), 1)
        self.assertEqual(booking.available_cars[0].car_plate,"DE812331")


    def test_return_car(self):
        car = rent_car_management.Car("D40", "Electric", "Automatic", "WE801114")
        booking = rent_car_management.Booking( "D40", "Electric", "Automatic", "WE801114", 11, "Brad", "Pitt", "62", "DE12345941", "9713-9077-1112", 2)
        booking.available_cars = [car]
        booking.rent_car(car, "WE801114")
        self.assertEqual(len(booking.available_cars), 0)


    def test_payment_fee_petrol_car(self):
        car_petrol = rent_car_management.Car("Z99", "Petrol", "Manual", "KH92732") 
        booking_petrol = rent_car_management.Booking(model = car_petrol.model , fuel_type = car_petrol.fuel_type, transmission_type = car_petrol.transmission_type, car_plate = car_petrol.car_plate, rental_days = 2, surname ="Angelina", last_name ="Jolie", age = "54", driver_license_id = "SW42902433", payment_info = "0021-4122-4362", numb_of_bookings = 1)
        self.assertEqual(booking_petrol.payment_fee_with_cost(), 155)


    def test_payment_fee_diesel_car(self):
        car_diesel = rent_car_management.Car("E21", "Diesel", "Automatic", "DF25132") 
        booking_diesel = rent_car_management.Booking(model = car_diesel.model , fuel_type = car_diesel.fuel_type, transmission_type = car_diesel.transmission_type, car_plate = car_diesel.car_plate, rental_days = 7, surname ="Angelina", last_name ="Jolie", age = "54", driver_license_id = "SW42902433", payment_info = "0021-4122-4362", numb_of_bookings = 1)
        self.assertEqual(booking_diesel.payment_fee_with_cost(), 355)


    def test_payment_fee_electric_car(self):
        car_electric = rent_car_management.Car("R11", "Electric", "Automatic", "MV012332") 
        booking_electric = rent_car_management.Booking(model = car_electric.model , fuel_type = car_electric.fuel_type, transmission_type = car_electric.transmission_type, car_plate = car_electric.car_plate, rental_days = 4, surname ="Angelina", last_name ="Jolie", age = "54", driver_license_id = "SW42902433", payment_info = "0021-4122-4362", numb_of_bookings = 1)
        self.assertEqual(booking_electric.payment_fee_for_electric_car(), 136.8)

    def test_payment_fee_vip_client(self):
        car = rent_car_management.Car("D40", "Electric", "Automatic", "WE801114")
        vip__customer = rent_car_management.CustomerService("George", "Clooney", "62", "VI37824", "1234-6543-8765", 7)
        rent_car_management.CustomerService.customer_vip_list = [vip__customer.driver_license_id]
        booking_vip = rent_car_management.Booking(model = car.model, fuel_type = car.fuel_type, transmission_type = car.transmission_type, car_plate = car.car_plate, rental_days = 2, surname = "George", last_name = "Clooney", age = "62", driver_license_id = "VI37824", payment_info ="1234-6543-8765", numb_of_bookings=7)
        self.assertEqual(booking_vip.payment_fee_vip_client(), 64.6)

        







if __name__ == "__main__" :
    unittest.main()