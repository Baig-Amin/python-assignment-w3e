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
