class Humano(object):
    def __init__(self, ojos, manos):
        self.ojos = ojos
        self.manos = manos

class Hombre(Humano):
    def __init__(self, ojos, manos, genero):
        Humano.__init__(self, ojos, manos)
        self.genero = genero

    def __str__(self):
        return 'el genro es {}, '.format(self.genero, self.ojos)