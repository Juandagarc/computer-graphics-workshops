class Distance:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def convert(self):
        if self.unit == 'km/h':
            self.unit = 'm/s'
            self.value = self.value / 3.6
        else:
            self.unit = 'm/s'
            self.value = self.value * 3.6
        print('the converted value is: ' + str(self.value) + ' ' + str(self.unit))