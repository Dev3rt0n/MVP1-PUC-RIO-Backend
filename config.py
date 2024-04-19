import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Casse de configuração
    Configurações centradas em um único arquivo e classe
    para facilitar o acesso e organização do projeto
    """
    #: Secret key
    SECRET_KEY = "my-secret"

    #: Configurações do Banco de dados
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    #: Caminho raiz do projeto
    ROOT = basedir
    APP_ROOT = os.path.join(ROOT, 'app')

    # Dados do Swagger
    SWAGGER_URL= '/swagger'
    API_URL= '/static/swagger.json'

