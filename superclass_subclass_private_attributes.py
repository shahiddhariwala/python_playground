class Superclass:
    def __init__(self):
        self.__private_attribute = 42

    def __private_method(self):
        print("This is a private method.")


class Subclass(Superclass):
    def access_private_attribute(self):
        print("Accessing private attribute:", self._Superclass__private_attribute)

    def call_private_method(self):
        self._Superclass__private_method()


# Create an instance of Subclass
obj = Subclass()

# Access private attribute through a method in the subclass
obj.access_private_attribute()  # Output: Accessing private attribute: 42

# Call private method in the subclass
obj.call_private_method()  # Output: This is a private method.

# Attempt to access private attribute directly in the subclass
# print(obj.__private_attribute)  # This will raise an AttributeError
