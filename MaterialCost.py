class MaterialCosts:
    #   Default constuctor
    def __init__(self):
        self.material_cost_per_unit = float(0.0)
        self.estimated_weight_in_grams = float(0.0)
        self.additional_expenses = float(0.0)

    #   This method is used to set the raw cost of materials per kg
    def set_material_cost (self, inputed_value: float):
        self.material_cost_per_unit = inputed_value

    #   This method is used to set the estimated weight of the print
    def set_estimated_weight (self, inputed_value: float):
        self.estimated_weight_in_grams = inputed_value

    #   This method is used to set the value of any additional expenses like screws
    def set_additional_expenses (self, inputed_value: float):
        self.additional_expenses = inputed_value

    #   This method is used to get the combined total material cost for the print
    def get_total_material_cost (self) -> float:
        grams_per_kg = float(1000)

        total_material_cost = float(((self.material_cost_per_unit / grams_per_kg) * self.estimated_weight_in_grams) + self.additional_expenses)

        return float(total_material_cost)