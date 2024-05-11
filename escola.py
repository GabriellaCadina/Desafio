class Estudante:
    nome = None
    matricula = None
    escola = 'Dio'

    def __init__(self, nome_do_estudante, matricula_do_estudante):
        self.nome = nome_do_estudante
        self.matricula = matricula_do_estudante

    def __str__(self) -> str:
        return f'{self.escola} - {self.matricula} - {self.nome}'

estudante1 = Estudante('Gabi', '999')
estudante1.batatinha()
print(estudante1)

estudante2 = Estudante('Mumu', '991')
print(estudante2)
