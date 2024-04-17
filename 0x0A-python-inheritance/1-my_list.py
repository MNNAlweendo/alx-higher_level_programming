#!/usr/bin/python3
"""Define a class MyList that inherits from list."""


class MyList(list):
    """Inherits from list and provides additional methods."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)


if __name__ == "__main__":
    # Example usage
    my_list = MyList([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    my_list.print_sorted()  # Should print [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

