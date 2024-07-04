import csv
import os
import my_exceptions


def load_data(path, expected_headers):
        if not os.path.isfile(path):
            raise my_exceptions.FileNotFound(f"Файл '{path}' не найден.")
        file_extension = os.path.splitext(path)[1].lower()
        if file_extension != '.csv':
            raise my_exceptions.InvalidFileExtensionError("Файл должен иметь расширение .csv")

        with open(path, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = []
            deleted_rows = 0

            actual_headers = csv_reader.fieldnames

            if not any(row for row in csv_reader):
                raise my_exceptions.EmptyFileError("Файл пуст.")
            if actual_headers != expected_headers:
                raise my_exceptions.InvalidHeaderError(f"Заголовки в файле не соответствуют ожидаемым: {actual_headers}")

            csv_file.seek(0)

            for row in csv_reader:
                if all(row.values()):
                    data.append(dict(row))
                else:
                    deleted_rows += 1

            print(f"Удалено {deleted_rows} строк с пустыми полями")

        return data


def filter_data(data, region_name):
    filtered_data = [row for row in data if row['region'] == region_name]

    if not filtered_data:
        raise my_exceptions.WrongRegion(f"Регион '{region_name}' не найден в таблице.")

    return filtered_data
