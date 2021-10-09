class Orgao:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.DesktopProprio = 0
        self.DesktopLocado = 0

    def setDesktopProprio(self, desktopProprio):
            self.DesktopProprio = int(desktopProprio)

    def setDesktopLocado(self, desktopLocado):
            self.DesktopLocado = int(desktopLocado)
