##from Questao6 import Questao6
import mysql.connector
from flask_restful import Resource
import jsons


class Questao6(Resource):

    def __init__(self):
        super()
        print('iniciando')
        print('iniciando')
        self.host = 'localhost'
        self.user = 'root'

        self.database = 'desafio_selecao'
        self.password = 'Sapgui12$'




    def get(self, id_resposta, ano_diagnostico,qtd_equipe,utiliza_metodologia,desktop_proprio,desktop_locado,desktop_proprio_antigo):
        self.id_resposta = id_resposta
        self.ano = ano_diagnostico
        self.qtd_equipe = qtd_equipe
        self.utiliza_metodologia = utiliza_metodologia
        self.desktop_proprio = desktop_proprio
        self.desktop_locado = desktop_locado
        self.desktop_proprio_antigo = desktop_proprio_antigo


        self.conectaBanco()
        self.alteraDados6()
        self.mydb.commit()
        self.mydb.close()
        return {'message': 'Alterações efetuadas'}, 200

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

    def alteraDados6(self):
        print(self.mydb)

        sql = 'update respostas_diagnostico_copia set qtd_equipe = ' + str(self.qtd_equipe)
        sql += ', utiliza_metodologia = ' + str(self.utiliza_metodologia)
        sql += ',ultima_atualizacao = now(),  desktop_proprio = ' + str(self.desktop_proprio)
        sql += ',  desktop_locado = ' + str(self.desktop_locado)
        sql += ',  desktop_proprio_antigo  = ' + str(self.desktop_proprio_antigo)
        sql += ' where id_resposta = ' + str(self.id_resposta)
        sql += ' and ano_diagnostico = ' + str(self.ano)
        print(sql)
        mycursor = self.mydb.cursor()
        mycursor.execute(sql)

# if __name__ == '__main__':
#     print('***', __name__)
#
#     qtd_equipe = 900
#     utiliza_metodologia = 1
#     desktop_proprio = 200
#     desktop_locado = 8
#     desktop_proprio_antigo = 9
#     ano_diagnostico = 2017
#     id_resposta = 10
#
#     quest6 = Questao6(qtd_equipe, utiliza_metodologia, desktop_proprio, desktop_locado, desktop_proprio_antigo,
#                 ano_diagnostico, id_resposta)
#
#     quest6.get(qtd_equipe, utiliza_metodologia, desktop_proprio, desktop_locado, desktop_proprio_antigo,
#                 ano_diagnostico, id_resposta)
# print('Fim pgm')
