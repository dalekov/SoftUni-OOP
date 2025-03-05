import math

class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(math.floor(float_value))

    @classmethod
    def from_roman(cls, value):
        roman_numerals = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        total = 0
        previous_value = 0
        for ch in reversed(value):
            current_value = roman_numerals.get(ch, 0)
            if current_value >= previous_value:
                total += current_value
            else:
                total -= current_value
            previous_value = current_value

        return cls(total)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"
        return cls(int(value))
