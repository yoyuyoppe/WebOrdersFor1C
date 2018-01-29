from wtforms import Form, StringField, TextAreaField, PasswordField, validators


class AuthForm(Form):
    username = StringField('', [validators.Length(
        min=1, max=30, message="Допустимая длина поля 30 символов")])
    password = PasswordField('', [validators.DataRequired(), validators.Length(
        min=7, max=15, message="Допустимая длина пароля от 7 до 15 символов")])
