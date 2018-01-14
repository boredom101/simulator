def generate (resources, args, properties, parent):
    if args[0] in resources:
        resources[args[0]].modify(1)
    else:
        print("nonexistent subatomic particle")

def view (resources, args, properties, parent):
    if (args[0] in resources):
        print(str(resources[args[0]].amount))
    else:
        print("nonexistent subatomic particle")