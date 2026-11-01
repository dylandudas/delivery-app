from objects.package import DeliveryStatus


class Truck:
    def __init__(self,truck_num, packages,pids,time):
        self.packages = packages
        self.pids = pids
        self.time = time
        self.truck_num = truck_num
        self.miles = 0
        self.total_time = 0

        for pid in pids:
            pack = packages.get(pid)
            pack.status = DeliveryStatus.ENROUTE
            pack.loading_time = time
            pack.truck = truck_num

