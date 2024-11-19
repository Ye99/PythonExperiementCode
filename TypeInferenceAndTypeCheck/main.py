# Create and activate a virtual environment, then pip install mypy
# mypy main.py

def apply_operation(numbers: list[int], operation: callable) -> list[int]:
    """
    Applies a given operation to each number in a list.

    Args:
        numbers: A list of integers to process.
        operation: A function that takes an integer and returns an integer.

    Returns:
        A list of integers after applying the operation.
    """
    if not operation:
        raise ValueError("operation must not be None")
    return [operation(num) for num in numbers]


# Define some operations
def square(x: int) -> int:
    return x * x


def double(x: int) -> int:
    return x * 2


# Example usage
nums = [1, 2, 3, 4, 5]

# Pass the function reference as a parameter, None can be passed as parameter.
# squared_nums = apply_operation(nums, None)
# print(f"Squared: {squared_nums}")  # Output: Squared: [1, 4, 9, 16, 25]

doubled_nums = apply_operation(nums, double)
print(f"Doubled: {doubled_nums}")  # Output: Doubled: [2, 4, 6, 8, 10]

'''
Test 2: type inference and mypy type check 
'''
from typing import Literal, Optional


def process_input_caller(mode: Optional[Literal["all", "any", "mean", "min", "max"]]) -> None:
    print(f"process_input_caller, mode is {mode}.")
    #  Argument 1 to "process_input" has incompatible type "Literal['all', 'any', 'mean', 'min', 'max'] | None";
    #  expected "Literal['all', 'any', 'mean', 'min', 'max']"
    process_input(mode)

def process_input(mode: Literal["all", "any", "mean", "min", "max"]) -> None:
    print(f"process_input mode is {mode}")


#process_input_caller(None)
#process_input_caller("average")

class ExampleClass:
    def __init__(
            self,
            aggregate_same_input: Optional[Literal["all", "any", "mean", "min", "max"]] = None,
    ):
        """
        Initialize the ExampleClass.

        Args:
            aggregate_same_input: A method to aggregate the same input. Must be one of
                                  'all', 'any', 'mean', 'min', 'max', or None.
        """
        # aggregate_same_input inherits aggregate_same_input's type
        self.aggregate_same_input = aggregate_same_input
        process_input_caller(self.aggregate_same_input)

    def __repr__(self)->str:
        # __init__ is called before __repr__
        return f"ExampleClass(aggregate_same_input={self.aggregate_same_input})"


# Example usage
example1 = ExampleClass(aggregate_same_input="mean")
print(example1)

example2 = ExampleClass()  # Defaults to None
print(example2)
