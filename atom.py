def create (plugin, args, parent):
    if (len(args) == 0):
        return "no element name given"
    element = args[0]
    if element in plugin.resources.keys():
        flag = True
        insufficient = []
        for particle in ["electron", "proton", "neutron"]:
            if parent.resources[particle].amount < plugin.properties[particle + "s"].values[element]:
                flag = False
                insufficient.append(particle + "s")
        if flag:
            parent.resources["electron"].modify(-plugin.properties["electrons"].values[element])
            parent.resources["proton"].modify(-plugin.properties["protons"].values[element])
            parent.resources["neutron"].modify(-plugin.properties["neutrons"].values[element])
            name = element + str(len(plugin.items["atoms"].info))
            plugin.items["atoms"](-1, [name])
            return "created atom " + name
        else:
            return "insufficient " + ", ".join(insufficient)
    else:
        return "there is no element named " + element

def list (plugin, args, parent):
    return "Atoms:\n" + "\n".join(plugin.items["atoms"].info.keys())