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
    trans.execute("CREATE TABLE IF NOT EXISTS funcionario (id INTEGER PRIMARY KEY AUTOINCREMENT, cpf TEXT, nome TEXT, endereco TEXT, email TEXT, telefone TEXT, nascimento TEXT, funcao TEXT, disciplina TEXT)")
    trans.persist()
    trans.disconnect()

# ADICIONA OS DADOS DO DB
def insert(cpf, nome, endereco, email, telefone, nascimento, funcao, disciplina):
    trans = TransactionObject()
    trans.connect()
    trans.execute("INSERT INTO funcionario VALUES(NULL, ?,?,?,?,?,?,?,?)", (cpf, nome, endereco, email, telefone, nascimento, funcao, disciplina))
    trans.persist()
    trans.disconnect()

# VISUALIZA OS DADOS DO DB
def view():
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM funcionario")
    rows = trans.fetchall()
    trans.disconnect()
    return rows

# PESQUISA DADOS NO DB
def search(param):
    trans = TransactionObject()
    trans.connect()
    trans.execute(f"SELECT * FROM funcionario WHERE nome like '%{param}%'")
    rows = trans.fetchall()
    trans.disconnect()
    return rows

# EXCLUI UM DADO DO DB
def delete(i):
    trans = TransactionObject()
    trans.connect()
    trans.execute("DELETE FROM funcionario WHERE id = ?", i)
    trans.persist()
    trans.disconnect()

# EDITA OS DADOS DO DB
def update(i):
    trans = TransactionObject()
    trans.connect()
    trans.execute("UPDATE funcionario SET cpf=?, nome=?, endereco=?, email=?, telefone=?, nascimento=?, funcao=?, disciplina=? WHERE id = ?", i)
    trans.persist()
    trans.disconnect()

# VERIFICA SE O NOME EXISTE NO DB
def search_name(param):
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM funcionario WHERE nome = ?",[(param)])
    result = trans.fetchall()
    trans.disconnect()
    return result

# INCIANDO CONEXAO
initDB()