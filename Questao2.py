from OrgaoB import OrgaoB
import mysql.connector
from TipoDeOrgao import TipoDeOrgao
from flask_restful import Resource
import jsons


class Questao2(Resource):

    def __init__(self, ano=2000, orgao='SF'):
        super()
        print('iniciando')
        self.host = 'localhost'
        self.user = 'root'
        self.database = 'desafio_selecao'
        self.password = 'Sapgui12$'
        self.listaDeOrgaos = list()
        self.ano = ano
        self.orgao = 'SF'
        if orgao != 'SF':
            self.orgao = orgao

    def get(self, ano, orgao='SF'):
        self.listaDeOrgaos = list()
        self.ano = ano
        self.orgao = orgao
        self.conectaBanco()
        self.recuperaDados2()
        self.mydb.close()
        return jsons.dumps(self.listaDeOrgaos)

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

    def recuperaDados2(self):
        print(self.mydb)
        if self.orgao != '*':
            select1 = 'select sum(qtd_equipe), orgao, tipo_orgao from respostas_diagnostico where data_submissao is not null and orgao = "'
            select2 = self.orgao + '"'
        else:
            select1 = 'select sum(qtd_equipe), orgao, tipo_orgao from respostas_diagnostico where data_submissao is not null '
            select2 = ' '

        select3 = ' and ano_diagnostico  = ' + "'" + str(self.ano) + "'"
        select = select1 + select2 + select3

        mycursor = self.mydb.cursor(buffered=True, dictionary=True)
        print(select)
        mycursor.execute(select)
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x['sum(qtd_equipe)'], x['orgao'], x['tipo_orgao'])
            if self.orgao == '*':
                orgao = OrgaoB('Todos', x['tipo_orgao'], str(self.ano), x['sum(qtd_equipe)'])
            else:
                orgao = OrgaoB(x['orgao'], x['tipo_orgao'], str(self.ano), x['sum(qtd_equipe)'])
        self.listaDeOrgaos.append(orgao)
        print(self.listaDeOrgaos)

        # if __name__ == '__main__':
        #     print('***', __name__)
        #     quest2 = Questao2(2018,'SMDHC')
        #     quest2.conectaBanco()
        #     quest2.recuperaDados()
        #     print('Fim pgm')
