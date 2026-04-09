import mysql.connector

from dao.dbConnect import dbConnect
from gestionale.core.cliente import ClienteRecord
from gestionale.core.prodotto import ProdottoRecord

# facendo connection pooling in dbConnect tutti i metodi qui dentro diventano @staticmethod
class DAO:

    @staticmethod
    def getAllProdotti():
        # creo una connessione con il database
        #cnx = mysql.connector.connect(
        #   user='root',
        #   password='programmazione',
        #   host='127.0.0.1',
        #   database='sw_gestionale')

        # invece di fare ogni volta quello supra usa questa riga sotto
        cnx = dbConnect.getConnection()     # dbConnect è senza parentesi perchè è un metodo di classe

        # creo un cursore
        cursor = cnx.cursor(dictionary = True)
        cursor.execute("Select * from prodotti")        # esegue una query SQL
        row = cursor.fetchall()  # leggiamo i dati dal cursore, sarà una lista di dizionari
        res = []    # lista dei risultati vuota
        for p in row:
            res.append(ProdottoRecord(p["nome"], p["prezzo"]))
        cursor.close()    # chiudiamo la connessione
        cnx.close()
        return res

    @staticmethod
    def getAllClienti():
        # creo una connessione con il database
        # cnx = mysql.connector.connect(
        #   user='root',
        #   password='programmazione',
        #   host='127.0.0.1',
        #   database='sw_gestionale')

        # invece di fare ogni volta quello supra usa questa riga sotto
        cnx = dbConnect.getConnection()

        # creo un cursore
        cursor = cnx.cursor(dictionary = True)
        cursor.execute("Select * from clienti")        # esegue una query SQL
        row = cursor.fetchall()  # leggiamo i dati dal cursore, sarà una lista di dizionari
        res = []    # lista dei risultati vuota
        for c in row:
            res.append(ClienteRecord(c["nome"], c["email"], c["categoria"]))
        cursor.close()    # chiudiamo la connessione
        cnx.close()
        return res

    # questi metodi sotto mi servono se per esempio mi arriva un ordine nuovo e io devo aggiomgere i prodotti e i clienti al database

    @staticmethod
    def addProdotto(prodotto):
        # creo una connessione con il database
        # cnx = mysql.connector.connect(
        #   user='root',
        #   password='programmazione',
        #   host='127.0.0.1',
        #   database='sw_gestionale')

        # invece di fare ogni volta quello supra usa questa riga sotto
        cnx = dbConnect.getConnection()

        # creo un cursore
        cursor = cnx.cursor(dictionary=True)
        query = """insert into prodotti 
                    (nome, prezzo) values (%s, %s)"""

        cursor.execute(query, (prodotto.name, prodotto.prezzo_unitario))  # esegue una query SQL

        cnx.commit()   # questo comando va a modificare il database
        cursor.close()  # chiudiamo la connessione
        cnx.close()
        return
    @staticmethod
    def addCliente(cliente):
        # creo una connessione con il database
        # cnx = mysql.connector.connect(
        #   user='root',
        #   password='programmazione',
        #   host='127.0.0.1',
        #   database='sw_gestionale')

        # invece di fare ogni volta quello supra usa questa riga sotto
        cnx = dbConnect.getConnection()

        # creo un cursore
        cursor = cnx.cursor(dictionary=True)
        query = """insert into clienti 
                    (nome, email, categoria) values (%s, %s, %s)"""

        cursor.execute(query, (cliente.nome, cliente.mail, cliente.categoria))  # esegue una query SQL

        cnx.commit()  # questo comando va a modificare il database
        cursor.close()  # chiudiamo la connessione
        cnx.close()
        return

    @staticmethod
    def hasCliente(cliente):
        # creo una connessione con il database
        # cnx = mysql.connector.connect(
        #   user='root',
        #   password='programmazione',
        #   host='127.0.0.1',
        #   database='sw_gestionale')

        # invece di fare ogni volta quello supra usa questa riga sotto
        cnx = dbConnect.getConnection()

        cursor = cnx.cursor(dictionary=True)
        query = "Select * from clienti where email = %s"
        cursor.execute(query, (cliente.mail, ))
        row = cursor.fetchall()

        cursor.close()
        cnx.close()
        return len(row) > 0

    @staticmethod
    def hasProdotto(prod):
        # creo una connessione con il database
        # cnx = mysql.connector.connect(
        #   user='root',
        #   password='programmazione',
        #   host='127.0.0.1',
        #   database='sw_gestionale')

        # invece di fare ogni volta quello supra usa questa riga sotto
        cnx = dbConnect.getConnection()

        cursor = cnx.cursor(dictionary=True)
        query = "Select * from prodotti where nome = %s"
        cursor.execute(query, (prod.name, ))
        row = cursor.fetchall()

        cursor.close()
        cnx.close()
        return len(row) > 0


if __name__ == '__main__':
    mydao = DAO()
    mydao.getAllProdotti()