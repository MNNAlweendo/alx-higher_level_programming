#!/usr/bin/python3
"""Define a function add_attribute."""


def add_attribute(obj, attribute, value):
    """Add a new attribute to obj if possible; otherwise raise TypeError."""
    if hasattr(obj, '__dict__'):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")


if __name__ == "__main__":
    # Example usage
    class Test:
        pass

    obj = Test()
    add_attribute(obj, "name", "John")
    print(obj.name)  # Should print "John"

    add_attribute("string", "name", "John")  # Should raise TypeError

