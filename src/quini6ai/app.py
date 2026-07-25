from quini6ai.database.migrations import Migration
from quini6ai.menu import Menu


class App:

    def run(self):

        Migration().run()

        Menu().mostrar()