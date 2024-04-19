import sys, traceback
from app import app, db
from app.models import *


with app.app_context():
    db.create_all()

    # Criando departamentos
    novo_departamento = Departamento(nome="Diretoria")
    db.session.add(novo_departamento)

    #Criando Funcionarios
    novo_funcionario = Funcionario(nome="Everton Oliveira", email='everton.oliveira@gmail.com', departamento=novo_departamento)
    db.session.add(novo_funcionario)
     
    novo_funcionario = Funcionario(nome="Jael Freixo Lopes", email='jael.freixo@gmail.com', departamento=novo_departamento)
    db.session.add(novo_funcionario)

    novo_funcionario = Funcionario(nome="Grace Mieiro Gois", email='grace.mieiro@gmail.com', departamento=novo_departamento)
    db.session.add(novo_funcionario)

    novo_funcionario = Funcionario(nome="Anaelle Vieira Camargo", email='anaelle.vieira@gmail.com', departamento=novo_departamento)
    db.session.add(novo_funcionario)
   
    # # Associando Gestor ao departamento
    # db.session.flush()
    # gestor = Gestor(funcionario_id=novo_funcionario.id, departamento_id=novo_departamento.id)
    # db.session.add(gestor)

    novo_departamento = Departamento(nome="Contabilidade")
    db.session.add(novo_departamento)

    #Criando Funcionarios
    novo_funcionario = Funcionario(nome="Benjamin Freire Malafaia", email='benjamin.freire@gmail.com')
    db.session.add(novo_funcionario)

    novo_funcionario = Funcionario(nome="Tomé Godoi Monsanto", email='tome.godoi@gmail.com')
    db.session.add(novo_funcionario)

    novo_funcionario = Funcionario(nome="Kael Queiroga Natal", email='kael.queiroga@gmail.com')
    db.session.add(novo_funcionario)

    novo_funcionario = Funcionario(nome="Emília Lopes Marçal", email='emilia.lopes@gmail.com')
    db.session.add(novo_funcionario)

    # # Associando Gestor ao departamento
    # db.session.flush()
    # gestor = Gestor(funcionario_id=novo_funcionario.id, departamento_id=novo_departamento.id)
    # db.session.add(gestor)

    novo_departamento = Departamento(nome="Financeiro")
    db.session.add(novo_departamento)

    #Criando Funcionarios
    novo_funcionario = Funcionario(nome="Antonia Sequeira Sardinha", email='antonia.sequeira@gmail.com', departamento=novo_departamento)
    db.session.add(novo_funcionario)

    novo_funcionario = Funcionario(nome="Deise Castilho Paz", email='deise.castilho@gmail.com', departamento=novo_departamento)
    db.session.add(novo_funcionario)

    novo_funcionario = Funcionario(nome="Nikol Palha Mata", email='nikol.palha@gmail.com', departamento=novo_departamento)
    db.session.add(novo_funcionario)

    # Associando Gestor ao departamento
    # db.session.flush()
    # gestor = Gestor(funcionario_id=novo_funcionario.id, departamento_id=novo_departamento.id)
    # db.session.add(gestor)

    novo_departamento = Departamento(nome="Tecnologia da Informação")
    db.session.add(novo_departamento)

    #Criando Funcionarios
    novo_funcionario = Funcionario(nome="Laurindo Lindim Carmo", email='laurindo.lindim@gmail.com', departamento=novo_departamento)
    db.session.add(novo_funcionario)

    novo_funcionario = Funcionario(nome="Célio Regueira Mexia", email='célio.regueira@gmail.com', departamento=novo_departamento)
    db.session.add(novo_funcionario)

    novo_funcionario = Funcionario(nome="Kiamy Amaral Cortesão", email='kiamy.amaral@gmail.com', departamento=novo_departamento)
    db.session.add(novo_funcionario)

    novo_funcionario = Funcionario(nome="Rahyssa Lima Covinha", email='rahyssa.lima@gmail.com', departamento=novo_departamento)
    db.session.add(novo_funcionario)

    novo_funcionario = Funcionario(nome="Fábio Cardoso Rufino", email='fábio.cardoso@gmail.com', departamento=novo_departamento)
    db.session.add(novo_funcionario)

    # # Associando Gestor ao departamento
    # db.session.flush()
    # gestor = Gestor(funcionario_id=novo_funcionario.id, departamento_id=novo_departamento.id)
    # db.session.add(gestor)
   
    db.session.commit()