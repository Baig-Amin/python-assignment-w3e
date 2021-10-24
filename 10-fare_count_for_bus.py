class Vehicle:
    def __init__(self, capacity):

        self.capacity = capacity

    def fare(self):
        
        fare_bus = self.capacity * 100 
        total_fare = fare_bus + (0.1 *fare_bus)
        return total_fare

class Bus(Vehicle):
    pass

setCapacity = 50
local_bus = Bus(setCapacity)
totalFare = local_bus.fare()

print(f"The bus seating capacity is {setCapacity}. so the final fare amount should be {totalFare}.")



# Another way by instructor 
# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#     def fare(self):
#         return self.capacity * 100
# class Bus(Vehicle):
#     def fare(self):
#         amount = super().fare()
#         amount += amount * 10 / 100
#         return amount
# _bus = Bus("Volvo", 12, 50)
# print("Total Bus fare is:", _bus.fare())
