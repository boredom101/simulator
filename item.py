class Item:

    # a unique object

    def __init__(self, name, info, subplugin):
        self.name = name
        self.info = info
        self.subplugin = subplugin

    def __call__(self, ref, args):
        if ref == -1:
            self.info[args[0]] = self.subplugin
        elif args[0] in self.info.values()[ref].commands:
            temp = args[0]
            args.pop(0)
            output = self.info.values()[ref].commands[temp](self.info.values()[ref], args, self.info.values()[ref].parent)
            if output == False:
                output = "Command " + self.info.values()[ref].commands[temp].name + " needs to recharge."
            return output
        else:
            return False