"""_summary_
    In this example, you have a Vehicle class that is at the top of your class hierarchy. Then, you have 
    two concrete classes that inherit from Vehicle and extend it with new attributes. Finally, you have a 
    factory function that you’ll use to create instances of your classes.
"""


class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Car(Vehicle):
    def __init__(self, make, model, max_speed):
        super().__init__(make, model)
        self.max_speed = max_speed

class Truck(Vehicle):
    def __init__(self, make, model, loading_capacity):
        super().__init__(make, model)
        self.loading_capacity = loading_capacity

def vehicle_factory(cls, *args, **kwargs):
    return cls(*args, **kwargs)