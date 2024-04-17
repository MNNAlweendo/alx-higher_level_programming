#!/usr/bin/python3
"""Define a class BaseGeometry with area and integer_validator methods."""


class BaseGeometry:
    """Base class for geometry methods and attributes."""

    def area(self):
        """Raise an exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value as an integer and check if it's greater than 0."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


if __name__ == "__main__":
    # Example usage
    bg = BaseGeometry()

    try:
        bg.area()
    except Exception as e:
        print(e)

    try:
        bg.integer_validator("width", 10)
        bg.integer_validator("height", 0)
    except Exception as e:
        print(e)

