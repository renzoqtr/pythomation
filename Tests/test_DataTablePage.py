from Pages.DataTablesPage import DataTablesPage
from TestData.tables_test_data import TablesTestData
from Tests.test_base import BaseTest
from Utilities.csv_reader import CsvFileReader


class TestDataTables(BaseTest):

    def test_data_table_content(self):
        test_data = CsvFileReader.read_csv(TablesTestData.CSV_CUSTOMERS, TablesTestData.CSV_DELIMITER)
        self.dataTablePage = DataTablesPage(self.driver)
        self.dataTablePage.open_data_table_page()
        table_as_text = self.dataTablePage.get_first_table_text()
        for ix in range(len(test_data)):
            data_table_row = table_as_text[ix]
            test_data_row = test_data[ix]
            for idx in range(len(test_data_row)):
                assert test_data_row[idx] == data_table_row[idx]
