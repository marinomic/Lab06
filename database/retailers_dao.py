from database.DB_connect import DBConnect
from model.retailer import Retailer


def get_retailers():
    """
    Funzione che restituisce una lista di oggetti di tipo Retailer presenti nel database estraendoli dalla tabella go_retailers
    """
    cnx = DBConnect.get_connection()
    query = """
    SELECT *
    FROM go_retailers"""
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query)
        result = set()
        for row in cursor.fetchall():
            read_retailer = Retailer(row["Retailer_code"],
                                     row["Retailer_name"],
                                     row["Type"],
                                     row["Country"])
            result.add(read_retailer)
        cursor.close()
        cnx.close()
        # per ogni riga della tabella go_retailers, creo un oggetto di tipo Retailer
        return result

    else:
        print("Could not connect")
        return None
