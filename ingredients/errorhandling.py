import urllib.request

try:
    webpage = urllib.request.urlopen("http://www.goooooogle.com")
except:
    print("An error has occured")
else:
    for line in webpage:
        print(line)


class CircuitBreaker:
    def __init__(self, max_amps):
        self.capacity = max_amps  # max capacity in amps
        self.load = 0  # present load in amps

    def connect(self, amps):
        if self.load + amps > self.capacity:
            raise Exception("connect will exceeds capacity")
        elif self.load + amps < 0:
            raise Exception("connect will cause negative load")
        else:
            self.load += amps


# create a 20A circuit breaker
cb = CircuitBreaker(20)

# connect few appliances and print load
cb.connect(12)
cb.connect(7)
print(f"Current load of circuit breaker is {cb.load}")

# connect another appliance which overloads the cb
try:
    cb.connect(10)
except Exception as e:
    print(f"Error: {e}")

# connect another appliance which underloads the cb
try:
    cb.connect(-30)
except Exception as e:
    print(f"Error: {e}")
