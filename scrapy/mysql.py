import MySQLdb
from tool import Software


class MySQL(object):

    # Create the connection object
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.passwd = "12345678"
        self.db = "RA_WEB"
        self.connect_status = 0
        self.connection = MySQLdb.connect(
            self.host, self.user, self.passwd, self.db)
        self.Connect()

    def Connect(self):
        # Create cursor and use it to execute SQL command
        self.cursor = self.connection.cursor()
        self.cursor.execute("select @@version")
        version = self.cursor.fetchone()

        if version:
            print('MySQL Running version: ', version)
            self.connect_status = 1

    def Close(self):
        self.connection.close()

    def CreateTable(self):
        self.cursor.execute("DROP TABLE IF EXISTS SoftwareInfo")
        if self.connect_status != 1:
            return
        sql = """CREATE TABLE SoftwareInfo (
                class  CHAR(30) NOT NULL,
                title  CHAR(30),
                text TEXT,  
                ref TEXT,
                header TEXT,
                description TEXT,
                bgurl TEXT,
                bginfo TEXT,
                publication TEXT)"""
        self.cursor.execute(sql)

    def Insert(self, s):
        if self.connect_status != 1:
            return
        # s = Software()
        sql = "INSERT INTO SoftwareInfo(class, title, text, ref,  header, description, bgurl, bginfo, publication) \
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)" % \
            (s.class_, s.title_, s.text_, s.ref_, s.banner__header,
             s.banner__description, s.bg_url, s.bg_info, s.publication)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except:
            self.connection.rollback()
