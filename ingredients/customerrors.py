class ElectricalError(Exception):
    def __init__(self, device, problem):
        self.device = device
        self.problem = problem

    def __str__(self):
        return f"The {self.device} is {self.problem}"


class PlumbingError(Exception):
    def __init__(self, device, problem):
        self.device = device
        self.problem = problem

    def __str__(self):
        return f"The {self.device} is {self.problem}"


def cause_error(error_type):
    if error_type == "electrical":
        raise ElectricalError("light", "fading")
    elif error_type == "plumbing":
        raise PlumbingError("pipe", "clogged")
    else:
        raise Exception("Generic household problem")


try:
    cause_error("electrical")
except ElectricalError as e:
    print(f"{e}. Fix it yourself")

try:
    cause_error("plumbing")
except PlumbingError as e:
    print(f"{e}. Call a plumber.")

try:
    cause_error("gas")
except Exception as e:
    print(f"{e}. Call the landlord")
