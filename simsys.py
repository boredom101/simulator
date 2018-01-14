class Simsys:

    def __init__(self, name, functions, plugins, prompt):
        self.name = name
        self.functions = functions
        self.prompt = prompt
        if self.prompt[0] == " ":
            self.prompt[0] = name
        self.plugins = plugins

    def __call__(self, args=[]):
        output = ""
        arguements = args
        if len(arguements) == 0:
            result = self.functions["input"](self, self.functions["exec"](self, self.prompt))
            arguements = result.split()
        if arguements[0] == self.name:
            if arguements[1] in self.functions:
                output = self.functions[arguements[1]](self, arguements[2:])
            else:
                output = "Command not found"
        elif arguements[0] in self.plugins:
            temp = arguements[0]
            output = self.plugins[temp](arguements[1:])
            if output == False:
                output = "Command not found"
        else:
            output = "Plugin not found"
        return output