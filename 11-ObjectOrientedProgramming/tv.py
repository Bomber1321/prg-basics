# tv.py file
# class definition
class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
    def turn_off(self):
        self.is_on = False
    def turn_on (self):
        self.is_on = True
    def show_is_on(self):
        return self.is_on
    def show_channel(self):
        return self.channel_no