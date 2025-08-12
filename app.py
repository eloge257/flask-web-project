from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# creation de l application Flask
app = Flask(__name__)
# Configuration MySQL (remplace par tes infos)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/facturation'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DB + Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Modèle (table)
class Utilisateurs(db.Model):
    id_utilisateur = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    nom = db.Column(db.String(100), unique=True, nullable=False)
    prenom = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Utilisateurs {self.nom}>"

class Categorie(db.Model):
    id_categorie = db.Column(db.Integer, primary_key=True)
    nom_categorie = db.Column(db.String(100), nullable=False)
    etat_categorie = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Categorie {self.nom_categorie}>"
class Materiel(db.Model):
    id_mat = db.Column(db.Integer, primary_key=True)
    nom_materiel = db.Column(db.String(50), nullable=False)
    id_categorie = db.Column(db.Integer, nullable=False)
    etat = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Materiel {self.nom_mat}>"

# les routes de l'application
@app.route('/')
def home():
    # Lire tous les utilisateurs
    utilisateurs = Utilisateurs.query.all()
    categorie = Categorie.query.all()
    return render_template('index.html', title="Accueil",utilisateurs=utilisateurs, categorie =categorie)

@app.route('/about')
def about():
    return render_template('about.html', title="A propos")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")

# pour lancer l application
if __name__ == '__main__':
    # db.create_all()  # Crée les tables si elles n'existent pas
    with app.app_context():
        db.create_all()
    app.run(debug=True)

