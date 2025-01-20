import logging


class StringCalculator:
    def __init__(self):
        self.delimiter = ','
        self.allowed_delimiters = [',', '\n']

    def execute(self, numbers: str) -> int:
        parsed_numbers = self._parse_input(numbers)
        result = self._calculate(parsed_numbers)
        return result

    def _parse_input(self, numbers: str) -> list[int]:
        modified_numbers = self._replace_delimiter(numbers)
        try:
            if self.delimiter in modified_numbers:
                modified_numbers = modified_numbers.split(self.delimiter)
                modified_numbers = [int(num) for num in modified_numbers]
            elif modified_numbers:
                modified_numbers = [int(modified_numbers)]
        except Exception as e:
            logging.info(f"Error in parsing the input: {e}")
            modified_numbers = []
        return modified_numbers

    def _replace_delimiter(self, numbers: str) -> str:
        for delimiter in self.allowed_delimiters:
            numbers = numbers.replace(delimiter, self.delimiter)
        return numbers

    def _calculate(self, parsed_numbers: list[int]) -> int:
        result = sum(parsed_numbers)
        return result
