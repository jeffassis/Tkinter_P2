import sqlite3 as lite

class TransactionObject():
    database = "dados.db"
    con = None
    cur = None
    connected = False

    def connect(self):
        TransactionObject.con = lite.connect(TransactionObject.database)
        TransactionObject.cur = TransactionObject.con.cursor()
        TransactionObject.connected = True

    def disconnect(self):
          TransactionObject.con.close()
          TransactionObject.connected = False

    def execute(self, lite, parms = None):
        if TransactionObject.connected:
            if parms == None:
                TransactionObject.cur.execute(lite)
            else:
                TransactionObject.cur.execute(lite, parms)
            return True
        else:
            return False

    def fetchall(self):
        return TransactionObject.cur.fetchall()

    def persist(self):
        if TransactionObject.connected:
            TransactionObject.con.commit()
            return True
        else:
            return False

def initDB():
    trans = TransactionObject()
    trans.connect()
    trans.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, senha TEXT)")
    trans.persist()
    trans.disconnect()

def logar(param1, param2):
    trans =TransactionObject()
    trans.connect()
    find_user = ('SELECT * FROM user WHERE nome = ? and senha = ?')
    trans.execute(find_user, [(param1), (param2)])
    result = trans.fetchall()
    return result

# INCIANDO CONEXAO
initDB()