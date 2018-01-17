class Resource:

    # a quantitative measurement.

    # name: used by plugin and any child plugin.
    # amount: a default amount or could be used for a save feature
    def __init__(self, name, amount=0):
        self.name = name
        self.amount = amount

    def modify(self, amount: object) -> object:
        self.amount += amount