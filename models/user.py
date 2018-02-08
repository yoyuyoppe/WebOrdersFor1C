from passlib.hash import sha256_crypt

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

        result = cur.execute("SELECT * FROM users WHERE username = %s", [self.username])

        if result > 0:
            data = cur.fetchone()
            password = data['password']
            
            valid = sha256_crypt.verify(self.password, password)

        return valid

    def add(self, g):
        if not hasattr(g, 'mysql_db'):
            raise "Отсутствует подключение к базе данных"

        cur = g.mysql_db.cursor()

        cur.execute("INSERT INTO users(username, password, email, phone) VALUES(%s, %s, %s, %s)",
                    (self.username, sha256_crypt.encrypt(self.password), self.email, self.phone))

        g.mysql_db.commit()           
