import os

class Receipt:
    @staticmethod
    def export_ticket_receipt(spot, data, checkout_dt, hours, bill):
        filename = f"ticket_{spot}_{data['customer'].replace('_')}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write("=========================================\n")
            file.write("        PARKING RECEIPT INVOICE         \n")
            file.write("=========================================\n")
            file.write(f"Customer/Plate: {data['customer']}\n")
            file.write(f"Assigned Space: {spot}\n")
            file.write(f"Arrival Time: {data['time_in'].strftime('%Y-%m-%d %I:%M:%S %p')}\n")
            file.write(f"Departure Time: {checkout_dt.strftime('%Y-%m-%d %I:%M:%S %p')}\n")
            file.write(f"Duration Track: {hours:.2f} hr/s\n")
            file.write('-----------------------------------------\n')
            file.write(f"TOTAL CHARGED: P{bill:.2f}\n")
            file.write("=========================================\n")
            