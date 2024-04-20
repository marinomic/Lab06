import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._retailer = None
        self._brand = None
        self._year = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def populate_dd_year(self):
        for year in self._model.get_years():
            self._view.dd_year.options.append(ft.dropdown.Option(key=year[0],
                                                                 text=year[0],
                                                                 data=year[0],
                                                                 on_click=self.read_year))
        self._view.update_page()

    def read_year(self, e):
        """Event handler che legge l'anno scelto dal menu a tendina ogniqualvolta viene cambiata
        la scelta, e lo memorizza in una variabile di istanza. L'anno è un intero, se si tratta di un anno,
        oppure un None se viene scelta l'opzione nessun filtro sull'
        anno"""
        self._year = e.control.data
        # self._view.txt_result.controls.append(ft.Text(f"Anno scelto: {self._year}"))
        # self._view.update_page()

    def populate_dd_brand(self):
        for brand in self._model.get_brands():
            self._view.dd_brand.options.append(ft.dropdown.Option(key=brand[0],
                                                                  text=brand[0],
                                                                  data=brand[0],
                                                                  on_click=self.read_brand))
        self._view.update_page()

    def read_brand(self, e):
        """Event handler che legge il brand scelto dal menu a tendina ogniqualvolta viene cambiata
            la scelta, e lo memorizza in una variabile di istanza. Il brand è una stringa, se si tratta di un brand,
            oppure un None se viene scelta l'opzione nessun filtro sul brand"""
        # if e.control.data == "None":
        #     self._brand = None
        # else:
        self._brand = e.control.data
        # self._view.txt_result.controls.append(ft.Text(f"Brand scelto: {self._brand}"))
        # self._view.update_page()

    def populate_dd_retailer(self):
        retailers = self._model.get_retailers()
        for retailer in retailers:
            self._view.dd_retailer.options.append(ft.dropdown.Option(key=retailer.retailer_code,
                                                                     text=retailer.retailer_name,
                                                                     data=retailer,
                                                                     on_click=self.read_retailer))
        self._view.update_page()

    def read_retailer(self, e):
        """Event handler che legge il retailer scelto dal menu a tendina ogniqualvolta viene cambiata
            la scelta, e lo memorizza in una variabile di istanza. Il retailer è un oggetto Retailer, se si tratta di un retailer,
            oppure un None se viene scelta l'opzione nessun filtro sul retailer"""
        self._retailer = e.control.data
        # if self.read_retailer == "Nessun filtro":
        #     # Set the selected value to an empty string
        #     self._view.dd_retailer.value = ""
        #     self._view.dd_retailer.update()
        # else:
        #     self._view.txt_result.controls.append(ft.Text(f"Retailer scelto: {self.read_retailer.retailer_name}"))
        #     self._view.update_page()

    def handle_top_sales(self, e):
        self._view.pr_ring.visible = True
        self._view.btn_top_sales.disabled = True
        self._view.btn_sales_analysis.disabled = True
        self._view.update_page()
        top_sales = self._model.get_top_sales(self._year, self._brand, self._retailer)
        self._view.pr_ring.visible = False
        self._view.btn_top_sales.disabled = False
        self._view.btn_sales_analysis.disabled = False
        self._view.txt_result.controls.clear()
        if len(top_sales) == 0:
            self._view.txt_result.controls.append(ft.Text("No sales found"))
        else:
            for sale in top_sales:
                self._view.txt_result.controls.append(ft.Text(sale))
        self._view.update_page()

    def handle_sales_analysis(self, e):
        pass
