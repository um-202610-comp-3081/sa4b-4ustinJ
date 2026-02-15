class Vehicle:
    def __init__(self, make, model, availability):
        self.make = make
        self.model = model
        self.availability = availability

    def __str__(self):
        return f"{self.make} {self.model} | Status: {self.availability}"


if __name__ == "__main__":
    v1 = Vehicle("Toyota", "Camry", "Available")
    v2 = Vehicle("Ford", "F-150", "In Maintenance")
    print(v1)
    print(v2)
