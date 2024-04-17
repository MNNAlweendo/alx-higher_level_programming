#!/usr/bin/python3
"""Define a class MyInt that inherits from int."""


class MyInt(int):
    """MyInt class inherits from int and inverts == and != operators."""

    def __eq__(self, other):
        """Invert the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert the != operator."""
        return super().__eq__(other)


if __name__ == "__main__":
    # Example usage
    a = MyInt(4)
    b = MyInt(4)
    c = MyInt(5)

    print(a == b)  # Should print False because of the inverted ==
    print(a != b)  # Should print True because of the inverted !=

    print(a == c)  # Should print True because of the inverted ==
    print(a != c)  # Should print False because of the inverted !=

