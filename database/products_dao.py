from database.DB_connect import DBConnect
from model.product import Product


def get_brands():
    """
    Funzione che restituisce tutti i brand presenti nel database estraendoli dalla colonna Product_brand
    di go_products
    """
    cnx = DBConnect.get_connection()
    query = """
    SELECT DISTINCT gp.Product_brand
    FROM go_products AS gp"""
    if cnx is not None:
        cursor = cnx.cursor()
        cursor.execute(query)
        brands = cursor.fetchall()
        cursor.close()
        cnx.close()
        return brands
    else:
        print("Could not connect")
        return None
