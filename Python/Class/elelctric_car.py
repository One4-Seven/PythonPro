from car import Car as C

class Battery:
    def __init__(self):
        self.battery_total = 45
          
    def update_battery(self):
        if self.battery_total != 60:
            self.battery_total = 60

    def show_range(self):
        if self.battery_total == 45:
            print("The car can drive 220 km")
        else:
            print("The car can drive 310 km")
    
class Electric_car(C):
    def __init__(self, name, modle, year):
        super().__init__(name, modle, year)
        self.battery = Battery()
        
    def describe(self):
        super().describe()
        print(f"The car's battery is {self.battery.battery_total} W\n")

