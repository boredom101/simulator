def view (plugin, args, parent):
    if len(args) == 0:
        total = 0
        for resource in parent.resources.values():
            total += plugin.properties["elementary charge"].values[resource.name] * resource.amount
        return str(total) + "e"
    elif args[0] in parent.resources:
            resource = parent.resources[args[0]]
            return str((resource.amount * plugin.properties["elementary charge"].values[resource.name])) + "e"
    else:
        return "nonexistent subatomic particle"