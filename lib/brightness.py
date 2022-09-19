import os

class Brightness:
    def __init__(self):
        self.path = "/sys/class/backlight/pwm-backlight"
        self.max_brightness_f = os.path.join(self.path, "max_brightness")
        self.actual_brightness_f = os.path.join(self.path, "actual_brightness")
        self.brightness_f = os.path.join(self.path, "brightness")
        self.init_max_brightness()

    def get_actual_brightness(self):
        with open(self.actual_brightness_f, 'r') as f:
            return f.read()

    def set_brightness(self, brightness):
        _b = int(brightness)
        if _b < 1:
            _b = 1
        if _b > self.max_brightness:
            _b = self.max_brightness
        brightness = str(_b)
        with open(self.brightness_f, 'w') as f:
            return f.write(brightness)

    def init_max_brightness(self):
        with open(self.max_brightness_f, 'r') as f:
            self.max_brightness = int(f.read())
