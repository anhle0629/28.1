
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Pet(db.Model):
    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    name = db.Column(db.Text, nullable = False)
    
    speices = db.Column(db.Text, nullable = False)
    
    photo = db.Column(db.Text, nullable = True)
    
    age = db.Column(db.Interger, nullable = True)    
    
    notes = db.Column(db.Boolean, nullable = True)

    ##added this on solution 
    available = db.Column(db.Boolean, nullable=False, default=True)    

##added this on from soloution
def image_url(self):
        """Return image for pet -- bespoke or generic."""

        return self.photo_url or GENERIC_IMAGE


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)