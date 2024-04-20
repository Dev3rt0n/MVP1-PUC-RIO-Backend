from flask import request, jsonify

from app import db
from app.models import Departamento, Funcionario
from . import api

@api.route('/departamentos', methods=['POST'])
def criar_departamento():
    try:
        nome = request.json['nome']
        funcionarios = request.json['list_func']

        novo_departamento = Departamento(nome=nome)
        db.session.add(novo_departamento)
        # Flush para recuperar o ID do objeto
        db.session.flush()

        for funcionario in funcionarios:
            membro = Funcionario.get(int(funcionario))
            membro.departamento_id = novo_departamento.id

        db.session.commit()
        return "", 201
    except Exception as e:
        return {'mensagem': e}, 500

@api.route('/departamentos', methods=['GET'])
def obter_departamentos():
    try:
        todos_departamentos = Departamento.query.all()
        return jsonify([{
            'id': departamento.id,
            'nome': departamento.nome,
            'funcionarios': [{
                'id': funcionario.id,
                'nome': funcionario.nome,
                'email': funcionario.email
            } for funcionario in departamento.funcionarios]
        } for departamento in todos_departamentos]), 201
    except Exception as e:
        return {'mensagem': e}, 500

@api.route('/departamentos/<int:id>', methods=['GET'])
def obter_departamento(id):
    try:
        departamento = Departamento.get(id)
        return jsonify({
            'mensagem': 'Operação realizada com sucesso',
            'id': departamento.id,
            'nome': departamento.nome,
            'funcionarios': [{
                'id': funcionario.id,
                'nome': funcionario.nome,
                'email': funcionario.email
            } for funcionario in departamento.funcionarios]
        }), 201
    except Exception as e:
        return {'mensagem': e}, 500

