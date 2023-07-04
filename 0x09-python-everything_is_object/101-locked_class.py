#!/usr/bin/python3


class LockedClass:
    """

This is a module that containts a clas that avoids
dynmaically created attributes

"""

    __slots__ = ['first_name']
