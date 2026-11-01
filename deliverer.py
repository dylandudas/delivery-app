from data_utilities.address_distances import DistanceTool
import datetime
from objects.package import DeliveryStatus

# Delivery Algorithm
def deliver(hub,distances, truck):
    dist = DistanceTool(distances) # See address_distances.py in data_utilities for DistanceTool
    current_address = hub
    closest_address = ""
    closest_package = None
    closest_id = None
    time = truck.time
    total_miles = 0
    pids = truck.pids.copy()

    #Loop for amount of provided package IDs
    for i in range(len(pids)):
        closest_distance = 1000.0

        # Check each package for closest distance
        for package_id in pids:
            package = truck.packages.get(package_id) # Query HASH Table with provided ID
            address = package.address # Extract address from package object
            distance = dist.get_distances(current_address, address) # Use DistanceTool to obtain distance values

            # Compare distances
            if distance < closest_distance:
                closest_address = address
                closest_distance = distance
                closest_package = package
                closest_id = package_id

        # Travel to closest found delivery address and deliver package
        minutes = (closest_distance / 18) * 60
        time += datetime.timedelta(minutes=minutes)
        truck.total_time += minutes
        total_miles += closest_distance
        current_address = closest_address
        closest_package.status = DeliveryStatus.DELIVERED
        closest_package.delivery_time = time
        pids.remove(closest_id)

        i += 1

    # Return to Hub
    to_hub_distance = dist.get_distances(current_address, "4001 South 700 East")
    minutes = (to_hub_distance / 18) * 60
    time += datetime.timedelta(minutes=minutes)
    total_miles += to_hub_distance
    truck.miles = total_miles

    return time
