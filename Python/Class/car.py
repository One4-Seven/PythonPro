class Car():    # 创建实例 #
    def __init__(self,name,modle,year):
        self.name = name
        self.modle = modle
        self.year = year
        
    def describe(self):
        if self.modle == 'bmw':    # 处理特殊汽车型号 #
            message = f"\n{self.name.title()} {self.modle.upper()} {self.year}"      
        else:
            message = f"\n{self.name} {self.modle} {self.year}".title()
        print(message)
        
      