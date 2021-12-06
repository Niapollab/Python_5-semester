import requests
from typing import Iterable
from datetime import *
from bs4 import BeautifulSoup
import json

DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0"
}
GISMETEO_URL = "https://www.gismeteo.ru"


class City:
    __id: str
    __name: str
    __district: str
    __sub_district: str
    __country: str

    def __init__(self, id: str, name: str, district: str, sub_district: str, country: str):
        self.__id = id
        self.__name = name
        self.__district = district
        self.__sub_district = sub_district
        self.__country = country

    @property
    def fullname(self) -> str:
        isnt_null = filter(lambda x: x is not None, [self.__name, self.__sub_district, self.__district, self.__country])
        return ", ".join(isnt_null)

    @property
    def id(self) -> str:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def district(self) -> str:
        return self.__district

    @property
    def sub_district(self) -> str:
        return self.__sub_district

    @property
    def country(self) -> str:
        return self.__country


class Weather:
    __day: date
    __name: str
    __max_per_day: int
    __min_per_day: int

    def __init__(self, day: date, name: str, max_per_day: int, min_per_day: int) -> None:
        self.__day = day
        self.__name = name
        self.__max_per_day = max_per_day
        self.__min_per_day = min_per_day

    @property
    def day(self) -> str:
        return self.__day

    @property
    def name(self) -> str:
        return self.__name

    @property
    def max_per_day(self) -> int:
        return self.__max_per_day

    @property
    def min_per_day(self) -> int:
        return self.__min_per_day


def find_cities_by_name(city_name: str) -> list[City]:
    response_url = f"{GISMETEO_URL}/api/v2/search/searchresultforsuggest/{city_name}"
    payload = {
        "lang": "ru",
        "domain": "ru"
    }
    request = requests.get(response_url, params=payload,
                           headers=DEFAULT_HEADERS)
    request_data = json.loads(request.text)
    return [City(item['url'].replace('/', ''), item['name'], item['district']['name'] if item['district'] else None, item['subDistrict']['name'] if item['subDistrict'] else None, item['country']['name'] if item['country'] else None) for item in request_data['items']]


def enumerate_days(start_date: date, count: int) -> Iterable[date]:
    for _ in range(count):
        yield start_date
        start_date += timedelta(days=1)


def get_weather_per_10_days(city_id: int) -> list[Weather]:
    response_url = f"{GISMETEO_URL}/{city_id}/10-days/"
    request = requests.get(response_url, headers=DEFAULT_HEADERS)
    text = request.text

    dates = enumerate_days(datetime.now().date(), 10)

    soup = BeautifulSoup(text, "html.parser")

    forecast_block = soup.find("div", class_="forecast_frame")

    weather_icons_block = forecast_block.find("div", "widget__row_icon")
    weather_names_tooltips = map(lambda x: x.attrs["data-text"].replace(
        "\xa0", " "), weather_icons_block.findAll("span", "tooltip"))

    weather_temperature_block = forecast_block.find(
        "div", "widget__row_temperature")
    weather_temperature_maxts = (int(maxt.find("span", "unit unit_temperature_c").text.replace(
        u'\u2212', "-")) for maxt in weather_temperature_block.findAll("div", "maxt"))
    weather_temperature_mints = (int(mint.find("span", "unit unit_temperature_c").text.replace(
        u'\u2212', "-")) for mint in weather_temperature_block.findAll("div", "mint"))

    raw_weather = list(zip(dates, weather_names_tooltips,
                        weather_temperature_maxts, weather_temperature_mints))
    return [Weather(raw_weather[0], raw_weather[1], raw_weather[2], raw_weather[3]) for raw_weather in raw_weather]
