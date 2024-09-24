from car import *

class Gas:
    def __init__(self):
        self.gas_total = 100
        
    def show_range(self):
        print(f"The car can drive {self.gas_total * 2} km")
        
    def set_gas(self,number):
        if number > self.gas_total:
            self.gas_total = number
            
    def up_gas(self,number):
        if number > 0:
            self.gas_total += number

    def down_gas(self,number):
        if self.gas_total - number > 0:
            self.gas_total -= number
            
class Gas_car(Car):
    def __init__(self, name, modle, year):
        super().__init__(name, modle, year)
        self.gas = Gas()
        
    def describe(self):
        super().describe()
        print(f"The car's gas remain {self.gas.gas_total} L\n")
        



