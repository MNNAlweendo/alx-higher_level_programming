#!/usr/bin/python3
"""Define a class BaseGeometry with an area method."""


class BaseGeometry:
    """Base class for geometry methods and attributes."""

    def area(self):
        """Raise an exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")


if __name__ == "__main__":
    # Example usage
    bg = BaseGeometry()
    try:
        bg.area()
    except Exception as e:
        print(e)

