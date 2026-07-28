from abc import ABC, abstractmethod


class BasePlugin(ABC):

    @property
    @abstractmethod
    def nombre(self):
        pass

    @abstractmethod
    def ejecutar(self, df, configuracion):
        """
        Recibe un DataFrame.

        Debe devolver el DataFrame modificado.
        """
        pass