class Truck:
    def __init__(self, load: list, truck_id, depart_time):
        self.capacity = 16
        self.speed = 18
        self.depart_time = depart_time
        self.load = load
        self.miles = float(0)
        self.address = "4001 South 700 East"
        self.truck_id = truck_id
        self.undelivered = load
        self.curr_time = depart_time

    def get_miles(self):
        return self.miles

    def __str__(self):
        return "Truck ID: %s, Miles: %s, Address: %s, Departure Time: %s" % (self.truck_id, self.miles, self.address, self.depart_time)