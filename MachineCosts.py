class MachineCostings:
    #   Default constructor
    def __init__(self):
        self.printer_purchase_price = float(0.0)
        self.extimated_printer_print_lifetime = float(0.0)

    #   This method is used to set the value of the printer purchase price
    def set_printer_purchase_price (self, input_value: float):
        self.printer_purchase_price = input_value

    #   This method is used to set the estimated number of hours the printer can print for
    def set_print_time_lifetime (self, input_value: float):
        self.extimated_printer_print_lifetime = input_value

    #   This method is used to get the total machine maintenance costing
    def get_maintenance_total (self) -> float:
        return float(self.printer_purchase_price * self.extimated_printer_print_lifetime)