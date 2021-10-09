from flask import Flask
from flask_restful  import Api

from Questao1 import Questao1
from Questao2 import Questao2
from Questao3 import Questao3
from Questao4 import Questao4
from Questao6 import Questao6

app = Flask(__name__)
api = Api(app)
api.add_resource(Questao1,'/quest1/<string:ano>')
api.add_resource(Questao2,'/quest2/<string:ano>/<string:orgao>/')
api.add_resource(Questao3,'/quest3/')
api.add_resource(Questao4,'/quest4/')
api.add_resource(Questao6,'/quest6/<string:id_resposta>/<string:ano_diagnostico>/<string:qtd_equipe>/<string:utiliza_metodologia>/<string:desktop_proprio>/<string:desktop_locado>/<string:desktop_proprio_antigo>/')

if __name__ == '__main__':
    app.run(debug=True)