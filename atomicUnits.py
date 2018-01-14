def view (resources, args, properties, parent):
    if len(args) == 0:
        total = 0
        for resource in parent.resources.values():
            total += properties["elementary charge"].values[resource.name] * resource.amount
        return str(total) + "e"
    elif args[0] in parent.resources:
            resource = parent.resources[args[0]]
            return str((resource.amount * properties["elementary charge"].values[resource.name])) + "e"
    else:
        return "nonexistent subatomic particle"