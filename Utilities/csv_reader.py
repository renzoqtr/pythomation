import csv


class CsvFileReader:

    def read_csv(file_path, separator):
        with open(file_path) as csv_file:
            table = []
            csv_reader = csv.reader(csv_file, delimiter=separator)
            next(csv_reader)
            for row in csv_reader:
                table.append(row)
        return table
