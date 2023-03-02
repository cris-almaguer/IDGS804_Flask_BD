from wtforms import Form
from wtforms import StringField, IntegerField, EmailField, validators

class UserForm(Form):
    id = IntegerField('id', [validators.number_range(min=1, max=20, message="Valor no valido")])
    nombre = StringField('Nombre', [validators.DataRequired(message="Valor no valido")])
    apaterno = StringField('Apellido paterno', [validators.DataRequired(message="Valor no valido")])
    email = EmailField('Email', [validators.DataRequired(message="Valor no valido"), validators.Email(message="Ingresa un correo valido")])