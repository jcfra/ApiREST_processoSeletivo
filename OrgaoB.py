class OrgaoB:
    def __init__(self, nome, tipo, ano, somaequipe):
        self.nome = nome
        self.tipo = tipo
        self.ano = ano
        x = str(somaequipe)
        print (type(somaequipe))
        if x == 'None':
            self.somaEquipe = 0
        else:
            self.somaEquipe = int(somaequipe)







