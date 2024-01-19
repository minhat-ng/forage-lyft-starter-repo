import unittest
from datetime import datetime

from battery.battery_types.nubbin_battery import NubbinBattery
from battery.battery_types.spindler_battery import SpindlerBattery


from engine.engine_types.capulet_engine import CapuletEngine
from engine.engine_types.sternman_engine import SternmanEngine
from engine.engine_types.willoughby_engine import WilloughbyEngine



class TestNubbinBattery(unittest.TestCase): 
    def test_needs_service_nubbin_true(self): 
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        battery = NubbinBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())
        
    def test_needs_service_nubbin_false(self): 
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        battery = NubbinBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_spindler_true(self): 
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 8)
        battery = SpindlerBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())
        
    def test_needs_service_spindler_false(self): 
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = SpindlerBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())
        
class TestCapuletEngine(unittest.TestCase): 
    def test_needs_service_capulet_true(self): 
        current_milage = 30002
        last_service_milage = 1
        engine = CapuletEngine(current_milage, last_service_milage)
        self.assertTrue(engine.needs_service())
    
    def test_needs_service_capulet_false(self): 
        current_milage = 4000
        last_service_milage = 4000
        engine = CapuletEngine(current_milage, last_service_milage)
        self.assertFalse(engine.needs_service())

class TestSternmanEngine(unittest.TestCase): 
    def test_needs_service_sternman_true(self): 
        warning_light_on = True
        engine = SternmanEngine(warning_light_on)
        self.assertTrue(engine.needs_service())
    
    def test_needs_service_sternman_false(self): 
        warning_light_on = False
        engine = SternmanEngine(warning_light_on)
        self.assertFalse(engine.needs_service())

class TestWilloughbyEngine(unittest.TestCase): 
    def test_needs_service_willoughby_true(self): 
        current_milage = 600000
        last_service_milage = 1
        engine = WilloughbyEngine(current_milage, last_service_milage)
        self.assertTrue(engine.needs_service())
    
    def test_needs_service_capulet_willoughby_false(self): 
        current_milage = 6000
        last_service_milage = 1999
        engine = WilloughbyEngine(current_milage, last_service_milage)
        self.assertFalse(engine.needs_service())


if __name__ == '__main__':
    unittest.main()
