from HashTable import HashTable

class Menu:
    def __init__(self, total_distance, package_table: HashTable):
        self.total_distance = total_distance
        self.package_table = package_table

    def show_menu(self):
        usr_exit = False

        # Continues asking for menu input until user enters 3
        while usr_exit is False:
            print("Welcome to WGUPS Delivery System")
            print("Please select an option")
            print(f"The total distance travelled for this route is: {self.total_distance} miles")
            print("1. View the delivery status of one package")
            print("2. View the delivery status of all packages")
            print("3. Exit")

            try:
                # Formatting for headers
                headers = "PackageID TruckID Address Due ZIP Weight Status Delivered".split()
                row = "{:<17} {:<10} {:40} {:>5} {:>12} {:>8} {:>10} {:>18}"
                selected = int(input("Selection: "))
                match selected:
                    case 1:
                        try:
                            # Asks for packageID and prints information associated with the package at specified time
                            package_id = int(input("Please enter the package ID: "))
                            package = self.package_table.get_item(package_id)
                            time = (input("Please enter the time you wish to view the delivery status. Use the format: HH:MM:SS \n"))
                            print(f"Displaying information for package {package_id} at time {time}:\n")
                            print(row.format(*headers))
                            print(f"{'-' * 130}")
                            print(f"{package.get_status(time)}\n")
                        except:
                            print("Invalid input. Please try again.")
                    case 2:
                        try:
                            # Asks for time and prints information for all packages
                            time = (input("Please enter the time you wish to view the delivery status. Use the format: HH:MM:SS \n"))
                            print(f"Displaying information for all packages at {time}:\n")
                            print(row.format(*headers))
                            print(f"{'-' * 130}")
                            for i in range(1,41):
                                package = self.package_table.get_item(i)
                                print(package.get_status(time))
                            print("\n")
                        except:
                            print("Invalid input. Please try again.")
                    case 3:
                        usr_exit = True

            except:
                print("Invalid input. Please try again.")
                continue




