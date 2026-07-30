from abc import ABC, abstractmethod


class BaseGenerator(ABC):

    @property
    @abstractmethod
    def nombre(self):
        """
        Nombre único del generador.
        """
        pass

    @abstractmethod
    def generar(
        self,
        ranking,
        cantidad
    ):
        """
        Genera una lista de jugadas.
        """
        pass