from plugin import Plugin
from simsys import Simsys
from resource import Resource
from command import Command
from property import Property
from item import Item
import subatomic
import atomicUnits
import atom

def exiter(system, args):
    exit(0)


def setPrompt(system, args):
    system.prompt = args

def exec(system, args):
    return system(args)

def echo(system, args):
    return " ".join(args)

def inputer(system, args):
    return input(args)

# resources used in multiple plugins

particles = {"proton": Resource("proton"), "electron": Resource("electron"), "neutron": Resource("neutron")}
subPlugin = Plugin("atomic", particles, {}, {}, {})

# the parent plugin
subatomic = Plugin("subatomic", particles, {"generate": Command("generate", subatomic.generate, 5), "view": Command("view", subatomic.view)}, {}, {})

atoms = {"hydrogen": Resource("hydrogen"), "helium": Resource("helium")}

# the child plugins
atomicUnits = Plugin("atomic units", {"mass": Resource("mass")}, {"view": Command("view", atomicUnits.view)}, {"elementary charge": Property("elementary charge", "charge", particles, {"proton": 1, "electron": -1, "neutron": 0})}, {}, subatomic)

atom = Plugin("atom", atoms, {"create": Command("create", atom.create), "list": Command("list", atom.list)}, {"protons": Property("protons", "count", atoms, {"hydrogen": 1, "helium": 2}), "electrons": Property("electrons", "count", atoms, {"hydrogen": 1, "helium": 2}), "neutrons": Property("neutrons", "count", atoms, {"hydrogen": 0, "helium": 2})}, {"atoms": Item("atoms", {}, subPlugin)}, subatomic)

# the main system containing the plugins
system = Simsys("system", {"echo": echo, "input": inputer, "exit": exiter, "prompt": setPrompt, "exec": exec}, {"subatomic": subatomic, "atomicUnits": atomicUnits, "atom": atom}, ["atomicUnits", "view"])

while True:
    output = system()
    if output:
        print(output)
