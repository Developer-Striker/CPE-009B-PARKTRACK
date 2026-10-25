from datetime import datetime, time

class BillingEngine:
    mall_closing_time = time (15, 28)
    overstay_fee = 150.0
    
    @staticmethod
    def is_overstaying(time_in, current_time=None, is_exempt=False):
        if is_exempt:
            return False
        now = current_time or datetime.now()
        if now.date() > time_in.date():
            return True
        if time_in.time() < BillingEngine.mall_closing_time <= now.time():
            return True
        return False
        
    @staticmethod
    def calculate_bill(time_in, time_out, base_rate, hourly_fee, is_exempt=False):
        duration = time_out - time_in
        hours_parked = max(1.0, duration.total_seconds() / 3600.0)
        additional_hours = max(0.0, hours_parked - 1.0)
        total_bill = base_rate + (additional_hours * hourly_fee)
        
        if BillingEngine.is_overstaying(time_in, time_out, is_exempt):
            total_bill += BillingEngine.overstay_fee
            
        return hours_parked, total_bill
