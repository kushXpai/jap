from functools import reduce
from typing import Optional

numbers = [1, 2, 3, 4, 5, 6]

# Filter: Get only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)

# Map: Square each even number
squared_evens = list(map(lambda x: x ** 2, even_numbers))
print("Squared Even Numbers:", squared_evens)

# Reduce: Sum of squared even numbers
sum_of_squares: Optional[int] = reduce(lambda x, y: x + y, squared_evens) if squared_evens else None

# Optional Handling
if sum_of_squares is not None:
    print("Sum of Squared Even Numbers:", sum_of_squares)
else:
    print("No even numbers to process.")

# Demonstrate use of Optional in function return
def get_first_even(nums: list[int]) -> Optional[int]:
    """Return the first even number from the list, if any."""
    evens = list(filter(lambda x: x % 2 == 0, nums))
    return evens[0] if evens else None

first_even = get_first_even(numbers)
print("First Even Number:", first_even if first_even is not None else "No even number found.")
