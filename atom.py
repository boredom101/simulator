def create (plugin, args, parent):
    if (len(args) == 0):
        return "no element name given"
    element = args[0]
    if element in plugin.tables["atomdata"].rows.keys():
        flag = True
        insufficient = []
        for particle in ["electron", "proton", "neutron"]:
            if parent.resources[particle].amount < plugin.tables["atomdata"][[element, particle + "s"]]:
                flag = False
                insufficient.append(particle + "s")
        if flag:
            parent.resources["electron"].modify(-plugin.tables["atomdata"][[element, "electrons"]])
            parent.resources["proton"].modify(-plugin.tables["atomdata"][[element, "protons"]])
            parent.resources["neutron"].modify(-plugin.tables["atomdata"][[element, "neutrons"]])
            name = element + str(len(plugin.items["atoms"].info))
            plugin.items["atoms"](-1, [name])
            return "created atom " + name
        else:
            return "insufficient " + ", ".join(insufficient)
    else:
        return "there is no element named " + element

def list (plugin, args, parent):
    return "\n".join(plugin.items["atoms"].info.keys())