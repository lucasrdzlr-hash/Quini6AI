class BaseProvider:

    def cargar(self):
        raise NotImplementedError(
            "Los providers deben implementar cargar()."
        )