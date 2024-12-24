class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_detail(self):
        print(f"Product Name: {self.name}")
        print(f"Product Price: {self.price}")


class ElectricProduct(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

    def display_detail(self):
        super().display_detail()
        print(f"Product Warranty: {self.warranty} years")

electric_product = ElectricProduct("Washing Machine", 500, 2)
electric_product.display_detail()

class Shape:
    def __init__(self, name):
        self._name = name 

    def get_name(self):
        return self._name

    def __display_info(self):
        print(f"Shape Name: {self._name}")

    def display_info(self):
        self.__display_info()



shape = Shape("Circle")
print(shape.get_name()) 
shape.display_info()    

class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.__length = length  
        self.__width = width    

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)

    def display_info(self):
        super().display_info()
        print(f"Length: {self.__length}")
        print(f"Width: {self.__width}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")



rectangle = Rectangle("Rectangle", 10, 5)
rectangle.display_info()