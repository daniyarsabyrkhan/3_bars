import json
import operator
import math


def load_data(filepath):
    with open(filepath, "r") as bars:
        moscow_bars = json.load(bars)
        return moscow_bars


def get_biggest_bar(data):
    biggest_bar = (
        max(data, key=lambda idata: idata["Cells"]["SeatsCount"]))
    return biggest_bar


def get_smallest_bar(data):
    smallest_bar = (
        min(data, key=lambda idata: idata["Cells"]["SeatsCount"]))
    return smallest_bar


def get_closest_bar(data, latitude, longitude):
    def get_distance(bar):
        lon, lat = bar['Cells']['geoData']['coordinates']
        return ((lon - longitude) ** 2 + (lat - latitude) ** 2)
    return min(data, key=get_distance)


if __name__ == '__main__':
    path_for_json = input("Укажите путь до json файла:")
    latitude, longitude = map(
        float, input("Укажите координаты где вы находитесь:").split(', '))
    moscow_bars = load_data(path_for_json)
    biggest_bar = get_biggest_bar(moscow_bars)
    smallest_bar = get_smallest_bar(moscow_bars)
    closest_bar = get_closest_bar(moscow_bars, latitude, longitude)
    print ("Самый большой бар: %s" % (biggest_bar["Cells"]["Name"]))
    print ("Cамый маленький бар: %s" % (smallest_bar["Cells"]["Name"]))
    print ("Cамый близкий бар: %s" % (closest_bar["Cells"]["Name"]))
