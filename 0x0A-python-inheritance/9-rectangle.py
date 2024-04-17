#!/usr/bin/python3
"""Define a class Rectangle that inherits from BaseGeometry."""


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


class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize private width and height with validation."""
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"


if __name__ == "__main__":
    # Example usage
    try:
        r = Rectangle(3, 5)
        print(r)
        print("Area:", r.area())
    except Exception as e:
        print(e)

    try:
        r1 = Rectangle(4, "5")
    except Exception as e:
        print(e)

    try:
        r2 = Rectangle(-1, 5)
    except Exception as e:
        print(e)

