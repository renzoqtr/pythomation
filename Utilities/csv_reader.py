import csv

from Config.config import TestConfig


class CsvFileReader:

    def read_csv(file_path):
        with open(file_path) as csv_file:
            table = []
            csv_reader = csv.reader(csv_file, delimiter=TestConfig.CSV_DELIMITER)
            next(csv_reader)
            for row in csv_reader:
                table.append(row)
        return table
