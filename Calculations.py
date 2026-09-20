import math

class CostCalculations:
    #   Default constructor.
    def __init__(self):
        self.material_cost_per_unit = float(0.0)
        self.electricity_cost_per_kWH = float(0.0)

    #   This function is used to set the value for the electrical usage cost.
    def set_electrical_cost_per_kWH (self, kwh_amount: float):
        if kwh_amount is None:
            raise ValueError("Electricity cost cannot be None.")

        if math.isnan(kwh_amount) or kwh_amount <= 0:
            raise ValueError("Electricity cost must be greater than zero.")

        self.electricity_cost_per_kwh = kwh_amount

    #   This function is used to set the value for the material unit cost.
    def set_material_cost_per_unit (self, material_cost: float):
        if material_cost is None:
            raise ValueError("Material cost cannot be None.")

        if math.isnan(material_cost) or material_cost <=0:
            raise ValueError("Material cost must be greater than zero.")

        self.material_cost_per_unit = material_cost

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