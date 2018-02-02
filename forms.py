from wtforms import Form, StringField, TextAreaField, TextField, PasswordField, validators


class AuthForm(Form):
    username = StringField('', [validators.Length(
        min=1, max=30, message="Допустимая длина поля 30 символов"), validators.required()])
    password = PasswordField('', [validators.DataRequired(), validators.Length(
        min=8, max=15, message="Допустимая длина пароля от 8 до 15 символов"), validators.required()])


class RegForm(Form):
    username = StringField('', [validators.Length(
        min=1, max=30, message="Допустимая длина поля 30 символов"), validators.required()])
    password = PasswordField('', [validators.DataRequired(), validators.Length(
        min=8, max=15, message="Допустимая длина пароля от 8 до 15 символов"), validators.required()])
    email = StringField('', [validators.Length(
        min=6, max=120, message="Допустимая длина поля от 6 до 120 символов"), validators.Email()])
    phone = StringField('', [validators.Length(
        min=1, max=100, message="Допустимая длина поля 50 символов")])
