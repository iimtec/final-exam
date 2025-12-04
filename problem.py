class DeliveryOrder:
    def __init__(self, customer, item, status = "preparing"):
        self.customer = customer
        self.item = item
        self.status = status

    def assign_driver(driver):
        return driver
    
    def summary(self):
        return "Order Summary:\n"\
                f"Item: {self.item}\n"\
                f"Customer: {self.customer}\n"\
                f"Status: {self.status}\n"\
                f"Driver: {d.name}\n"

class Person:
    def __init__(self,name):
        self.name = name

    def introduce(self):
        print(f"Hi, I'm {self.name}.")

class Customer(Person):
    def __init__(self, name, address):
        super().__init__(name)
        self.address = address

    def place_order(item):
        return DeliveryOrder(item)
    
class Driver(Person):
    def __init__(self, name, vehicle):
        self.vehicle = vehicle
        super().__init__(name)

    def deliver(self,order):
        print(f"{self.name} is delivering {order.item} to {order.customer} using {self.vehicle}")

a = Person("Alice")
b = Person("Bob")
d = Driver("David","motorcycle")
order_a = DeliveryOrder("Alice","Laptop")
order_b = DeliveryOrder("Bob","Headphones")
a.introduce()
b.introduce()
d.introduce()
print()
print(order_a.summary())
print(order_b.summary())
d.deliver(order_a)
d.deliver(order_b)
print()
print("Final Status:")
print(f"Order for {order_a.item} -> delivered")
print(f"Order for {order_b.item} -> delivered")