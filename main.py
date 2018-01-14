from plugin import Plugin
from simsys import Simsys
from resource import Resource
from command import Command
from property import Property
import subatomic
import atomicUnits


def exiter(system, args):
    exit(0)


def setPrompt(system, args):
    system.prompt = args

def exec(system, args):
    system(args)

particles = {"proton": Resource("proton"), "electron": Resource("electron"), "neutron": Resource("neutron")}
subatomic = Plugin("subatomic", particles, {"generate": Command("generate", subatomic.generate, 0.5), "view": Command("view", subatomic.view)}, {})
atomicUnits = Plugin("atomic units", {"mass": Resource("mass")}, {"view": Command("view", atomicUnits.view)}, {"elementary charge": Property("elementary charge", "charge", particles, {"proton": 1, "electron": -1, "neutron": 0})}, subatomic)
system = Simsys("system", {"printer": print, "input": input, "exit": exiter, "prompt": setPrompt, "exec": exec}, {"subatomic": subatomic, "atomicUnits": atomicUnits})

while True:
    system()
