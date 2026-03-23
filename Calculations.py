class CostCalculations:
    #   Default constructor.
    def __init__(self, raw_material_cost_per_unit: float, raw_electricity_cost_per_kWH: float):
        self.material_cost_per_unit = raw_material_cost_per_unit
        self.electricity_cost_per_kWH = raw_electricity_cost_per_kWH

    #   This function is used to calculate the material usage cost of a printed part
    #   estimated_printed_weight_in_grams = the final weight of the printed piece (aka how much it will way)
    #   additional_material_expenses = any additional costs needed for the part (e.g. Hinges, screws)
    def calculate_cost_of_material_used (self, estimated_printed_weight_in_grams: float, additional_material_expenses: float, target_division_amount: float) -> float:
        material_gram_weight = self._divide_value_by_amount(self.material_cost_per_unit, target_division_amount)
        
        total_material_cost = float((material_gram_weight * estimated_printed_weight_in_grams) + additional_material_expenses)

        return float(total_material_cost)
    
    #   This function is used to calculate the electrical usage cost for printing the selected part
    #   part_print_time = how long the printer will take to print the part
    #   printer_power_wattage = the wattage of the printer
    #   target_division_amount = the value needed to complete the division calculation
    def calculate_electricity_usage_cost (self, part_print_time: float, printer_power_wattage: float, target_division_amount: float) -> float:
        converted_power_consumption = self._divide_value_by_amount(printer_power_wattage, target_division_amount)

        total_electricty_cost = float(converted_power_consumption * (self.electricity_cost_per_kWH * part_print_time))
        
        return float(total_electricty_cost)
    
    #   This function is used to calculate and return a float value based on the supplied values.
    def _divide_value_by_amount (self, original_value: float, division_value: float) -> float:
        return float(original_value / division_value)