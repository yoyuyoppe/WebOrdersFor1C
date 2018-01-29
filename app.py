from flask import Flask, render_template, url_for, request, flash, redirect, session, logging, g, Response
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from forms import AuthForm
from settings.app_config import CONFIG as cfg
from models.user import User

app = Flask(__name__)
# Обновим по ключу необходимые настройки конфига
app.config.update(cfg)
# Инициализируем объект mysql для работы с БД
mysql = MySQL(app)


@app.before_request
def before_request():
    # Перед обработкой запроса создадим активное соединение с MySql
    if not hasattr(g, 'mysql_db'):
        g.mysql_db = mysql.connection


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/auth', methods=['GET', 'POST'])
def auth():
    import controllers.users_controller as users_controller
    _form = AuthForm(request.form)
    if request.method == 'POST' and _form.validate():
        # Получаем данные с формы авторизации
        username = str(_form.username.data)
        # Захэшируем наши пароли. Обязательно в конфиге должен быть заполнен "SECRET_KEY"
        #password = sha256_crypt.encrypt(str(_form.password.data))
        password = str(_form.password.data)

        user = User(username, password)

        if not user.exist(g):
            flash('Не верный пользователь или пароль', 'danger')
            return render_template('auth.html', form=_form)
    
        return redirect('/')

    return render_template('auth.html', form=_form)


if __name__ == '__main__':
    app.run()
