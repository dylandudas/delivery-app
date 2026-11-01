# 012661414
from deliverer import deliver
from datetime import datetime, timedelta
from data_utilities.csv_reader import csv_reader_packages, csv_reader_distances
from objects.truck import Truck
from ui import print_status_by_truck

# Import data and instantiate hash table
# See data_utilities for csv_reader.py and hash_table.py
packages = csv_reader_packages("data/packages.csv")
distances = csv_reader_distances("data/distancematrix.csv")

# Initial time and location
# Delivery day is arbitrarily Oct 15, 2026 -- Deliveries begin at 8:00AM
start_time = datetime(year=2026, month= 10, day=15, hour=8, minute=0)
hub_location = "4001 South 700 East"

# Package IDs selected for each truck
truck1_pids = [1,13,14,15,16,19,20,29,30,31,34,37,40,21,22,23]
truck2_pids = [2,3,4,5,7,8,10,11,12,17,18,33,35,36,6,25]
truck3_pids = [9,28,32,26,27,38,39,24]

# Trucks are loaded and delivered using deliver()
# See deliverer.py for delivery algorithm

# Load truck 1 and leave HUB at 8:00AM
truck1 = Truck(1,packages,truck1_pids,start_time)
t1_time = deliver(hub_location,distances, truck1)

# Load truck 2 and leave HUB at 9:05AM in order to accommodate delayed packages
truck2 = Truck(2,packages,truck2_pids,start_time + timedelta(hours=1,minutes=5))
t2_time = deliver(hub_location,distances, truck2)

# Load truck 3 and leave once truck 3 returns
truck3 = Truck(3,packages,truck3_pids,t1_time)
t3_time = deliver(hub_location,distances, truck3)

# Total Miles
total_miles = truck1.miles + truck2.miles + truck3.miles
print(f"Total miles traveled: {total_miles:.2f}")

# Prompt user for time
print("Enter time for package statuses:")
user_time = input()
time_input = datetime.strptime(user_time, "%I:%M %p").time()

# Print package statuses by truck at user time
print_status_by_truck(time_input,truck1)
print_status_by_truck(time_input,truck2)
print_status_by_truck(time_input,truck3)









