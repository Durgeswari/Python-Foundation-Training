class Vehicle:
    def __init__(self, vehicle_id, model, make, year, color, registration_number, daily_rate, availability=True):
        self.vehicle_id = vehicle_id
        self.model = model
        self.make = make
        self.year = year
        self.color = color
        self.registration_number = registration_number
        self.daily_rate = daily_rate
        self.availability = availability
