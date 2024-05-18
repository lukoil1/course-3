class Car:
    def __init__(self, name, speed):
        print("oб'єкт створено", self)
        self.name = name
        self.speed = speed    
    def drive(self,):
        print("бібіка їде зі швидкістю", self.speed)
                

lada_sedan = Car("lastochka", 300)
lada_sedan.drive()