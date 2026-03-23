from Calculations import CostCalculations

material_cost_per_kg = float(50)
electricity_cost_per_kWH = float(0.30)
calculations_instance = CostCalculations(material_cost_per_kg, electricity_cost_per_kWH)

def get_material_cost () -> float:
    printed_weight = float(43.30)
    additional_materials = float(0.0)
    division_amount = float(1000)

    return calculations_instance.calculate_cost_of_material_used(printed_weight, additional_materials, division_amount)

def get_electricity_cost () -> float:
    print_time = float(6.50)
    printer_wattage = float(350)
    division_amount = float(1000)

    return calculations_instance.calculate_electricity_usage_cost(print_time, printer_wattage, division_amount)

print(f'Total material cost = {get_material_cost()}')

print(f'Total electricity usage cost = {get_electricity_cost()}')

print(f'Total print cost = ${get_material_cost() + get_electricity_cost()}')