class Simsys:

    #system object used by frontend

    # name = what simsys is referred to as in commands
    # functions = dictionary of functions used by simsys to run according to your desired configuration
    #             all take the simsys object and another variable as arguements
    #  exec : runs the list of arguments as a command, should return output of command
    #  input : prompts user for input, could use args as prompt text, should return user input as string
    #  exit : should at least exit the session
    # plugins = a dictionary of plugins used by this configuration, keys are names used by commands
    # prompt = list of args ran before input is ran
    def __init__(self, name, functions, plugins, prompt):
        self.name = name
        self.functions = functions
        self.prompt = prompt
        if self.prompt[0] == " ":
            self.prompt[0] = name
        self.plugins = plugins

    def __call__(self, args=[]):
        output = ""
        arguments = args
        if len(arguments) == 0: # not a call for prompt or the such, so it needs to ask user for arguments
            result = self.functions["input"](self, self.functions["exec"](self, self.prompt))
            arguments = result.split()
        if arguments[0] == self.name: # check if command is to a system function
            if arguments[1] in self.functions:
                output = self.functions[arguments[1]](self, arguments[2:])
            else:
                output = "Command not found"
        elif arguments[0] in self.plugins: # check if plugin command
            temp = arguments[0]
            output = self.plugins[temp](arguments[1:])
            if output == False:
                output = "Command not found"
        else:
            output = "Plugin not found"
        return output
