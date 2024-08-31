class Triangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def calculate_area(self):
        area = 0.5 * self.base * self.height
        print(f"Area :{area}")


tb,th = map(float,input("For T1 = ").split(","))
t1 = Triangle(tb,th)
t1.calculate_area()


t2b,t2h = map(float,input("For T2 = ").split(","))
t2 = Triangle(t2b,t2h)
t2.calculate_area()
