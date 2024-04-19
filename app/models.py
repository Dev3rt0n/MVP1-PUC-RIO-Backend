import os
import binascii
import datetime

from app import db

class Model(db.Model):
    __abstract__ = True
    __public__ = ()
    created = db.Column(db.DateTime, default=datetime.datetime.now)
    updated = db.Column(db.DateTime, default=datetime.datetime.now,
                        onupdate=datetime.datetime.now)

    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    @classmethod
    def from_dict(cls, json):
        items = {}
        for key, val in json.items():
            if isinstance(val, (str, int, list)):
                if hasattr(cls, key):
                    items[key] = val
        return cls(**items)

    @classmethod
    def get(cls, id):
        return cls.query.get(id)

"""Tabela Associativa: FuncionariosProjetos
- funcionario_id (FK)
- projeto_id (FK)"""
associacao_funcionario_projeto = db.Table('associacao_funcionario_projeto',
    db.Column('funcionario_id', db.Integer, db.ForeignKey('funcionarios.id'), primary_key=True),
    db.Column('projeto_id', db.Integer, db.ForeignKey('projetos.id'), primary_key=True)
)

class Funcionario(Model):
    """User model"""
    __tablename__ = 'funcionarios'
    __public__ = ('nome', 'email')
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    departamento_id = db.Column(db.Integer, db.ForeignKey('departamentos.id'))
    
    #departamento_gestor = db.relationship("Departamento", uselist=False, backref="gestor")
    #projetos = db.relationship('Projeto', secondary='associacao_funcionario_projeto', back_populates='funcionarios')

    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True)

    def __init__(self, **kwargs):
        super(Funcionario, self).__init__(**kwargs)
    
class Departamento(Model):
    """User model"""
    __tablename__ = 'departamentos'
    __public__ = ('nome')
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    funcionarios = db.relationship('Funcionario', backref='departamento')
    projetos = db.relationship('Projeto', backref='departamento')

    nome = db.Column(db.String(255), unique=True, nullable=False)

    def __init__(self, **kwargs):
        super(Departamento, self).__init__(**kwargs)

class Projeto(Model):
    """Projetos
    - projeto_id (PK)
    - departamento_id (FK)
    - Nome
    - Código de Serviço"""
    __tablename__ = 'projetos'
    __public__ = ('nome')
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    departamento_id = db.Column(db.Integer, db.ForeignKey('departamentos.id'))

    funcionarios = db.relationship(
        'Funcionario',
        secondary=associacao_funcionario_projeto,
        backref=db.backref('projetos', lazy='dynamic'),
        cascade="all, delete"
    )

    nome = db.Column(db.String(255), nullable=False)
    cod_serv = db.Column(db.String(15), nullable=False)

    def __init__(self, **kwargs):
        super(Projeto, self).__init__(**kwargs)
