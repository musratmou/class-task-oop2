class Vehicle:
    def __init__(self, color):
        self.color = color

    def vehicle_info(self):
        print(f"Vehicle Color: {self.color}")


class Car(Vehicle):
    def __init__(self, color, model, capacity, variant):
        super().__init__(color)
        self.__model = model         # Private attribute
        self.__capacity = capacity   # Private attribute
        self.__variant = variant     # Private attribute

    def get_model(self):
        return self.__model

    def get_capacity(self):
        return self.__capacity

    def get_variant(self):
        return self.__variant

    def set_model(self, model):
        self.__model = model

    def set_capacity(self, capacity):
        self.__capacity = capacity

    def set_variant(self, variant):
        self.__variant = variant

    def vehicle_info(self):
        super().vehicle_info()
        print(f"Model: {self.__model}")
        print(f"Capacity: {self.__capacity}")
        print(f"Variant: {self.__variant}")



t1 = Car("Red", "Model X", 5, "Electric")
t2 = Car("Blue", "Model S", 4, "Hybrid")


print("Details of t1:")
t1.vehicle_info()


print("\nDetails of t2:")
t2.vehicle_info()


t1.set_model("Model Y")
t1.set_capacity(7)
t1.set_variant("Electric Plus")

print("\nUpdated details of t1:")
t1.vehicle_info()
