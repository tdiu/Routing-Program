import csv
from HashTable import HashTable
from Package import Package

class FileHandler:
    def __init__(self, file):
        self.file = file

    # Parses csv file and returns list
    def read(self):
        with open(self.file) as file:
            read = csv.reader(file, delimiter=";")
            return list(read)

    # Extracts information from package list and creates Package objects
    def extract_packages(self):
        package_table = HashTable()
        info = self.read()
        for row in info:
            pid = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            pzip = row[4]
            deadline = row[5]
            weight = row[6]

            package_table.insert_item(pid, Package(pid, address, city, state, pzip, deadline, weight))
        return package_table

    # Extracts information from addresses file and returns list of only addresses
    def extract_addresses(self):
        address_indexes = []
        addresses = self.read()
        for row in addresses:
            address_indexes.append(row[2])
        return address_indexes
