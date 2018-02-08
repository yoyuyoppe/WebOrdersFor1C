class News():

    def __init__(self, title, content):
        self.title = title
        self.content = content

    @staticmethod
    def getListNews(g):
        listnews = []
        if not hasattr(g, 'mysql_db'):
            return listnews

        cur = g.mysql_db.cursor()

        result = cur.execute('select * from news')

        listnews = cur.fetchall()

        return listnews
