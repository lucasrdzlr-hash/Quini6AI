class PluginManager:

    def __init__(self):

        self.plugins = {}

    def registrar(self, plugin):
        """
        Registra un plugin disponible.
        """

        self.plugins[plugin.nombre] = plugin

    def ejecutar(self, df, estrategia):
        """
        Ejecuta todos los plugins activos de la estrategia
        respetando el orden configurado en el YAML.
        """

        plugins = [

            (nombre, configuracion)

            for nombre, configuracion

            in estrategia["plugins"].items()

            if configuracion["activo"]

        ]

        plugins.sort(
            key=lambda item: item[1]["orden"]
        )

        for nombre, configuracion in plugins:

            plugin = self.plugins.get(nombre)

            if plugin is None:

                print(
                    f"Plugin '{nombre}' no registrado."
                )

                continue

            print(
                f"Ejecutando plugin: {nombre}"
            )

            df = plugin.ejecutar(
                df,
                configuracion["parametros"]
            )

        return df