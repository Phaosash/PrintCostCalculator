from Calculations import CostCalculations

#   Use this for the total cost of a full spoll or bottle of either filament or resin 
#   (e.g. 1Kg of Elegoo PLA filament in AUD is $50 from Elegoo).
material_cost_per_kg = float(50)

#   This is used to create an instance of the cost calculations class.
calculations_instance = CostCalculations()

#   This function is used to get the total cost of the material used for the printed part
def get_material_cost () -> float:
    printed_weight = float(0.37)
    additional_materials = float(0.0)
    division_amount = float(1000)

    return calculations_instance.calculate_cost_of_material_used(printed_weight, additional_materials, division_amount)

#   This function is used to get the total cost of the electricity useage for the printed part
#   print_time format = hours.minutes (e.g. 1.45 would be 1 hour and 45 minutes).
def get_electricity_cost () -> float:
    print_time = float(1.21)
    printer_wattage = float(350)
    division_amount = float(1000)
    electricity_cost_per_kWH = get_float_input_from_user("Please enter the cost per kWH of print time: ")

    try:
        calculations_instance.set_electrical_cost_per_kWH(electricity_cost_per_kWH)
    except ValueError as e:
        print(f"Could not set electricity cost: {e}")

    return calculations_instance.calculate_electricity_usage_cost(print_time, printer_wattage, division_amount)

def get_float_input_from_user(prompt: str):
    is_valid_prompt = bool(False)
    while not is_valid_prompt:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid Input. Please enter a valid number")


#   Outputs the material cost
print(f'Total material cost = {get_material_cost()}')

#   Outputs the electricity cost
print(f'Total electricity usage cost = {get_electricity_cost()}')

#   Ouputs the entire cost of the print
print(f'Total print cost = ${get_material_cost() + get_electricity_cost()}')