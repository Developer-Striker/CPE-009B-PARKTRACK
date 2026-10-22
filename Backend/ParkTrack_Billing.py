class BillingEngine:
    @staticmethod
    def calculate_bill(time_in, time_out, base_rate, hourly_fee):
        duration = time_out - time_in
        hours_parked = max(1.0, duration.total_seconds() / 60.0)
        additional_hours = max(0.0, hours_parked - 1.0)
        total_bill = base_rate + (additional_hours * hourly_fee)
        return hours_parked, total_bill