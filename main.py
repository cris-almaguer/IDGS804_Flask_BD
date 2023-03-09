from flask import Flask, render_template, request, redirect, url_for, jsonify
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from models import db
from models import Alumno
import forms

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.route('/', methods=['GET', 'POST'])
def index():
    create_form = forms.UserForm(request.form)
    if request.method == 'POST':
        alumno = Alumno(nombre = create_form.nombre.data, apaterno = create_form.apaterno.data, email = create_form.email.data)
        db.session.add(alumno)
        db.session.commit()
    return render_template('index.html', form = create_form)

@app.route('/abcompleto', methods=['GET', 'POST'])
def abc():
    create_form = forms.UserForm(request.form)
    #select * from alumnos
    alumnos = Alumno.query.all()
    return render_template('abcompleto.html', form = create_form, alumnos=alumnos)   

@app.route('/modificar', methods=['GET', 'POST'])
def modificar_alumno():
    create_form = forms.UserForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        # SELECT * FROM alumnos WHERE id = id
        alumno = db.session.query(Alumno).filter(Alumno.id == id).first()
        create_form.id.data = alumno.id     
        create_form.nombre.data =  alumno.nombre
        create_form.apaterno.data = alumno.apaterno
        create_form.email.data = alumno.email

    if request.method == 'POST':
        id = create_form.id.data
        alumno = db.session.query(Alumno).filter(Alumno.id==id).first()
        alumno.nombre = request.form.get('nombre')
        alumno.apaterno = request.form.get('apaterno')
        alumno.email =  request.form.get('email')
        db.session.add(alumno)
        db.session.commit()
        return redirect('/abcompleto')
    return render_template('modificar.html', form = create_form)

@app.route('/eliminar', methods=['GET', 'POST'])
def eliminar_alumno():
    id = request.args.get('id')
    alumno = db.session.query(Alumno).filter(Alumno.id==id).first()
    db.session.delete(alumno)
    db.session.commit()  
    return redirect('/abcompleto')

if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)