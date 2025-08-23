import datetime

class VehicleRent:
    print("======== Welcome to Vehicle Rental Service ========")

    def __init__(self, totalStock):
        self.totalStock = totalStock
        self.availableStock = totalStock
        self.rentalTime = 0
        self.rentalBasis = 0
        self.numOfVehicle = 0

    def displayStock(self):
        print(f"We have currently {self.availableStock} vehicles available to rent.")

    def rentHourly(self, n):
        if n <= 0:
            print("Number should be positive")
            return -1
        elif n > self.availableStock:
            print(f"Sorry, we have currently {self.availableStock} vehicles available to rent")
            return -1
        else:
            self.rentalTime = datetime.datetime.now()
            self.rentalBasis = 1
            self.numOfVehicle = n
            self.availableStock -= n
            print(f"You have rented {n} vehicle(s) on hourly basis at {self.rentalTime}")
            return self.rentalTime

    def rentDaily(self, n):
        if n <= 0:
            print("Number should be positive")
            return -1
        elif n > self.availableStock:
            print(f"Sorry, we have currently {self.availableStock} vehicles available to rent")
            return -1
        else:
            self.rentalTime = datetime.datetime.now()
            self.rentalBasis = 2
            self.numOfVehicle = n
            self.availableStock -= n
            print(f"You have rented {n} vehicle(s) on daily basis at {self.rentalTime}")
            return self.rentalTime

    def returnVehicle(self, request):
        car_hour_price = 10
        car_day_price = 80
        bike_hour_price = 5
        bike_day_price = 50

        if not request:
            return None
            
        self.rentalTime, self.rentalBasis, self.numOfVehicle = request
        bill = 0

        if self.rentalTime and self.rentalBasis and self.numOfVehicle:
            self.availableStock += self.numOfVehicle
            now = datetime.datetime.now()
            rentalPeriod = now - self.rentalTime

            if self.rentalBasis == 1:   # hourly
                bill = self.numOfVehicle * car_hour_price * (rentalPeriod.seconds / 3600)
            elif self.rentalBasis == 2: # daily
                bill = self.numOfVehicle * car_day_price * (rentalPeriod.days + rentalPeriod.seconds / 86400)
            elif self.rentalBasis == 3: # bike hourly
                bill = self.numOfVehicle * bike_hour_price * (rentalPeriod.seconds / 3600)
            elif self.rentalBasis == 4: # bike daily
                bill = self.numOfVehicle * bike_day_price * (rentalPeriod.days + rentalPeriod.seconds / 86400)

            if (3 <= self.numOfVehicle <= 5):
                print("You are eligible for family rental promotion of 30% discount")
                bill *= 0.7

            print("Thanks for returning your vehicle. Hope you enjoyed our service")
            print(f"Your bill is ${bill:.2f}")
            self.rentalTime, self.rentalBasis, self.numOfVehicle = 0, 0, 0
            return bill
        else:
            print("Invalid return. No record found.")
            return None


class CarRent(VehicleRent):
    discount_rate = 15

    def __init__(self, totalStock):
        super().__init__(totalStock)

    def discount(self, bill):
        return bill - (bill * self.discount_rate / 100)


class BikeRent(VehicleRent):
    def __init__(self, totalStock):
        super().__init__(totalStock)

    def rentHourly(self, n):
        result = super().rentHourly(n)
        if result != -1:
            self.rentalBasis = 3  # Bike hourly basis
        return result

    def rentDaily(self, n):
        result = super().rentDaily(n)
        if result != -1:
            self.rentalBasis = 4  # Bike daily basis
        return result


class Customer:
    def __init__(self):
        self.bikes = 0
        self.rentalBasis_b = 0
        self.rentalTime_b = 0

        self.cars = 0
        self.rentalBasis_c = 0
        self.rentalTime_c = 0

    def requestVehicle(self, rentType):
        if rentType == "car":
            vehicles = int(input("How many cars do you want to rent? "))
            if vehicles < 1:
                print("Number should be greater than zero")
                return -1
            else:
                self.cars = vehicles
                return vehicles
        elif rentType == "bike":
            vehicles = int(input("How many bikes do you want to rent? "))
            if vehicles < 1:
                print("Number should be greater than zero")
                return -1
            else:
                self.bikes = vehicles
                return vehicles
        else:
            print("Request error")
            return -1

    def returnVehicle(self, rentType):
        if rentType == "car":
            if self.rentalTime_c and self.rentalBasis_c and self.cars:
                return self.rentalTime_c, self.rentalBasis_c, self.cars
            else:
                return 0, 0, 0
        elif rentType == "bike":
            if self.rentalTime_b and self.rentalBasis_b and self.bikes:
                return self.rentalTime_b, self.rentalBasis_b, self.bikes
            else:
                return 0, 0, 0
        else:
            return 0, 0, 0


# Main program
bikeShop = BikeRent(10)
carShop = CarRent(20)
customer = Customer()

while True:
    print("\n======== Vehicle Rental Service ========")
    print("1. Display available vehicles")
    print("2. Rent a car")
    print("3. Rent a bike")
    print("4. Return a car")
    print("5. Return a bike")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        bikeShop.displayStock()
        carShop.displayStock()
    elif choice == '2':
        cars = customer.requestVehicle("car")
        if cars != -1:
            basis = input("Rent hourly or daily? (h/d): ").lower()
            if basis == 'h':
                carShop.rentHourly(cars)
                customer.rentalTime_c = carShop.rentalTime
                customer.rentalBasis_c = carShop.rentalBasis
            elif basis == 'd':
                carShop.rentDaily(cars)
                customer.rentalTime_c = carShop.rentalTime
                customer.rentalBasis_c = carShop.rentalBasis
            else:
                print("Invalid basis")
    elif choice == '3':
        bikes = customer.requestVehicle("bike")
        if bikes != -1:
            basis = input("Rent hourly or daily? (h/d): ").lower()
            if basis == 'h':
                bikeShop.rentHourly(bikes)
                customer.rentalTime_b = bikeShop.rentalTime
                customer.rentalBasis_b = bikeShop.rentalBasis
            elif basis == 'd':
                bikeShop.rentDaily(bikes)
                customer.rentalTime_b = bikeShop.rentalTime
                customer.rentalBasis_b = bikeShop.rentalBasis
            else:
                print("Invalid basis")
    elif choice == '4':
        request = customer.returnVehicle("car")
        bill = carShop.returnVehicle(request)
        if bill:
            if bill > 100:
                bill = carShop.discount(bill)
                print(f"After discount: ${bill:.2f}")
    elif choice == '5':
        request = customer.returnVehicle("bike")
        bikeShop.returnVehicle(request)
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")