class Vehicle:
    def __init__(self, make, model, mileage):
        if mileage < 0:
            raise ValueError("mileage must be non-negative")
        self.make = make
        self.model = model
        self.mileage = mileage

    def __str__(self):
        return f"{self.make} {self.model} | Mileage: {self.mileage}"


if __name__ == "__main__":
    v1 = Vehicle("Toyota", "Camry", 120000)
    v2 = Vehicle("Ford", "F-150", 45000)
    print(v1)
    print(v2)
