class Vehicle:
    def __init__(self, make, model, mileage, availability):
        if mileage < 0:
            raise ValueError("mileage must be non-negative")
        self.make = make
        self.model = model
        self.mileage = mileage
        self.availability = availability

    def __str__(self):
        return f"{self.make} {self.model} | Mileage: {self.mileage} | Status: {self.availability}"


if __name__ == "__main__":
    v1 = Vehicle("Toyota", "Camry", 120000, "Available")
    v2 = Vehicle("Ford", "F-150", 45000, "In Maintenance")
    print(v1)
    print(v2)
