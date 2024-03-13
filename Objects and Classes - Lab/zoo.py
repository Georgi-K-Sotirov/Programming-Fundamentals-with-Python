class Zoo:
    __animals = 0

    def __init__(self, name_of_zoo):
        self.name_of_zoo = name_of_zoo
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            return f"{species.capitalize()}s in {self.name_of_zoo}: "+ ", ".join(self.mammals) +\
                   f"\nTotal animals: {Zoo.__animals}"
        elif species == "fish":
            return f"{species.capitalize()}es in {self.name_of_zoo}: " + ", ".join(self.fishes) +\
                   f"\nTotal animals: {Zoo.__animals}"
        elif species == "bird":
            return f"{species.capitalize()}s in {self.name_of_zoo}: " + ", ".join(self.birds) +\
                   f"\nTotal animals: {Zoo.__animals}"


name = input()
zoo = Zoo(name)
animals = int(input())

for x in range(animals):
    species_of_animal, name_of_animal = input().split()
    zoo.add_animal(species_of_animal, name_of_animal)

info_for_species = input()

print(zoo.get_info(info_for_species))

