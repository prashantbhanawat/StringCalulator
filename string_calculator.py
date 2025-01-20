import logging


class StringCalculator:
    def __init__(self):
        self.delimiter = ','

    def execute(self, numbers: str) -> int:
        parsed_numbers = self._parse_input(numbers)
        result = self._calculate(parsed_numbers)
        return result

    def _parse_input(self, numbers: str) -> list[int]:
        try:
            if self.delimiter in numbers:
                numbers = numbers.split(self.delimiter)
                numbers = [int(num) for num in numbers]
            elif numbers:
                numbers = [int(numbers)]
        except Exception as e:
            logging.info(f"Error in parsing the input: {e}")
            numbers = []
        return numbers

    def _calculate(self, parsed_numbers: list[int]) -> int:
        result = sum(parsed_numbers)
        return result
