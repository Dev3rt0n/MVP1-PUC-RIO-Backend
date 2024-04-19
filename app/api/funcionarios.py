from flask import request, jsonify

from app import db
from app.models import Funcionario, Departamento
from . import api

@api.route('/funcionarios', methods=['POST'])
def criar_funcionario():
    try:
        novo_funcionario = Funcionario.from_dict(request.json)
        db.session.add(novo_funcionario)
        db.session.commit()

        return {'mensagem': 'Operação realizada com sucesso'}, 201
    except Exception as e:
        return {'mensagem': e}, 500

@api.route('/funcionarios', methods=['GET'])
def obter_funcionarios():
    try:
        todos_funcionarios = Funcionario.query.all()
        return jsonify([{
                'id': funcionario.id,
                'nome': funcionario.nome,
                'email': funcionario.email,
                'departamento': {
                    'id': funcionario.departamento.id,
                    'nome': funcionario.departamento.nome,
                } if funcionario.departamento else {

                }
            } for funcionario in todos_funcionarios
        ]), 200
    except Exception as e:
        return {'mensagem': e}, 500

@api.route('/funcionarios/<int:id>', methods=['GET'])
def obter_funcionario(id):
    try:
        funcionario = Funcionario.get(id)
        return jsonify({
            'mensagem': 'Operação realizada com sucesso',
            'id': funcionario.id,
            'nome': funcionario.nome,
            'email': funcionario.email,
            'departamento': {
                'id': funcionario.departamento.id,
                'nome': funcionario.departamento.nome
            } if funcionario.departamento else {

            }
        }), 200
    except Exception as e:
        return {'mensagem': e}, 500

@api.route('/funcionarios/<int:id>', methods=['PUT'])
def atualizar_funcionario(id):
    try:
        funcionario = Funcionario.get(id)
        nome = request.json.get('nome')
        email = request.json.get('email')
        departamento = request.json.get('departamento')

        if nome:
            funcionario.nome = nome
        if email:
            funcionario.email = email
        if departamento:
            novo_departamento = Departamento.get(int(departamento))
            funcionario.departamento = novo_departamento
        db.session.commit()

        return {'mensagem': 'Operação realizada com sucesso'}, 200
    except Exception as e:
        return {'mensagem': e}, 500

@api.route('/funcionarios/<int:id>', methods=['DELETE'])
def deletar_funcionario(id):
    try:
        funcionario = Funcionario.get(id)
        db.session.delete(funcionario)
        db.session.commit()

        return {'mensagem': 'Operação realizada com sucesso'}, 200
    except Exception as e:
        return {'mensagem': e}, 500

