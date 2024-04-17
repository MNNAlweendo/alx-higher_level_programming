#!/usr/bin/python3
"""Check if an object is an instance of, or inherited from, the specified class."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of, or inherited from, a_class; otherwise False."""
    return isinstance(obj, a_class)


if __name__ == "__main__":
    # Example usage
    class MyClass:
        pass

    class MyDerivedClass(MyClass):
        pass

    obj1 = MyClass()
    obj2 = MyDerivedClass()
    obj3 = "Hello"
    obj4 = 123

    print(is_kind_of_class(obj1, MyClass))       # Should print True
    print(is_kind_of_class(obj2, MyClass))       # Should print True
    print(is_kind_of_class(obj2, MyDerivedClass))# Should print True
    print(is_kind_of_class(obj3, MyClass))       # Should print False
    print(is_kind_of_class(obj4, MyClass))       # Should print False

