class LabourCostings:
    #   Default constructor
    def __init__(self):
        self.hourly_rate = float(0.0)
        self.preperation_time_per_object = float(0.0)

    #   This method is used to set the user hourly rate
    def set_hourly_rate (self, input_value: float):
        self.hourly_rate = input_value

    #   This method is used to set the amount of prep time per object
    def set_preperation_time (self, input_value: float):
        self.preperation_time_per_object = input_value

    #   This method is used to get the total labour cost
    def get_labour_cost (self) -> float:
        minutes_per_hour = float(60)
        
        return float((self.hourly_rate / minutes_per_hour) * self.preperation_time_per_object)