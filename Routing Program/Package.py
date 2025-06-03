import datetime


class Package:
    def __init__(self, pid, address, city, state,zip,deadline, weight):
        self.id = pid
        self.address = address
        self.deadline = deadline
        self.city = city
        self.state = state
        self.zip = zip
        self.weight = weight
        self.status = "At the HUB"
        self.depart_time = None
        self.delivery_time = None
        self.truck_id = None

    # Converts given string into time format
    @staticmethod
    def __time_conversion(time):
        (h, m, s) = time.split(":")
        return datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

    # Accepts user time and returns formatted string
    def get_status(self, time):
        time = self.__time_conversion(time)
        # Change delivery status depending on time
        if self.delivery_time >= time >= self.depart_time:
            self.status = "EN ROUTE"
        elif time >= self.delivery_time:
            self.status = "Delivered"
        else:
            self.status = "At the HUB"

        # Handles Displaying delivery time depending on specified time input
        if self.status == "Delivered":
            temp = self.delivery_time
        else:
            temp = "Undelivered"

        # Handle package 9 address change
        if self.id == 9 and time < self.__time_conversion("10:20:00"):
            self.address = "300 State St"
            self.zip = "84103"
        elif self.id == 9 and time >= self.__time_conversion("10:20:00"):
            self.address = "410 S. State St."
            self.zip = "84111"

        row = "{:<20} {:<5} {:40} {:>10} {:>10} {:>5} {:>15} {:>15}"
        return row.format(f"Package ID: {self.id}", self.truck_id, self.address, self.deadline, self.zip,self.weight, self.status, f"{temp}")

    def __str__(self):
         return ("PackageID: %s || Address: %s || Deadline: %s || ZIP: %s || Weight: %s || Status: %s"
                 % (self.id, self.address, self.deadline, self.zip,self.weight, self.status))