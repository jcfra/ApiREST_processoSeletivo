from OrgaoA import OrgaoA
import mysql.connector
from flask_restful import Resource
import jsons

class Questao1(Resource):

    def __init__(self, ano='2018'):
        super()
        print('iniciando')
        self.host = 'localhost'
        self.user = 'root'
        self.database = 'desafio_selecao'
        self.password = 'Sapgui12$'
        self.ano = ano
        self.listaDeOrgaos = list()

    def get(self, ano):
        self.ano = ano
        self.conectaBanco()
        self.recuperaDados1()
        self.mydb.close()
        return  jsons.dumps(self.listaDeOrgaos)

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
    def recuperaDados1(self):
        print(self.mydb)
        mycursor = self.mydb.cursor(buffered=True, dictionary=True)
        mycursor.execute('select data_submissao,orgao, tipo_orgao from respostas_diagnostico where data_submissao is not null and ano_diagnostico = ' + self.ano)
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x['data_submissao'],x['orgao'], x['tipo_orgao'])
            orgao = OrgaoA(x['orgao'],x['tipo_orgao'])
            self.listaDeOrgaos.append(orgao)
        print(self.listaDeOrgaos)

# if __name__ == '__main__':
#    print('***',__name__)
#    quest1 = Questao1('2019')
#    quest1.conectaBanco()
#    quest1.recuperaDados()
#    print('Fim pgm')
