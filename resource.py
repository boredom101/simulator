class Resource:

    def __init__(self, name, amount=0):
        self.name = name
        self.amount = amount

    def get(self):
        return self.amount

    def modify(self, amount):
        self.amount += amount