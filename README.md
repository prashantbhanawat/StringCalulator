This project implements a simple string calculator in Python, designed to parse a given string of numbers and return their sum based on specific requirements and extensions to the basic functionality.

## Method Signature
```python
int Add(string numbers)
```

## Features

1. **Simple Addition**
    - The method can take up to two numbers, separated by commas, and will return their sum.
    - Examples:
      - `""` should return `0`
      - `"1"` should return `1`
      - `"1,2"` should return `3`

2. **Handling Multiple Numbers**
    - The `Add` method can handle an unknown number of numbers.

3. **Handling New Lines**
    - The method can handle new lines between numbers as valid separators, along with commas.
    - Example:
      - `"1\n2,3"` should return `6`

4. **Support for Different Delimiters**
    - To change a delimiter, the format at the beginning of the string will be `//[delimiter]\n`.
    - Example:
      - `"//;\n1;2"` should return `3`
    - This line is optional, and all existing scenarios should still be supported.

5. **Negative Number Exception**
    - Calling `Add` with a negative number will throw an exception `negatives not allowed` with the negative numbers that were passed.
    - Example: `"1,-2,-3"` will result in exception "negatives not allowed: -2, -3"

6. **Ignoring Large Numbers**
    - Numbers larger than `1000` should be ignored in computations.
    - Example: `"2,1001"` should return `2`

7. **Custom Delimiter Length**
    - Delimiters can be of any length.
    - Example: `"//[***]\n1***2***3"` should return `6`

8. **Multiple Delimiters**
    - Multiple delimiters can be specified like this: `"//[delim1][delim2]\n"`
    - Example: `"//[*][%]\n1*2%3"` should return `6`

9. **Complex Delimiters**
    - Support multiple delimiters of variable lengths.
    - Example: `"//[***][#][%]\n1***2#3%4"` should return `10`

## How to Use

1. **Installation**
    - Ensure Python is installed and set up on your machine.

2. **Running Tests**
    - Write and run tests for each of the features above. Consider using a testing framework like `unittest`.

3. **Example Usage**
    - Example call to the `Add` method:
      ```python
      result = Add("1,2")
      print(result)  # Output: 3
      ```

## Future Enhancements

- Further validation may be added to support additional functionalities.
- Improved error handling and user feedback.
