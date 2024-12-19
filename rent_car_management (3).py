import abc

class Car:
    def __init__(self, model, fuel_type, transmission_type, car_plate):
        self.model = model
        self.fuel_type = fuel_type
        self.transmission_type = transmission_type
        self.car_plate = car_plate
        self.car_available = True

  
        
class CarMaintenance(abc.ABC):
    @abc.abstractmethod
    def return_info_car(self):
        pass

    @abc.abstractmethod
    def calculate_maintenance_cost(self):
        pass
    
class UseAbstract(CarMaintenance):
    
    def return_info_car(self, model, fuel_type, transmission_type, car_plate):
       
        return f'Model: {model} Fuel Type: {fuel_type}, Transmission: {transmission_type}, Car Plate: {car_plate}'
    
    def maintenance_cost(self):
        return 150

 
class Customer:
    def __init__(self, surname, last_name, age, driver_license_id, payment_info):
        self.surname = surname
        self.last_name = last_name
        self.age = age
        self.driver_license_id = driver_license_id
        self.payment_info = payment_info
       
    
    def check_if_customer_is_underage(self):
        if self.age < 18:
            print("The client must be 18 years old or older in order to use our services")
            return False
        else:
            print("The customer can proceed")
            return True
    


class CustomerService(Customer):
    def __init__(self,  surname, last_name, age, driver_license_id, payment_info, numb_of_bookings):
        super().__init__(surname, last_name, age, driver_license_id, payment_info)
        self.customer_list = []
        self.customer_vip_list = []
        self.numb_of_bookings = numb_of_bookings
        
    
    def register_client(self):
            if self.driver_license_id not in self.customer_list and self.numb_of_bookings == 0:
                new_client = Customer(self.surname, self.last_name, self.age, self.driver_license_id, self.payment_info)
                self.customer_list.append(new_client)
                print(f'New client {self.driver_license_id} was successfully registered')
            else:
                print("Impossible to register the client")
    
    def sign_off(self):
        for client in self.customer_list:
            if client.driver_license_id == self.driver_license_id:
                self.customer_list.remove(client)
                print(f'Client {self.driver_license_id} was successfully signed off')
    
    def add_customer_in_vip(self):
        if self.driver_license_id not in self.customer_vip_list and self.numb_of_bookings >= 3:
            new_vip_client = Customer(self.surname, self.last_name, self.age, self.driver_license_id, self.payment_info)
            self.customer_vip_list.append(new_vip_client)
            print("A new client made our VIP list!")
        else:
            print("The client doesn't meet the VIP requirments")
                


class Booking:
    def __init__(self, model, fuel_type, transmission_type, car_plate, rental_days, surname, last_name, age, driver_license_id, payment_info, numb_of_bookings):
        self.car = Car(model, fuel_type, transmission_type, car_plate)
        self.customer = CustomerService(surname, last_name, age, driver_license_id, payment_info, numb_of_bookings)
        self.available_cars = []
        self.rental_days = rental_days

    
    def rent_car(self, car_plate):
            if self.rental_days <=0:
                print("Impossible to proceed with the booking")
                return
            
            for available_car in self.available_cars:
                if available_car.car_plate == car_plate:
                    self.car_available = False
                    self.available_cars.remove(available_car)
                    print("The car was successfully booked")
                    return

           
    def returned_car(self, car_plate):
        if self.car.car_plate == car_plate:
            self.car_available = True
            self.available_cars.append(self.car)
            print("The car was successfully returned")

    
    def payment_fee_with_cost(self):
        if self.car.fuel_type == "Petrol":
            additional_charge = 79
            price_with_added_cost = (38 * self.rental_days) + additional_charge
        elif self.car.fuel_type == "Diesel":
            additional_charge = 89
            price_with_added_cost = (38 * self.rental_days) + additional_charge
           

        return price_with_added_cost
    
    def payment_fee_for_electric_car(self):
        if self.car.fuel_type == "Electric":
            discount = 0.10
            price_with_discount = (38 * self.rental_days) * (1- discount)
           
        
        return price_with_discount


    def payment_fee_vip_client(self):
        if self.customer.driver_license_id in CustomerService.customer_vip_list:
            discount = 0.15
            price_with_discount = (38 * self.rental_days) * (1- discount)
        
        return price_with_discount


if __name__ == "__main__":

    underage_customer = Customer("Johnny", "Joe", 17, "Fw92322", "1354-5345-9973")
    underage_customer.check_if_customer_is_underage()

    adult_customer = Customer("Anthony", "Hopkins", 22, "QW2434532", "0234-6643-9927")
    adult_customer.check_if_customer_is_underage()

    new_customer = CustomerService("Johnny", "Depp", "44", "B274213412", "3134-4652-6543", 0)
    new_customer.register_client()

    signing_off_client = CustomerService("Brad", "Pitt", "62", "DE12345941", "9713-9077-1112", 2)
    signing_off_client.sign_off()

    vip_customer = CustomerService("Leo", "Dicaprio", "57", "GW7938274", "1412-0483-0000", 5)
    vip_customer.add_customer_in_vip()

    rented_car = Booking("F23", "Diesel", "Automatic", "J837420", 5, "Johnny", "Depp", "44", "B274213412", "3134-4652-6543", 0)
    rented_car.rent_car("J837420")

    returned_car = Booking("D40", "Electric", "Automatic", "WE801114", 11, "Brad", "Pitt", "62", "DE12345941", "9713-9077-1112", 2)
    returned_car.returned_car(car_plate = "WE801114")

    car_petrol = Booking("Z99", "Petrol", "Manual", "KH92732", 1, "Brad", "Pitt", "62", "DE12345941", "9713-9077-1112", 2)
    car_petrol.payment_fee_with_cost()

    
   

    

    
   

    
       
        

    





