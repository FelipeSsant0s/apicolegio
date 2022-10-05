from flask import Flask, render_template, request
app = Flask (__name__)


armazenamentos = []
registros = []

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






if __name__ == '__main__':
    app.run(debug=True)
