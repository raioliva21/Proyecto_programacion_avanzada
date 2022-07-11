from abc import abstractmethod
from abc import ABCMeta

""" clase abstracta"""
class Ciudadano(metaclass = ABCMeta):

    def __init__(self):
        self.__id = None
        self.__estado = None

    @abstractmethod
    def ID(self):
        pass
    