import pytest

from string_calculator import StringCalculator


def test_string_calculator():
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

    # Test new line delimiter
    assert calculator.execute("1\n2,3") == 6

    # Test new line delimiter with multiple numbers
    assert calculator.execute("1\n2\n3,4\n5") == 15

    # Test custom delimiter
    assert calculator.execute("//;\n1;2") == 3

    # Test custom delimiter with multiple numbers
    assert calculator.execute("//;\n1;2;3;4") == 10

    # Test Negative numbers
    with pytest.raises(ValueError):
        calculator.execute("-1,2,3")

    # Test Negative numbers
    with pytest.raises(ValueError):
        calculator.execute("-1\n2,-3")


if __name__ == "__main__":
    pytest.main()
