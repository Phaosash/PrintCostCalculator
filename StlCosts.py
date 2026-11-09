class StlCostings:
    #   Default constructor
    def __init__(self):
        self.stl_file_price = float(0.0)
        self.percentage_file_recovery_amount = float(0.0)

    #   This method is used to set the value of the STL file
    def set_stl_value (self, input_amount: float):
        self.stl_file_price = input_amount

    #   This method is used to set and convert the recovery amount to a percentage
    def set_recovery_amount (self, input_amount: float):
        division_amount  = float(100)

        self.percentage_file_recovery_amount = (input_amount / division_amount)

    #   This method is used to get the billable total for the STL file
    def get_stl_total (self) -> float:
        return float(self.stl_file_price * self.percentage_file_recovery_amount)