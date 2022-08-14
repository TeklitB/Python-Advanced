
class Tire:
    def __init__(self, size):
        self.size = size
    
    def get_pressure(self):
        print("Pressure")
    
    def pump(self):
        print("Pumping the tire.")

class Engine:
    def __init__(self, ftype):
        self.fuel_type = ftype
    
    def start(self):
        print("Starting the engine.")
    
    def stop(self):
        print("Stopping the engine.")
    
    def get_state(self):
        print("Uknown state.")

class Vehicle:
    def __init__(self, VIN, engine, tires):
        self.VIN = VIN
        self.engine = engine
        self.tires = tires
        

city_tires = Tire(15)
off_road_tires = Tire(18)

electric_engine = Engine("Electric")
petrol_engine = Engine("Petrol")

city_car = Vehicle("PN123", electric_engine, city_tires)
city_car.engine.start()
city_car.tires.pump()

terrain_car = Vehicle("SN564", petrol_engine, off_road_tires)
terrain_car.engine.start()
terrain_car.tires.pump()







