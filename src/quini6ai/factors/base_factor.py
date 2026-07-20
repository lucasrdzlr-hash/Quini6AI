from abc import ABC, abstractmethod


class BaseFactor(ABC):

    nombre = ""

    @abstractmethod
    def calcular(self, jugada, ranking):

        """
        Debe devolver un valor entre 0 y 1
        """

        pass