class Comida:

    def __init__(self, nome, estragada):
        self.nome = nome
        self._estragada = estragada

    def marcar_como_estragada(self):
        self._estragada = True

    @property
    def estragada(self):
        if self._estragada:
            return 'Sim'
        else:
            return 'Não'

lasanha = Comida('lasanha', False)

# 7 dias depois

lasanha.marcar_como_estragada()

# 1 dia depois


# 

# Estragado?
print(lasanha.estragada)