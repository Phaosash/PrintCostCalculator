from Calculations import CostCalculations

#   Use this for the total cost of a full spoll or bottle of either filament or resin 
#   (e.g. 1Kg of Elegoo PLA filament in AUD is $50 from Elegoo).
material_cost_per_kg = float(50)

#   This should be used to help offset the cost of printing the part if its later sold.
electricity_cost_per_kWH = float(0.30)

#   This is used to create an instance of the cost calculations class.
calculations_instance = CostCalculations(material_cost_per_kg, electricity_cost_per_kWH)

#   This function is used to get the total cost of the material used for the printed part
def get_material_cost () -> float:
    printed_weight = float(67.44)
    additional_materials = float(0.0)
    division_amount = float(1000)

    return calculations_instance.calculate_cost_of_material_used(printed_weight, additional_materials, division_amount)

#   This function is used to get the total cost of the electricity useage for the printed part
#   print_time format = hours.minutes (e.g. 1.45 would be 1 hour and 45 minutes).
def get_electricity_cost () -> float:
    print_time = float(1.21)
    printer_wattage = float(350)
    division_amount = float(1000)

    return calculations_instance.calculate_electricity_usage_cost(print_time, printer_wattage, division_amount)

#   Outputs the material cost
print(f'Total material cost = {get_material_cost()}')

#   Outputs the electricity cost
print(f'Total electricity usage cost = {get_electricity_cost()}')

#   Ouputs the entire cost of the print
print(f'Total print cost = ${get_material_cost() + get_electricity_cost()}')