class ShipingCostings:
    #   Default constructor
    def __init__(self):
        self.cost_of_supplies = float(0.0)
        self.cost_of_labels = float(0.0)

    #   This method is used to set the cost of the supplies like envelopes
    def set_supply_cost (self, input_value: float):
        self.cost_of_supplies = input_value

    #   This method is used to set the cost of the labels
    def set_label_cost (self, input_value: float):
        self.cost_of_labels = input_value

    #   This method is used to get the total cost of shipping the print
    def get_shipping_total (self) -> float:
        return float(self.cost_of_labels + self.cost_of_supplies)