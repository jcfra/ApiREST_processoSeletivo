from Orgao import Orgao
import mysql.connector
from TipoDeOrgao import TipoDeOrgao
from flask_restful import Resource
import jsons


class Questao4(Resource):

    def __init__(self):
        super()
        print('iniciando')
        self.host = 'localhost'
        self.user = 'root'
        self.database = 'desafio_selecao'
        self.password = 'Sapgui12$'
        self.listaDeOrgaos = list()

    def get(self):
        self.conectaBanco()
        self.recuperaDados4()
        self.mydb.close()
        return jsons.dumps( self.listaDeOrgaos)

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

    def recuperaDados4(self):
        print(self.mydb)
        mycursor = self.mydb.cursor(buffered=True, dictionary=True)
        select = 'select orgao, tipo_orgao, sum(desktop_proprio), sum(desktop_locado) from respostas_diagnostico  where data_submissao is not null and tipo_orgao = ' + '\'Secretaria\'' + 'group by orgao'
        mycursor.execute(select)
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x['orgao'], x['tipo_orgao'], x['sum(desktop_proprio)'], x['sum(desktop_locado)'])
            orgao =  orgao = Orgao(x['orgao'],x['tipo_orgao'])
            orgao.setDesktopLocado(x['sum(desktop_locado)'])
            orgao.setDesktopProprio(x['sum(desktop_proprio)'])
            self.listaDeOrgaos.append(orgao)
        print(self.listaDeOrgaos)



# if __name__ == '__main__':
#     print('***', __name__)
#     quest3 = Questao4()
#     quest3.conectaBanco()
#     quest3.recuperaDados()
#     print('Fim pgm')
