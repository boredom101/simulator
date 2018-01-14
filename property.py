class Property:

    # A static property to add to a group of resources

    # name : used by plugin and any child plugin.
    # type : type of measurement, used for conversion (currently only 'charge' and 'other')
    # resources : a dictionary of resources that it applies to
    # values : a dictionary of values for each resource
    # NOTE: the keys of resources and values, MUST correspond

    def __init__(self, name, type, resources, values):
        self.name = name
        self.type = type
        self.resources = resources
        self.values = values