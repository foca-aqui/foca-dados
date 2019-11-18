from app.model.data import db


class Votacao(db.Document):

    nome = db.StringField(required=True)
    nome_urna = db.StringField()
    bairro = db.StringField()
    qtd_votos = db.StringField()
    porcentagem_votos = db.StringField()



