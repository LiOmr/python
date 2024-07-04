from tabulate import tabulate


def display_table(data):
    table = tabulate(data, headers='keys', tablefmt='psql')
    print(table)


def display_statistics(statistics):
    print("Статистические метрики:")
    for metric, value in statistics.items():
        print(f"{metric}: {value}")


def display_percentiles(percentiles):
    for percentile, value in percentiles.items():
        print(f"{percentile}: {value}")


def display_list_of_regions(data):
    regions = []
    for row in data[1:]:
        regions.append(row['region'])
    regions = set(regions)
    print(*regions, sep = "\n")