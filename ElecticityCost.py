class ElectricityCosts:
    #   Default constructor
    def __init__(self):
        self.print_time_in_hours = float(0.0)
        self.cost_per_kWH = float(0.0)
        self.printer_wattage = float(0.0)

    #   This method is used to set the print time
    def set_print_time (self, inputed_value: float):
        self.print_time_in_hours = inputed_value

    #   This method is used to set the energy cost per kWH
    def set_energy_cost (self, inputed_value: float):
        self.cost_per_kWH = inputed_value

    #   This method is used to set the wattage of the printer
    def set_printer_wattage (self, inputed_value: float):
        self.printer_wattage = inputed_value

    #   This method is sued to get the total cost of the energy usage for the print
    def get_total_energy_cost (self) -> float:
        watt_to_kWH = float(1000)

        total_energy_cost = float((self.printer_wattage / watt_to_kWH) * (self.cost_per_kWH * self.print_time_in_hours))

        return float(total_energy_cost)