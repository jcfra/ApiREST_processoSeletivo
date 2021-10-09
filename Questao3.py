from Orgao import Orgao
import mysql.connector
from TipoDeOrgao import TipoDeOrgao
from flask_restful import Resource
import jsons


class Questao3(Resource):

    def __init__(self):
        super()
        print('iniciando')
        self.host = 'localhost'
        self.user = 'root'
        self.database = 'desafio_selecao'
        self.password = 'Sapgui12$'
        self.listaDeTiposDeOrgaos = list()

    def get(self):
        self.conectaBanco()
        self.recuperaDados3()
        self.mydb.close()
        return jsons.dumps( self.listaDeTiposDeOrgaos)

    def conectaBanco(self):

        self.mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            database=self.database,
            password=self.password)
        # mydb = mysql.connector.connect(
        #     host='localhost',
        #     user='root',
        #     database='desafio_selecao',
        #     password='Sapgui12$')
        print(self.mydb)

    def recuperaDados3(self):
        print(self.mydb)
        mycursor = self.mydb.cursor(buffered=True, dictionary=True)
        mycursor.execute('select sum(qtd_equipe) from respostas_diagnostico where data_submissao is not null')
        myresult = mycursor.fetchall()
        for linTotal in myresult:
            print(linTotal)
            total = linTotal['sum(qtd_equipe)']
        mycursor.execute('select tipo_orgao, sum(qtd_equipe) from respostas_diagnostico where data_submissao is not null group by tipo_orgao')
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x['tipo_orgao'], x['sum(qtd_equipe)'])
            proporcao = x['sum(qtd_equipe)'] * 100 / total
            strproporcao = "%0.2f" % proporcao
            strproporcao += '%'
            TipoDeOrgaoorgao = TipoDeOrgao(x['tipo_orgao'], strproporcao)
            print((x['tipo_orgao'], proporcao))
            self.listaDeTiposDeOrgaos.append(TipoDeOrgaoorgao)
        print(self.listaDeTiposDeOrgaos)



# if __name__ == '__main__':
#     print('***', __name__)
#     quest3 = Questao3()
#     quest3.conectaBanco()
#     quest3.recuperaDados()
#     print('Fim pgm')
