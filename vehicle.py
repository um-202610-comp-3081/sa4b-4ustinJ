class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"{self.make} {self.model}"


if __name__ == "__main__":
    v1 = Vehicle("Toyota", "Camry")
    v2 = Vehicle("Ford", "F-150")
    print(v1)
    print(v2)
