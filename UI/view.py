import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab06"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_result = None
        self.__theme_switch = None
        self.dd_year = None
        self.dd_brand = None
        self.dd_retailer = None
        self.btn_sales_analysis = None
        self.btn_top_sales = None
        self.pr_ring = None

    def load_interface(self):
        # theme switch and title
        self.__theme_switch = ft.Switch(label="Dark Theme", on_change=self.theme_changed)
        self._title = ft.Text("Analizza vendite", color="blue", size=24)
        self._page.controls.append(
                ft.Row(spacing=400, controls=[self.__theme_switch, self._title,],
                       alignment=ft.MainAxisAlignment.START)
        )

        # ROW 0 with filters Dropdowns

        self.dd_year = ft.Dropdown(
                label="year",
                width=200,
                options=[ft.dropdown.Option(text="Nessun filtro",
                                            data=None)],
                hint_text="Choose a year as filter"
        )
        self._controller.populate_dd_year()
        
        self.dd_brand = ft.Dropdown(
                label="brand",
                width=200,
                options=[ft.dropdown.Option(key=None,
                                            text="Nessun filtro")],
                hint_text="Choose a brand as filter"
        )
        self._controller.populate_dd_brand()
        
        self.dd_retailer = ft.Dropdown(
                label="retailer",
                width=550,
                options=[ft.dropdown.Option(text="Nessun filtro",
                                            data=None)],
                hint_text="Choose a retailer as filter"
        )
        self._controller.populate_dd_retailer()
        
        row0 = ft.Row([self.dd_year, self.dd_brand, self.dd_retailer],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row0)
        
        # ROW 1 with actions' buttons
        
        self.btn_top_sales = ft.ElevatedButton(
                text="Top sales",
                on_click=self._controller.handle_top_sales,
                tooltip="Searches the top 5 sales based on selected filters"
        )

        self.btn_sales_analysis = ft.ElevatedButton(
                text="sales analysis",
                on_click=self._controller.handle_sales_analysis,
                tooltip="Analyzes sales based on selected filters"
        )

        self.pr_ring = ft.ProgressRing(visible=False)

        row1 = ft.Row([self.btn_top_sales, self.btn_sales_analysis, self.pr_ring],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self._page.theme_mode = (
            ft.ThemeMode.LIGHT
            if self._page.theme_mode == ft.ThemeMode.DARK
            else ft.ThemeMode.DARK
        )
        self.__theme_switch.label = (
            "Light theme" if self._page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.update_page()
