class BaseService:

    @property
    def nombre(self):
        raise NotImplementedError

    def ejecutar(self):
        raise NotImplementedError