from config import db

class Cachorro(db.Model):
    __tablename__ = 'cachorros'

    # Identificador único
    id = db.Column(db.Integer, primary_key=True)
    
    # Atributos do cachorro
    nome = db.Column(db.String(80), nullable=False)
    raca = db.Column(db.String(80), nullable=False)
    idade = db.Column(db.Integer, nullable=False)

    def json(self):
        """
        Retorna os dados do cachorro em formato JSON.
        """
        return {
            'id': self.id,
            'nome': self.nome,
            'raca': self.raca,
            'idade': self.idade
        }
