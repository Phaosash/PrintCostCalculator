from MaterialCost import MaterialCosts
from ElecticityCost import ElectricityCosts

material_cost_instance = MaterialCosts()
electricity_cost_instance = ElectricityCosts()

#   This method is used to generate the total cost of the materials for the print
def generate_material_cost () -> float:    
    material_cost_instance.set_material_cost(get_float_input_from_user("Please enter the cost per kg for the material: "))
    material_cost_instance.set_estimated_weight(get_float_input_from_user("Please enter the estimated weigh of the final print: "))
    material_cost_instance.set_additional_expenses(get_float_input_from_user("Please enter the value for an extra expenses like screws, if none enter 0: "))

    return float(material_cost_instance.get_total_material_cost())

#   This method is used to generate the cost of electricity usage for the print
def generate_electricity_cost () -> float:
    electricity_cost_instance.set_print_time(get_float_input_from_user("Please enter the estimated print time. e.g 6.5 is 6 hrs and 50 minutes: "))
    electricity_cost_instance.set_energy_cost(get_float_input_from_user("Please enter your cost per kWH for each hour of print time. e.g 0.30 is 30 cents per hours: "))
    electricity_cost_instance.set_printer_wattage(get_float_input_from_user("Please enter the power wattage of your printer: "))

    return float(electricity_cost_instance.get_total_energy_cost())

#   This method is used to get a float input from the user
def get_float_input_from_user (prompt: str):
    is_valid_prompt = bool(False)
    while not is_valid_prompt:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid Input. Please enter a valid number")

#   Outputs the material cost
print(f'Total material cost = {generate_material_cost()}')

#   Outputs the enegy usage cost
print(f"Total Electricity Cost = {generate_electricity_cost()}")