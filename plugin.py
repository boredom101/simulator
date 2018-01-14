class Plugin:

    def __init__(self, name, resources, commands, properties, parent=None):
        self.resources = resources
        self.commands = commands
        self.name = name
        self.parent = parent
        self.properties = properties

    def __call__(self, args):
        if args[0] in self.commands:
            temp = args[0]
            args.pop(0)
            result = self.commands[temp](self.resources, args, self.properties, self.parent)
            if result == False:
                print("Command " + self.commands[temp].name + " needs to recharge.")
            return True
        else:
            return False