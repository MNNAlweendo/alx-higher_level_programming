#!/usr/bin/python3
"""Return the list of available attributes and methods of an object."""


def lookup(obj):
    """Return a list of available attributes and methods of an object."""
    return dir(obj)


if __name__ == "__main__":
    class MyClass:
        def __init__(self):
            self.attribute1 = "value1"
        
        def method1(self):
            pass

    obj = MyClass()
    print(lookup(obj))

