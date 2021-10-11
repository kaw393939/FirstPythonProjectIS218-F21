"""A simple calc_mod module"""
class Simple:
    """A simple calc_mod class"""
    result = 0
    def __init__(self):
        pass
    def add(self, value_one, value_two):
        """Adds Two Numbers"""
        self.result = value_one + value_two
        return self.result
    def subtract(self, value_one, value_two):
        """Subtract Two Numbers"""
        self.result = value_one - value_two
        return self.result
