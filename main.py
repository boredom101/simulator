from plugin import Plugin
from simsys import Simsys
from resource import Resource
from command import Command
from property import Property
from item import Item
from table import Table
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

atomdata = Table("atomdata", {"hydrogen": {"name": "hydrogen", "protons": 1, "electrons": 1, "neutrons": 0},
                              "helium": {"name": "helium", "protons": 2, "electrons": 2, "neutrons": 2},
                              "lithium": {"name": "lithium", "protons": 3, "electrons": 3, "neutrons": 4},
                              "beryllium": {"name": "beryllium", "protons": 4, "electrons": 4, "neutrons": 5}})

particles = {"proton": Resource("proton"), "electron": Resource("electron"), "neutron": Resource("neutron")}
subPlugin = Plugin("atomic", particles, {}, {}, {}, {})

# the parent plugin
subatomic = Plugin("subatomic", particles, {"generate": Command("generate", subatomic.generate, 5), "view": Command("view", subatomic.view)}, {}, {}, {})

atoms = {"hydrogen": Resource("hydrogen"), "helium": Resource("helium"), "lithium": Resource("lithium"), "beryllium": Resource("beryllium")}

# the child plugins
atomicUnits = Plugin("atomic units", {"mass": Resource("mass")}, {"view": Command("view", atomicUnits.view)}, {"elementary charge": Property("elementary charge", "charge", particles, {"proton": 1, "electron": -1, "neutron": 0})}, {}, {}, subatomic)

atom = Plugin("atom", atoms, {"create": Command("create", atom.create), "list": Command("list", atom.list)}, {}, {"atoms": Item("atoms", {}, subPlugin)}, {"atomdata": atomdata}, subatomic)

# the main system containing the plugins
system = Simsys("system", {"echo": echo, "input": inputer, "exit": exiter, "prompt": setPrompt, "exec": exec}, {"subatomic": subatomic, "atomicUnits": atomicUnits, "atom": atom}, ["atomicUnits", "view"])

while True:
    output = system()
    if output:
        print(output)
