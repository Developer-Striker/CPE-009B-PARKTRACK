import os
from ParkTrack_Billing import BillingEngine

class Receipt:
    @staticmethod
    def export_ticket_receipt(spot, data, checkout_dt, hours, bill):
        filename = f"ticket_{spot}_{data['customer'].replace(' ', '_')}.txt"
        vehicle_type = data.get("vehicle_type", "Car")
        is_exempt = data.get("is_exempt", False)
        is_overstay = BillingEngine.is_overstaying(data["Time_in"], checkout_dt, is_exempt)
        with open(filename, "w", encoding="utf-8") as file:
            file.write("=========================================\n")
            file.write("        PARKING RECEIPT INVOICE         \n")
            file.write("=========================================\n")
            file.write(f"Customer/Plate: {data['customer']}\n")
            file.write(f"Vehicle Type:   {vehicle_type}\n")
            file.write(f"Assigned Space: {spot}\n")
            file.write(f"Arrival Time:   {data['time_in'].strftime('%Y-%m-%d %I:%M:%S %p')}\n")
            file.write(f"Departure Time: {checkout_dt.strftime('%Y-%m-%d %I:%M:%S %p')}\n")
            file.write(f"Duration Track: {hours:.2f} hr/s\n")
            file.write('-----------------------------------------\n')
            if is_overstay:
                file.write("Overnight Surcharge (Past 10:30 PM): P150.00\n")
                file.write('-----------------------------------------\n')
            elif is_exempt:
                file.write("Exemption Status: Cinema/Overnight Pass\n")
                file.write('-----------------------------------------\n')                
            file.write(f"TOTAL CHARGED:  P{bill:.2f}\n")
            file.write("=========================================\n")
