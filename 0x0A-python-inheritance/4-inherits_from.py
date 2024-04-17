#!/usr/bin/python3
"""Check if an object is an instance of a subclass of the specified class."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class; otherwise False."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class


if __name__ == "__main__":
    # Example usage
    class MyClass:
        pass

    class MyDerivedClass(MyClass):
        pass

    class MySecondDerivedClass(MyDerivedClass):
        pass

    obj1 = MyDerivedClass()
    obj2 = MySecondDerivedClass()
    obj3 = MyClass()
    obj4 = "Hello"
    obj5 = 123

    print(inherits_from(obj1, MyClass))            # Should print True
    print(inherits_from(obj2, MyClass))            # Should print True
    print(inherits_from(obj2, MyDerivedClass))     # Should print True
    print(inherits_from(obj3, MyClass))            # Should print False
    print(inherits_from(obj4, MyClass))            # Should print False
    print(inherits_from(obj5, MyClass))            # Should print False

