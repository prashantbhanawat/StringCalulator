import pytest

from string_calculator import StringCalculator


def string_calculator():
    # Create a calculator object
    calculator = StringCalculator()

    # Test empty string
    assert calculator.execute("") == 0

    # Test single number
    assert calculator.execute("1") == 1

    # Test two numbers
    assert calculator.execute("2,3") == 5

    # Test multiple numbers
    assert calculator.execute("6,9,12") == 27


if __name__ == "__main__":
    pytest.main()
