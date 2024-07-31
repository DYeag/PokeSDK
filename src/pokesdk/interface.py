"""
Generic Class to create custom python object from API responses
"""


class GenericResource(object):
    def __init__(self, dictionary):
        for key in dictionary:
            setattr(self, key, dictionary[key])

    def __repr__(self):
        return "<dict2obj: %s>" % self.__dict__
