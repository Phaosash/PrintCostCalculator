class PrintCostings:
    #   Default constructor
    def __init__(self):
        self.profit_markup_percentage = float(0.0)
        self.total_expenses = float(0.0)
        self.project_costings_subtotal = float(0.0)
        self.gst_amount = float(0.0)
        self.total_sale_price = float(0.0)

    #   This method is used to set the total vost of the projects expenses
    def set_project_expenses (self, material_costs: float, electricity_costs: float, labour_costs: float, shipping_costs: float, stl_costs: float, machine_costs: float, print_protection: float):
        self.total_expenses = float(material_costs + electricity_costs + labour_costs + shipping_costs + stl_costs + machine_costs + print_protection)

    #   This method is used to set the markup value as a percentage
    def set_markup_percentage (self, inputed_value: float):
        division_amount = float(100)

        self.profit_markup_percentage = (inputed_value / division_amount)

    #   This method is used to get the total figure of the markup amount
    def __get_project_markup_total (self) -> float:
        return float(self.total_expenses * self.profit_markup_percentage)

    #   This method is used to get the net subtotal for the project
    def __get_project_net_value (self) -> float:
        return float(self.__get_project_markup_total + self.total_expenses)

    #   This method is used to calculate the amount of gst to be added to the invoice
    def get_gst_amount (self):
        self.gst_amount =  float(self.__get_project_net_value * self.gst_amount)

    #   This method is used to get the total cost of the project
    def get_print_cost_total (self) -> float:
        return float(self.gst_amount + self.__get_project_net_value)