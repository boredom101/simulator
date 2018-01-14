import time

class Command:

    def __init__(self, name, function, timeout=0):
        self.name = name
        self.function = function
        self.timeout = timeout
        self.lastrun = 0

    def __call__(self, resources, args, properties, parent):
        flag = True
        if time.time() > self.lastrun + self.timeout:
            self.function(resources, args, properties, parent)
        else:
            flag = False
        self.lastrun = time.time()
        return flag