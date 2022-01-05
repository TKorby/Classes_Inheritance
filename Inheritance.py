class Animal:
    def __init__(self, name, weight, size, habitat):
        self.name = name
        self.weight = weight
        self.size = size
        self.habitat = habitat
        self.positionX = 0
        self.positionY = 0
        self.positionZ = 0
        self.hunger = 0
        self.tiredness = 0

    def move(self, x, y):
        self.positionX += x
        self.positionY += y

    def eat(self, foodSat):
        if self.hunger - foodSat <= 0:
            self.hunger = 0
        else:
            self.hunger -= foodSat

    # larger the animal, the more sleep they need
    def sleep(self, time):
        if self.size == "tiny":
            sleepMult = 0.9
        elif self.size == "small":
            sleepMult = 0.825
        elif self.size == "medium":
            sleepMult = 0.75
        elif self.size == "large":
            sleepMult = 0.7
        elif self.size == "huge":
            sleepMult = 0.6
        else:
            sleepMult = 1

        if self.tiredness - (time * sleepMult) <= 0:
            self.tiredness = 0
        else:
            self.tiredness -= time * sleepMult


class Fish(Animal):
    def __init__(self, name, weight, size, habitat, species, fins):
        super().__init__(name, weight, size, habitat)
        self.species = species
        self.fins = fins

    def swim(self, x_1, y_1, z_1):
        self.positionX += x_1
        self.positionY += y_1
        self.positionZ += z_1

    def getPosition(self):
        return self.positionX, self.positionY, self.positionZ


class Snake(Animal):
    def __init__(self, name, weight, size, habitat, species, poisonous):
        super().__init__(name, weight, size, habitat)
        self.species = species
        self.isPoisonous = poisonous
        self.posture = "Relaxed"

    def curl(self):
        self.posture = "Curled"

    def lunge(self, x_1, y_1, z_1):
        if self.posture == "Curled":
            self.positionX += x_1
            self.positionY += y_1
            self.positionZ += z_1
        else:
            self.positionX += x_1 * 0.25
            self.positionY += y_1 * 0.25
            self.positionZ += z_1 * 0.5


# Other examples of inheritance is as follows...
# ---------------------------

# Parent Classes
# ---------------
# Book
# Vehicle
# ---------------

# Child Classes
# -------------
# Textbook(Book)
# Address_Book(Book)

# Car(Vehicle)
# Bicycle(Vehicle)
# Boat(Vehicle)
# HotAirBalloon(Vehicle)
# -------------
