from database import sales_dao, products_dao, retailers_dao


class Model:
    def get_years(self):
        return sales_dao.get_years()

    def get_brands(self):
        return products_dao.get_brands()

    def get_retailers(self):
        return retailers_dao.get_retailers()

    def get_top_sales(self, year, brand, retailer):
        return sales_dao.get_top_sales(year, brand, retailer)
