from serviceable import Serviceable

class Car(Serviceable): 
    def __init__(self, engine_type, battery_type):
        self.engine = engine_type
        self.battery = battery_type
    
    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service() 
    