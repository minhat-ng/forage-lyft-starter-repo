from tires.tire import Tire

class OctoprimeTire(Tire): 
    def __init__(self, tires) -> None:
        self.tires = tires
        
    def needs_service(self) -> bool: 
        return sum(self.tires) >= 3