import math

class CostCalculations:
    #   Default constructor.
    def __init__(self):
        self.material_cost_per_unit = float(0.0)
        self.electricity_cost_per_kWH = float(0.0)

    #   This method is used to divide two values
    def calculate_percentage_amount (self, initial_value: float, division_value: float) -> float:
        return (initial_value / division_value)

    #   This method is used to multiply two values together
    def multiply_two_floats (self, value_a: float, value_b: float) -> float:
        return float(value_a * value_b)