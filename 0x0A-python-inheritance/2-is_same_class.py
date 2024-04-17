#!/usr/bin/python3
"""Check if an object is exactly an instance of the specified class."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class; otherwise False."""
    return type(obj) is a_class


if __name__ == "__main__":
    # Example usage
    class MyClass:
        pass

    obj1 = MyClass()
    obj2 = "Hello"
    obj3 = 123

    print(is_same_class(obj1, MyClass))  # Should print True
    print(is_same_class(obj2, MyClass))  # Should print False
    print(is_same_class(obj3, MyClass))  # Should print False

