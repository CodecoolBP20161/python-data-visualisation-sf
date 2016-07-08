import psycopg2


class Database(object):

    def __init__(self, dbname, user, password):
        self.dbname = dbname
        self.user = user
        self.password = password

    def connect(self):
        connect_str = "dbname=%s user=%s host='localhost' password=%s" % (
            self.dbname, self.user, self.password)
        return psycopg2.connect(connect_str)

    def execute(self, sql_command):
        cursor = self.connect().cursor()
        try:
            cursor.execute("""%s""" % (sql_command))
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print("PROBLEM!!!!")
            print(e)

mydb = Database(input('What is your database name? '), input('What is your user name? '),
                   input('What is your password? '))