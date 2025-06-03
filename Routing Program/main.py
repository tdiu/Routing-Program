# Student ID: 011536308
# Name: Tony Diu

from FileHandler import FileHandler
from Truck import Truck
from datetime import timedelta
from Menu import Menu

# Read and extract data from packages.csv to hashtable
packages = FileHandler("packages.csv").extract_packages()
# Extract data from distances.csv
distances = FileHandler("distances.csv").read()
# Extract data from addresses.csv
addresses = FileHandler("addresses.csv").extract_addresses()

# Get address index from list of addresses
def address_index(address):
    return addresses.index(address)

# Determine distance between two locations
def distance_between(start, end):
    dist = distances[start][end]
    if dist == "":
        dist = distances[end][start]
    return float(dist)

# Finds lowest distance from current address to other undelivered package addresses
def lowest_distance(truck):
    # Array to hold distances between current address and all other addresses
    dist_arr = []
    # Iterate through undelivered packages and find the minimum
    for package in truck.undelivered:
        dist = distance_between(address_index(truck.address), address_index(packages.get_item(package).address))
        dist_arr.append(dist)

    # Return lowest distance and index of next delivery address
    return float(min(dist_arr)), dist_arr.index(min(dist_arr))

def deliver_packages(truck):
    # Set status of all packages
    for undelivered in truck.undelivered:
        packages.get_item(undelivered).status = "EN ROUTE"
        packages.get_item(undelivered).depart_time = truck.curr_time
        packages.get_item(undelivered).truck_id = truck.truck_id

    # Continuously loop through nearest neighbour until all packages delivered
    while len(truck.undelivered) > 0:
        # Find next delivery with the shortest distance from current point
        next_distance, next_address = lowest_distance(truck)
        index = truck.undelivered[next_address]
        package = packages.get_item(index)
        print(index, package)
        truck.address = package.address

        # Update time, miles travelled, and set status to delivered
        truck.miles += next_distance
        truck.curr_time += timedelta(hours=next_distance/truck.speed)
        package.delivery_time = truck.curr_time
        package.status = "DELIVERED"

        # Remove package from list of undelivered packages
        truck.undelivered.remove(index)

    # Only truck 1 returns to HUB after finishing deliveries to await truck 3 start
    if truck.truck_id == 1:
        return_distance = distance_between(address_index(truck.address), address_index(addresses[0]))
        truck.miles += return_distance
        truck.curr_time += timedelta(hours=return_distance/truck.speed)

class Main:
    # Loading trucks and setting departure times
    truck_one = Truck([13,14,15,16,19,20,1,29,30,31,34,37,40], 1, timedelta(hours=8, minutes=0))
    truck_two = Truck([6,25,3,18,36,38,26,27,33,35,39], 2, timedelta(hours=9, minutes=5))
    truck_three = Truck([9,28,32,2,4,5,7,8,10,11,12,17,22,23,24,21], 3, timedelta(hours=10, minutes=20))

    # Deliver packages
    deliver_packages(truck_one)
    deliver_packages(truck_two)
    deliver_packages(truck_three)

    # Calculate total distance
    total_dist = truck_one.miles + truck_two.miles + truck_three.miles

    print(f"Truck one departed at: {truck_one.depart_time}")
    print(f"Truck two departed at: {truck_two.depart_time}")
    print(f"Truck three departed at: {truck_three.depart_time}")
    # Display Menu
    menu = Menu(total_dist, packages).show_menu()