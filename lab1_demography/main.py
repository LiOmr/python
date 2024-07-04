from work_with_file import load_data, filter_data
from calculate_statistics import calculate_statistics, calculate_percentiles
from visualize_data import display_table, display_statistics, display_percentiles, display_list_of_regions
import my_exceptions
# C:\Users\79263\Desktop\russian_demography.csv
# C:\Users\79263\Desktop\russian_demography — empty.csv
# C:\Users\79263\Desktop\russian_demography — неверные данные.csv
# C:\Users\79263\Desktop\russian_demography — без заголовков.csv


def main():
    file_path = input("Введите путь к CSV-файлу: ")

    try:
        expected_headers = ["year", "region", "npg", "birth_rate", "death_rate", "gdw", "urbanization"]
        dataframe = load_data(file_path, expected_headers)

        display_list_of_regions(dataframe)
        region_name = input("Введите название региона: ")
        filtered_data = filter_data(dataframe, region_name)
        display_table(filtered_data)

        column_id = input("Введите название колонки: ")


        statistics = calculate_statistics(filtered_data, column_id)
        percentiles_data = calculate_percentiles(dataframe, column_id)

        display_table(filtered_data)
        display_statistics(statistics)
        display_percentiles(percentiles_data)

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
