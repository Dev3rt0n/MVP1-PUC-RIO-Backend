from flask import request, jsonify

from app import db
from app.models import Departamento, Funcionario
from . import api

@api.route('/departamentos', methods=['POST'])
def criar_departamento():
    nome = request.json['nome']
    funcionarios = request.json['list_func']

    print(nome)
    print(funcionarios)
    novo_departamento = Departamento(nome=nome)
    db.session.add(novo_departamento)
    db.session.flush()

    for funcionario in funcionarios:
        membro = Funcionario.get(int(funcionario))
        membro.departamento_id = novo_departamento.id

    db.session.commit()

    return "", 201

@api.route('/departamentos', methods=['GET'])
def obter_departamentos():
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

@api.route('/departamentos/<int:id>', methods=['GET'])
def obter_departamento(id):
    departamento = Departamento.get(id)
    return jsonify({
        'id': departamento.id,
        'nome': departamento.nome,
        'funcionarios': [{
            'id': funcionario.id,
            'nome': funcionario.nome,
            'email': funcionario.email
        } for funcionario in departamento.funcionarios]
    }), 201

@api.route('/departamentos/<int:id>', methods=['DELETE'])
def deletar_departamento(id):
    departamento = Departamento.get(id)
    db.session.delete(departamento)
    db.session.commit()

    return "", 201
