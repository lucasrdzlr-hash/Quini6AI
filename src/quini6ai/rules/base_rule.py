class BaseRule:

    @property
    def nombre(self):
        raise NotImplementedError

    def validar(self, jugada, parametros):
        raise NotImplementedError