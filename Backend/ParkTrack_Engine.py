class ParkingEngine:
    def __init__ (self, total_spots=24, total_moto_spots=24):
        self.car_slots = {f"Spot {i}": None for i in range(1, total_car_spots + 1)}
        self.moto_slots = {f"Moto Spot {i}": None for i in range(1, total_moto_spots +1)}
    
    def get_slot_data(self, spot_label):
        if spot_label.startwith("Moto"):
            return self.moto_slots.get(spot_label)
        return self.car_slots.get(spot_label)
    
    def is_occupied(self, spot_label):
        return self.get_slot_data(spot_label) is not None
    
    def allocate_spot(self, spot_label, customer_data):
        if spot_label.startwith("Moto):
            self.moto_slots[spot_label] = customer_data
        else:
            self.car_slots[spot_label] = customer_data
        
    def release_spot(self, spot_label):
        if spot_label.startswith("Moto"):
            self.moto_slots[spot_label] = None
        else:
            self.car_slots[spot_label] = None
        
    def get_car_slots(self):
        return self.car_slots.items()

    def get_moto_slots(self):
        return self.moto_slots.items()
