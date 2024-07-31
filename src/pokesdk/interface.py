"""
Generic Class to create custom python object from API responses
"""


class GenericResource(object):
    def __init__(self, dictionary):
        for key in dictionary:
            setattr(self, key, dictionary[key])

    def __repr__(self):
        return "<GenericResource: %s>" % self.__dict__
