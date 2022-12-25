# Define a minimal class with an attribute

class MyClass:
    """
    A minimal example class
    :param value: value to set as the ``attribute`` attribute
    :ivar attribute: contains the contents of ``value`` passed in init
    """

    # Method to create a new instance of MyClass
    def __init__(self, value):
        # Define attribute with the contents of the value param
        self.attribute = value


class Parent:
    def __init__(self):
        print("I'm a parent class!")


class SuperChild(Parent):
    def __init__(self):
        super().__init__()
        print("I'm a super child!")


class GrandChild(SuperChild):
    def __init__(self):
        super().__init__()
        print("I'm a grandchild!")


if __name__ == '__main__':
    grandchild = GrandChild()
