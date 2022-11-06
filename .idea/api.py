from flask import Flask, render_template, request, redirect, url_for, flash

from flask_sqlalchemy import SQLAlchemy

app = Flask (__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db_colegio.sqlite3"

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



class alunos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    materia = db.Column(db.String(100))
       
    def __init__(self, nome, materia):
        self.nome = nome
        self.materia = materia



 




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

    

@app.route('/alunos')
def lista_alunos(): # função de lista de alunos em tabela
    return render_template('alunos.html', alunos=alunos.query.all())

@app.route('/cria_aluno', methods=['GET', 'POST'])
def cria_alunos(): #função para cadastro de alunos
    nome = request.form.get('nome')
    materia = request.form.get('materia')
    if request.method == 'POST':
        aluno = alunos(nome, materia)
        db.session.add(aluno)
        db.session.commit()
        return redirect(url_for('lista_alunos'))
    return render_template('novo_aluno.html')


@app.route('/cursos')
def lista_cursos(): #lista dos cursos em tabela 
    return render_template('cursos.html',cursos=cursos.query.all())


@app.route('/cria_curso', methods=['GET', 'POST'])
def cria_cursos(): #função para criar o curso
    nome = request.form.get('nome')
    descricao = request.form.get('descricao')
    ch = request.form.get('ch')
    
    if request.method == 'POST':        
        curso = cursos(nome, descricao, ch)
        db.session.add(curso)  #(.add)adinionar
        db.session.commit()   
        return redirect(url_for('lista_cursos')) #retorna para lista depois que fizer o cadastro do novo
    return render_template('novo_curso.html')


@app.route('/<int:id>/atualiza_curso', methods={"GET", "POST"})
def atualiza_curso(id):   #função para atualizar o curso
    curso = cursos.query.filter_by(id=id).first()
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        ch = request.form['ch']
       
        cursos.query.filter_by(id=id).update({'nome':nome, 'descricao':descricao, 'ch':ch}) #(.update) atualizar a tabela
        db.session.commit()
        return redirect(url_for('lista_cursos')) #retorna para lista depois que fizer atualização
    return render_template('atualiza_curso.html', curso=curso)




with app.app_context():    
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

    