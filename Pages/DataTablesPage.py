from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class DataTablesPage(BasePage):
    DATA_TABLE_URL = "https://the-internet.herokuapp.com/tables"
    FIRST_TABLE_ROWS = (By.CSS_SELECTOR, '#table1 > tbody > tr')

    def __init__(self, driver):
        super().__init__(driver)

    def open_data_table_page(self):
        self.driver.get(self.DATA_TABLE_URL)

    def get_first_table_text(self):
        text_table = []
        rows = self.get_elements(self.FIRST_TABLE_ROWS)
        for row in rows:
            row_text = []
            columns = row.find_elements(By.CSS_SELECTOR, 'td')
            for column in columns:
                row_text.append(column.text)
            text_table.append(row_text)
        return text_table
