import time

class Command:

    # a function accessible to the user, could be getten from a prompt or mapped to a button, for example

    # function : a function that sould take a dictionary containing resources, a list of args, a dictionary of properties,
    #  and a parent plugin, only use if you specifically made the pugin a child.
    # timeout : A wait between allowed runs of function.
    def __init__(self, name, function, timeout=0):
        self.name = name
        self.function = function
        self.timeout = timeout
        self.lastrun = 0

    def __call__(self, resources, args, properties, parent):
        output = ""
        if time.time() > self.lastrun + self.timeout:
            output = self.function(resources, args, properties, parent)
        else:
            output = False
        self.lastrun = time.time()
        return output