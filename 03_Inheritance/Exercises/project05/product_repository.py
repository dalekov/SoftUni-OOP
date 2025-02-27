from project.product import Product
from project.food import Food
from project.drink import Drink

class ProductRepository:
    def __init__(self):
        self.products = [] # List of all product objects


    def add(self, product: Product):
        self.products.append(product)


    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)


    def __repr__(self):
        output = []
        for product in self.products:
            output.append(f"{product.name}: {product.quantity}")

        return "\n".join(output)



