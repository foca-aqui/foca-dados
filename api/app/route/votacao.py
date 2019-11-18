from flask import jsonify, Blueprint
from flask import request
from ..controller.controller_votacao import ControllerVotacao


votacao = Blueprint('votacao', __name__, url_prefix='/votacao')
controller = ControllerVotacao()


@votacao.route('',  methods=['GET'])
def get_votacao():
    params = request.get_json()
    parametros = {
        'cidade': params.get('cidade'),
        'candidato': params.get('cidade'),
    }

    votacao = controller.get_votacao(parametros)

    return jsonify(resultado=votacao)

@votacao.route('/teste',  methods=['GET'])
def teste_votacao():

    return jsonify(resultado='Passou no teste')