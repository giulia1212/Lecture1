import pathlib

import mysql.connector


class dbConnect:
    # in questo modo non potrò creare diverse istanze della classe ma non la creo proprio, uso il metodo come metodo di classe
    # quindi senza parentesi

    def __init__(self):
        # per implementare il pattern singletone e impedire al chiamante di creare istanze di classe.
        raise RuntimeError("Attenzione non devi creare un'istanza di questa classe. Usa i metodi di classe.")

    _myPool = None

    # uso CONNECTION POOLING
    @classmethod
    def getConnection(cls):
        if cls._myPool is None:
            try:
                cls._myPool = mysql.connector.pooling.MySQLConnectionPool(
                    #user="root",
                    #password="programmazione",
                    #host="127.0.0.1",
                    #database="sw_gestionale",
                    pool_size = 3,
                    pool_name = "myPool",
                    option_files = f"{pathlib.Path(__file__).resolve().parent}/connector.cfg"
                )
                return cls._myPool.get_connection()

            except mysql.connector.Error as err:
                print("Non riesco a collegarmi al db")
                print(err)
                return None
        else:
            # allora il pool già esiste e restituisco la connessione
            return cls._myPool.get_connection()

# La versione vecchia(questa commentata) crea una connessione e la restituisce, se connessione fallisce restituisce errore
# @classmethod
# def getConnection(cls):
# try:
#   cnx = mysql.connector.connect(
#      user = "root",
#     password ="programmazione",
#         host = "127.0.0.1",
#        database = "sw_gestionale"
#    )
#   return cnx
# except mysql.connector.Error as err:
#   print("Non riesco a collegarmi al db")
#   print(err)
#  return None