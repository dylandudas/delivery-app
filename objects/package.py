from enum import StrEnum


class Package:
    def __init__(self, id, address, city, state, zip_code, delivery_deadline, weight):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.loading_time = 0
        self.delivery_time = 0
        self.status = DeliveryStatus.HUB
        self.truck = None

    def __str__(self):
        return "ID: {}, Address: {}, City: {}, State: {}, Zip Code: {}, Weight: {}, Delivery Deadline: {}".format(self.id,self.address, self.city, self.state, self.zip_code, self.weight, self.delivery_deadline)

class DeliveryStatus(StrEnum):
    DELAYED = "DELAYED"
    HUB = "HUB"
    ENROUTE = "ENROUTE"
    DELIVERED = "DELIVERED"

