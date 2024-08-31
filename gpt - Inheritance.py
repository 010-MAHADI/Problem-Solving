class Phone:
    def __init__(self,model,name):
        self.model = model
        self.name = name
    def callme(self):
        print(f"{self.name} is so good")

class Tecno(Phone):
    def __init__(self,model,price):
        self.price = price
        super().__init__(model,"tecno phone")
    def dakue(self):
            print(f"{self.price} is good price fo {self.model}")

class Nokia(Phone):
    def __init__(self,model,price):
        self.price = price
        super().__init__(model,"Nokia phone")
    def dakue(self):
        print(f"{self.price} is good price fo {self.model}")


tecno = Tecno("spark 8 pro","16000")
tecno.callme()
tecno.dakue()

nokia = Nokia("Myti 98", "274284")
nokia.callme()
nokia.dakue()