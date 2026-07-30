class RuleManager:

    def __init__(self):

        self.rules = {}

    def registrar(self, rule):

        self.rules[rule.nombre] = rule

    def validar(self, jugada, estrategia):

        rules = estrategia["rules"]

        for nombre, config in rules.items():

            if not config["activo"]:
                continue

            regla = self.rules.get(nombre)

            if regla is None:

                print(
                    f"Regla '{nombre}' no registrada."
                )

                continue

            if not regla.validar(
                jugada,
                config["parametros"]
            ):

                print(
                    f"No cumple la regla '{nombre}'."
                )

                return False

        return True