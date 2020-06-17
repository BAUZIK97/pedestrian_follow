class CServo:
    def __init__(self, ms, tolerance):
        self.ms = ms
        self.tolerance = tolerance

    def ch_tolerance(self, newtolerance):
        self.tolerance = newtolerance

    def add_ms(self, ms_diff):
        self.ms = self.ms + ms_diff

    def sub_ms(self, ms_diff):
        self.ms = self.ms - ms_diff

    def ch_ms(self, new_ms):
        self.ms = new_ms
