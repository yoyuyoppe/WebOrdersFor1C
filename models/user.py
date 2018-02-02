class User():

    def __init__(self, username, password, email="", phone=""):
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone

    def exist(self, g):
        valid = False

        if not hasattr(g, 'mysql_db'):
            return valid

        cur = g.mysql_db.cursor()

        cur.execute(
            "select * from users where username = %s and password = %s", (self.username, self.password))

        rows = cur.fetchall()

        if rows != ():
            valid = True

        return valid

    def add(self, g):
        if not hasattr(g, 'mysql_db'):
            raise "Отсутствует подключение к базе данных"

        cur = g.mysql_db.cursor()

        cur.execute("INSERT INTO users(username, password, email, phone) VALUES(%s, %s, %s, %s)",
                    (self.username, self.password, self.email, self.phone))

        g.mysql_db.commit()           
