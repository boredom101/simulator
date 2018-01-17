class Plugin:

    # a group of commands, resources, and properties that all work together.

    # name : used by simsys for commands
    # resources, commands, properties and items : dictionaries of said objects
    # parent : Another plugin that this plugin can access

    def __init__(self, name, resources, commands, properties, items, parent=None):
        self.resources = resources
        self.commands = commands
        self.name = name
        self.parent = parent
        self.properties = properties
        self.items = items

    def __call__(self, args):
        if args[0] in self.commands:
            temp = args[0]
            args.pop(0)
            output = self.commands[temp](self, args, self.parent)
            if output == False:
                output = "Command " + self.commands[temp].name + " needs to recharge."
            return output
        else:
            return False