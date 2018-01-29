class User():

    def __init__(self, username, password, email=""):
        self.username = username
        self.password = password
        self.email = str(email).strip

    def exist(self, g):
        valid = False

        if not hasattr(g, 'mysql_db'):
            return valid

        cur = g.mysql_db.cursor()

        print("select * from users where username = %s and password = %s",
              (self.username, self.password))
        cur.execute(
            "select * from users where username = %s and password = %s", (self.username, self.password))

        rows = cur.fetchall()
        print(rows)

        if rows != ():
            valid = True

        return valid
