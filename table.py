class Table:

    def __init__(self, name, rows):
        self.name = name
        self.rows = rows

    def __getitem__(self, item):
        return self.rows[item[0]][item[1]]