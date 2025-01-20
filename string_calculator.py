import logging

import re
import traceback


class StringCalculator:
    def __init__(self):
        self.default_delimiter = ','
        self.allowed_delimiters = [',', '\n']

    def execute(self, numbers: str) -> int:
        parsed_numbers = self._parse_input(numbers)
        self._check_negatives(parsed_numbers)
        parsed_numbers = self._remove_numbers_greater_than_1000(parsed_numbers)
        result = self._calculate(parsed_numbers)
        return result

    def _parse_input(self, numbers: str) -> list[int]:
        try:
            modified_numbers = self._replace_delimiter(numbers)
            if self.default_delimiter in modified_numbers:
                modified_numbers = modified_numbers.split(self.default_delimiter)
                modified_numbers = [int(num) for num in modified_numbers]
            elif modified_numbers:
                modified_numbers = [int(modified_numbers)]
        except Exception as e:
            logging.error(f"Invalid Input, Error in parsing the input: {e}")
            traceback.print_exc()
            modified_numbers = []
        return modified_numbers

    def _replace_delimiter(self, numbers: str) -> str:
        match = re.match(r'//\[(.*?)]\n', numbers)
        if match:
            delimiter = match.group(1)
            self.allowed_delimiters.append(delimiter)
            numbers = numbers[match.end():]

        elif numbers.startswith('//'):
            self.allowed_delimiters.append(numbers[2])
            numbers = numbers.split('\n')[1]
        for delimiter in self.allowed_delimiters:
            numbers = numbers.replace(delimiter, self.default_delimiter)

        return numbers

    def _check_negatives(self, parsed_numbers: list[int]):
        negatives = [num for num in parsed_numbers if num < 0]
        if negatives:
            raise ValueError(f"Negatives not allowed: {negatives}")

    def _remove_numbers_greater_than_1000(self, parsed_numbers: list[int]) -> list[int]:
        parsed_numbers = [num for num in parsed_numbers if num <= 1000]
        return parsed_numbers

    def _calculate(self, parsed_numbers: list[int]) -> int:
        result = sum(parsed_numbers)
        return result
