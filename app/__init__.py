from config import Config

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)

db.init_app(app)

swagger_blueprint = get_swaggerui_blueprint(
    app.config['SWAGGER_URL'],
    app.config['API_URL'],
    config={
        'app_name': "Sample API"
    }
)
app.register_blueprint(
    swagger_blueprint,
    url_prefix=app.config['SWAGGER_URL']
)
from .api import api as api_blueprint
app.register_blueprint(
    api_blueprint
)

@app.route('/', methods=['GET'])
def home():
    return "O serviço está online", 200