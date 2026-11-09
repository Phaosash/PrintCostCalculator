class PrintFailureProtectionCostings:
    #   Default constructor
    def __init__(self):
        self.print_failure_cost = float(0.0)
        self.offset_percentage_amount = float(0.0)

    #   This method is used to set the cost of a print failure
    def set_print_failure_cost (self, labour_cost: float, electricity_cost: float, material_cost: float):
        self.print_failure_cost = (labour_cost + electricity_cost + material_cost)

    #   This method is used to set the offset amount as a percentage
    def set_print_failure_offset_percentage (self, input_value: float):
        division_amount = float(100)

        self.offset_percentage_amount = (input_value / division_amount)

    #   This method is used to get the total value of the print failure protection
    def get_print_failure_protection_value (self) -> float:
        return float(self.print_failure_cost * self.offset_percentage_amount)