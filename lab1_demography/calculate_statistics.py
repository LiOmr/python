import numpy as np
import my_exceptions

def calculate_statistics(data, column_id):
    try:
        column_data = []
        for row in data:
            try:
                value = float(row[column_id])
                column_data.append(value)
            except ValueError:
                raise my_exceptions.InvalidDataError("Данные должны быть представлены в численном виде.")

        statistics = {
            'Maximum': np.max(column_data),
            'Minimum': np.min(column_data),
            'Median': np.median(column_data),
            'Average': np.mean(column_data)
        }

        return statistics
    except my_exceptions.InvalidDataError as e:
        raise e


def calculate_percentiles(data, column_id):
    try:
        column_data = []
        for i, row in enumerate(data):
            if i == 0:
                continue
            try:
                value = float(row[column_id])
                column_data.append(value)
            except ValueError:
                print(f"Проблемное значение в строке {i+1}: {row[column_id]}")
                print("Продолжаем анализ...")
                raise my_exceptions.InvalidDataError("Данные должны быть представлены в численном виде.")

        sorted_data = sorted(column_data)

        percentiles = {}
        for percentile in range(5, 101, 5):
            value = np.percentile(sorted_data, percentile)
            percentiles[f'Percentile {percentile}%'] = value

        return percentiles
    except my_exceptions.InvalidDataError as e:
        raise e
