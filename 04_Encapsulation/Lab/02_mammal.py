class Mammal:
    def __init__(self, name: str, type: str, sound: str):
        self.name = name
        self.type = type
        self.sound = sound
        self.__kingdom = "animals"


    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self):
        return self.__kingdom


    def info(self):
        return f"{self.name} is of type {self.type}"