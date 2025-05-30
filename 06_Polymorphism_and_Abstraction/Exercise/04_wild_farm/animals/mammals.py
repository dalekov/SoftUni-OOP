from project.animals.animal import Mammal


class Mouse(Mammal):
    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if food.__class__.__name__ not in ["Vegetable", "Fruit"]:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += 0.10 * food.quantity


class Dog(Mammal):
    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if food.__class__.__name__ != "Meat":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += 0.40 * food.quantity


class Cat(Mammal):
    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if food.__class__.__name__ not in ["Vegetable", "Meat"]:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += 0.30 * food.quantity


class Tiger(Mammal):
    def make_sound(self):
        return "ROAR!!!"
    def feed(self, food):
        if food.__class__.__name__ != "Meat":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += 1 * food.quantity
