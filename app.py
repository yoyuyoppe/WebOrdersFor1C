from flask import Flask, render_template, url_for, request, flash, redirect, session, logging, g, Response
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from forms import AuthForm, RegForm
from settings.app_config import CONFIG as cfg
from models.user import User
from models.news import News, getListNews

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
    return render_template('home.html', listnews = getListNews(g))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def autorization(form):
    username = str(form.username.data)
    password = str(form.password.data)

    user = User(username, password)

    if not user.exist(g):
        flash('Не верный пользователь или пароль', 'danger')
        return render_template('login.html', isReg=False, form=form)

    session['logged_in'] = True
    session['username'] = username

    return redirect("/")


def registration(form):
    username = str(form.username.data)
    # Захэшируем наши пароли. Обязательно в конфиге должен быть заполнен "SECRET_KEY"
    password = str(form.password.data)
    email = str(form.email.data)
    phone = str(form.phone.data)

    user = User(username, password, email, phone)

    try:
        user.add(g)
        session['logged_in'] = True
    except Exception as e:
        flash("Ошибка при регистрации: %s" % e, 'danger')
        return render_template('login.html', isReg=True, form=form)

    return redirect("/")


@app.route('/login/auth', methods=['GET', 'POST'], defaults={'isReg': False})
@app.route('/login/reg', methods=['GET', 'POST'], defaults={'isReg': True})
def login(isReg):
    _form = RegForm(request.form) if isReg else AuthForm(request.form)
    if request.method == 'POST':
        return registration(_form) if isReg else autorization(_form)

    return render_template('login.html', isReg=isReg, btnRegOff=not isReg, form=_form)


if __name__ == '__main__':
    app.run()
