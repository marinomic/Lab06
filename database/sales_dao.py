from database.DB_connect import DBConnect
from model.sale import Sale


def get_years() -> list | None:
    """
    Funzione che restituisce tutti gli anni presenti dal database estraendoli dalla colonna date
    di go_daily_sales
    """
    cnx = DBConnect.get_connection()
    query = """
    SELECT DISTINCT YEAR(gds.Date)
    FROM go_daily_sales AS gds"""
    if cnx is not None:
        cursor = cnx.cursor()
        cursor.execute(query)
        years = cursor.fetchall()
        cursor.close()
        cnx.close()
        return years
    else:
        print("Could not connect")
        return None


def get_top_sales(year, brand, retailer):
    """
    Funzione che restituisce le prime 5 vendite del database, filtrate per anno, brand e retailer
    """
    cnx = DBConnect.get_connection()
    query = f"""
    SELECT *
    FROM go_daily_sales AS gds
    WHERE YEAR(gds.Date) = {year}
    AND gds.Product_number IN (SELECT p.Product_number
                               FROM go_products AS p
                               WHERE p.Product_brand = '{brand}')
    AND gds.Retailer_code = {retailer.retailer_code}
    ORDER BY gds.Unit_sale_price * gds.Quantity DESC
    LIMIT 5"""
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query)
        sales = cursor.fetchall()
        result = set()
        for row in sales:
            sale = Sale(row["Date"],
                        row["Quantity"],
                        row["Unit_price"],
                        row["Unit_sale_price"],
                        row["Retailer_code"],
                        row["Product_number"],
                        row["Order_method_code"])
            result.add(sale)
    else:
        print("Could not connect")
        return None
