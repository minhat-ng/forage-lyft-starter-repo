from tires.tire import Tire

class CarriganTire(Tire): 
    def __init__(self, tires) -> None:
        self.tires = tires
        
    def needs_service(self) -> bool: 
        for tire in self.tires:
            if tire >= 0.9: 
                return True
        return False
        