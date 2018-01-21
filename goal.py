class Goal:

    def __init__(self, name, log, plugin, test):
        self.name = name
        self.log = log
        self.plugin = plugin
        self.test = test

    def __call__(self):
        if (self.test(self.plugin)):
            return self.log
        else:
            return False