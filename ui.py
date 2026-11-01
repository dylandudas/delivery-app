from datetime import datetime
from objects.package import DeliveryStatus

# Takes user time and truck object and prints the status of the truck's packages at that time
def print_status_by_truck(time_input,truck):
    last_update = 0
    day_start = datetime(year=2026, month= 10, day=15, hour=8, minute=0).time()
    WIDTH = 165

    print("-" * WIDTH)
    print(f"{'Truck ' + str(truck.truck_num):^165}")
    print(f"{'Package':140}{'Status':^15}{'Last Update':>10}")
    print("-" * WIDTH)

    # Check package statuses and selected time
    # Handles DELAYED packages and incorrect address
    for pid in truck.pids:
        user_p = truck.packages.get(pid)

        if pid == 9 and time_input < datetime(year=2026, month= 10, day=15, hour=10, minute=20).time():
            user_p.address = "300 State St"
            user_p.zip_code = "84103"

        if (pid == 28 or pid == 32 or pid == 25 or pid == 6) and (time_input < datetime(year=2026, month= 10, day=15, hour=9, minute=5).time()):
            user_p.status = DeliveryStatus.DELAYED
            last_update = day_start

        elif user_p.loading_time.time() <= time_input < user_p.delivery_time.time():
            user_p.status = DeliveryStatus.ENROUTE
            last_update = user_p.loading_time.time()

        elif time_input < user_p.loading_time.time():
            user_p.status = DeliveryStatus.HUB
            last_update = day_start

        elif time_input >= user_p.delivery_time.time():
            user_p.status = DeliveryStatus.DELIVERED
            last_update = user_p.delivery_time.time()


        print(f"{str(user_p):140}{str(user_p.status):^15}{str(last_update):>10}")

    tm = round(truck.miles,1)
    tt = int(truck.total_time)

    print("-" * WIDTH)
    print(f"{'Truck ' + str(truck.truck_num) + ' UPON COMPLETION: total miles: ' + str(tm) + ' | total time: ' + str(tt) + ' minutes':^165}")
    print("-" * WIDTH)