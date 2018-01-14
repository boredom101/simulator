class Simsys:

    def __init__(self, name, functions, plugins, prompt=[" ","printer",">"]):
        self.name = name
        self.functions = functions
        if prompt[0] == " ":
            prompt[0] = name
        self.prompt = prompt
        self.plugins = plugins

    def __call__(self, args=[]):
        if len(args) == 0:
            self.functions["exec"](self, self.prompt)
            result = self.functions["input"](">")
            args = result.split
        if args[0] == self.name:
            if args[1] in self.functions:
                args.pop(0)
                self.functions[args[0]](self, args)
            else:
                self.functions["printer"]("Command not found")
        elif args[0] in self.plugins:
            temp = args[0]
            args.pop(0)
            flag = self.plugins[temp](args)
            if flag == False:
                self.functions["printer"]("Command not found")
        else:
            self.functions["printer"]("Huh?")