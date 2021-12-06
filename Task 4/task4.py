import sys
from console_utils import *
from weather_utils import *


def print_forecast(weather: Iterable[Weather]):
    for w in weather:
        print(f'{datetime.strftime(w.day, "%A (%d %B %Y)")}: ')
        print(f"Погода: {w.name}")
        print(f"Максимальная температура: {w.max_per_day}")
        print(f"Минимальная температура: {w.min_per_day}")
        print()


def main(argv):
    while True:
        city_name = input("Введите название города: ")
        cities = find_cities_by_name(city_name)

        if len(cities) < 1:
            print(f"Не удалось найти города с названием \"{city_name}\".")
            pause()
            clear()
            continue
        
        index = 0
        if len(cities) > 1:
            index = read_menu_item("Найденные города: ", [city.fullname for city in cities])
            clear()

        weather = get_weather_per_10_days(cities[index].id)
        print_forecast(weather)
        break

    return 0


if __name__ == "__main__":
    main(sys.argv)
