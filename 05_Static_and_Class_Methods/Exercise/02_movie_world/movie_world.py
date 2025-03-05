from project.customer import Customer
from project.dvd import DVD

class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = [] #list of customer objects
        self.dvds = [] #list of dvd objects

    @classmethod
    def dvd_capacity(cls):
        return 15

    @classmethod
    def customer_capacity(cls):
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)


    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = next((customer for customer in self.customers if customer.id == customer_id), None)
        dvd = next((dvd for dvd in self.dvds if dvd.id == dvd_id), None)

        if dvd in customer.rented_dvds:
                return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
                return "DVD is already rented"

        if dvd.age_restriction > customer.age:
                return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"


        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"


    def return_dvd(self, customer_id: int, dvd_id: int):
        customer = next((customer for customer in self.customers if customer.id == customer_id), None)
        dvd = next((dvd for dvd in self.dvds if dvd.id == dvd_id), None)

        if not dvd in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"

        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        output = []

        for customer in self.customers:
            output.append(repr(customer))

        for dvd in self.dvds:
            output.append(repr(dvd))

        return "\n".join(output)

