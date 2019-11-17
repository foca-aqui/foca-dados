from flask import Flask


def make_app():
    app = Flask('app')
    app.config['MONGODB_DB'] = 'focadados'
    app.config['MONGODB_HOST'] = '127.0.0.1'
    app.config['MONGODB_CONNECT'] = False

    from app.model import db
    db.init_app(app)

    _register_blueprints(app)

    return app

def _register_blueprints(app):
    import sys
    sys.path.append("../")

    from .route.votacao import votacao

    app.register_blueprint(votacao)

