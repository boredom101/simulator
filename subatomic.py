def generate (plugin, args, parent):
    if args[0] in plugin.resources:
        plugin.resources[args[0]].modify(1)
    else:
        return "nonexistent subatomic particle"

def view (plugin, args, parent):
    if (args[0] in plugin.resources):
        return str(plugin.resources[args[0]].amount)
    else:
        return "nonexistent subatomic particle"