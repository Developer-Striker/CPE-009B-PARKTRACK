class ParkingEngine:
    def __init__ (self, total_spots=24):
        self.parking_slots = {f"Spot {i}": None for i in range(1, total_spots + 1)}
        
    def get_slot_data(self, spot_label):
        return self.parking_slots.get(spot_label)
    
    def is_occupied(self, spot_label):
        return self.parking_slots.get(spot_label) is not None
    
    def allocate_spot(self, spot_label, customer_data):
        self.parking_slots[spot_label] = customer_data
        
    def release_spot(self, spot_label):
        self.parking_slots[spot_label] = None
        
    def get_all_slots(self):
        return self.parking_slots.items()