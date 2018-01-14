def generate (resources, args, properties, parent):
    if args[0] in resources:
        resources[args[0]].modify(1)
    else:
        return "nonexistent subatomic particle"

def view (resources, args, properties, parent):
    if (args[0] in resources):
        return str(resources[args[0]].amount)
    else:
        return "nonexistent subatomic particle"