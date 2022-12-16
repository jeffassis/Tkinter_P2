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
    trans.execute("CREATE TABLE IF NOT EXISTS aluno (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, endereco TEXT, telefone TEXT, cep TEXT, nascimento TEXT, sangue TEXT)")
    trans.persist()
    trans.disconnect()

# ADICIONA OS DADOS DO DB
def insert(nome, endereco, telefone, cep, nascimento, sangue):
    """
    -> Função que adiciona aluno a tabela
    """
    trans = TransactionObject()
    trans.connect()
    trans.execute("INSERT INTO aluno VALUES(NULL, ?,?,?,?,?,?)", (nome, endereco, telefone, cep, nascimento, sangue))
    trans.persist()
    trans.disconnect()

# VISUALIZA OS DADOS DO DB
def view():
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM aluno")
    rows = trans.fetchall()
    trans.disconnect()
    return rows

# PESQUISA DADOS NO DB
def search(param):
    trans = TransactionObject()
    trans.connect()
    trans.execute(f"SELECT * FROM aluno WHERE nome like '%{param}%'")
    rows = trans.fetchall()
    trans.disconnect()
    return rows    

# EXCLUI UM DADO DO DB
def delete(i):
    trans = TransactionObject()
    trans.connect()
    trans.execute("DELETE FROM aluno WHERE id = ?", i)
    trans.persist()
    trans.disconnect()    

# EDITA OS DADOS DO DB
def update(i):
    trans = TransactionObject()
    trans.connect()
    trans.execute("UPDATE aluno SET nome=?, endereco=?, telefone=?, cep=?, nascimento=?, sangue=? WHERE id = ?", i)
    trans.persist()
    trans.disconnect()    

# VERIFICA SE O NOME EXISTE NO DB
def search_name(param):
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM aluno WHERE nome = ?",[(param)])
    result = trans.fetchall()
    trans.disconnect()
    return result


initDB()