import datetime

from app import db

class Model(db.Model):
    """Cria atributos e métodos comuns a todos os demais modelos"""
    __abstract__ = True
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

class Funcionario(Model):
    __tablename__ = 'funcionarios'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    departamento_id = db.Column(db.Integer, db.ForeignKey('departamentos.id'))
    
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True)

    def __init__(self, **kwargs):
        super(Funcionario, self).__init__(**kwargs)
    
class Departamento(Model):
    __tablename__ = 'departamentos'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    funcionarios = db.relationship('Funcionario', backref='departamento')
    projetos = db.relationship('Projeto', backref='departamento')

    nome = db.Column(db.String(255), unique=True, nullable=False)

    def __init__(self, **kwargs):
        super(Departamento, self).__init__(**kwargs)

