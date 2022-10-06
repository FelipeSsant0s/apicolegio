from flask import Flask, render_template, request
import urllib.request, json
from flask_sqlalchemy import SQLAlchemy

app = Flask (__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cursos.sqlite3"

db = SQLAlchemy(app)


armazenamentos = []
registros = []

class cursos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    descricao = db.Column(db.String(100))
    ch = db.Column(db.Integer)

    def __init__(self, nome, descricao, ch):
        self.nome = nome
        self.descricao = descricao
        self.ch = ch



@app.route('/', methods=['GET', 'POST'])
def principal():
    if request.method == 'POST':
        if request.form.get("profer") and request.form.get('mater'):
            armazenamentos.append({'profer': request.form.get('profer'), 'mater': request.form.get('mater')})
    return render_template('index.html', armazenamentos=armazenamentos)

@app.route('/student', methods=['GET', 'POST'])
def student():
    if request.method == 'POST':
        if request.form.get('aluno') and request.form.get('idd'):
            registros.append({'aluno': request.form.get('aluno'), 'idd': request.form.get('idd')})
    return render_template('student.html', registros=registros)

@app.route('/cursos', methods=['GET', 'POST'])
def lista_cursos():
    return render_template('cursos.html',cursos=cursos.query.all())





if __name__ == '__main__':
    app.run(debug=True)
with app.app_context():
    db.create_all()