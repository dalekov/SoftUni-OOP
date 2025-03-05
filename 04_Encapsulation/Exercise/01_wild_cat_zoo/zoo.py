from project.animal import Animal
from project.worker import Worker

class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price) -> str:
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"

        if self.__budget < price:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name) -> str:
        worker = next((w for w in self.workers if w.name == worker_name))
        if worker:
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        total_salaries = sum(worker.salary for worker in self.workers)

        if self.__budget < total_salaries:
            return f"You have no budget to pay your workers. They are unhappy"
        self.__budget -= total_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self) -> str:
        budget_needed = sum(animal.money_for_care for animal in self.animals)

        if self.__budget < budget_needed:
            return f"You have no budget to tend the animals. They are unhappy."
        self.__budget -= budget_needed
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount) -> None:
        self.__budget += amount

    def animals_status(self):
        lions = [repr(animal) for animal in self.animals if animal.__class__.__name__ == "Lion"]
        tigers = [repr(animal) for animal in self.animals if animal.__class__.__name__ == "Tiger"]
        cheetahs = [repr(animal) for animal in self.animals if animal.__class__.__name__ == "Cheetah"]

        result = [f"You have {len(self.animals)} animals", f"----- {len(lions)} Lions:"]
        result.extend(lions)

        result.append(f"----- {len(tigers)} Tigers:")
        result.extend(tigers)

        result.append(f"----- {len(cheetahs)} Cheetahs:")
        result.extend(cheetahs)

        return "\n".join(result)

    def workers_status(self):
        keepers = [repr(worker) for worker in self.workers if worker.__class__.__name__ == "Keeper"]
        caretakers = [repr(worker) for worker in self.workers if worker.__class__.__name__ == "Caretaker"]
        vets = [repr(worker) for worker in self.workers if worker.__class__.__name__ == "Vet"]

        result = [f"You have {len(self.workers)} workers", f"----- {len(keepers)} Keepers:"]
        result.extend(keepers)

        result.append(f"----- {len(caretakers)} Caretakers:")
        result.extend(caretakers)

        result.append(f"----- {len(vets)} Vets:")
        result.extend(vets)

        return "\n".join(result)
