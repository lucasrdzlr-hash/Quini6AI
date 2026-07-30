class GeneratorManager:

    def __init__(self):

        self.generators = {}

    def registrar(self, generator):

        self.generators[
            generator.nombre
        ] = generator

    def obtener(self, nombre):

        generator = self.generators.get(
            nombre
        )

        if generator is None:

            raise ValueError(
                f"Generator '{nombre}' no registrado."
            )

        return generator