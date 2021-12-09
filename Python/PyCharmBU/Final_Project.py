# Program: OpenWeatherMap - Weather Forecast
# Purpose: Webservice program to output weather forecast data for requested city/zip.
# Developer: Patrick Weatherford
# Week 10 - Course Project
# DSC 510 T301 - Intro to Programming
# Bellevue University - Professor Michael Eller

# API Key = 7691d4d4070cca8bd0f78ab6b1f79ec6

import requests
import json
import IPython
from urllib.parse import urlparse
from requests.exceptions import HTTPError
from datetime import datetime
from geopy.geocoders import Nominatim

nl = '\n'
tab = '\t'
dash = '-'
degree = u"\N{DEGREE SIGN}"


# try to connect to url and get http response back
def url_connect_msg(url, param_dict):
    try:
        response = requests.request("GET", url, params=param_dict)
        response.raise_for_status()
    except HTTPError as http_error:
        connect_msg = {
            'msg':f"Connection failed! {http_error}"
            , 'continue':'N'
        }
        return connect_msg
    except Exception as other_error:
        connect_msg = {
            'msg':"Connection failed for unknown reason!"
            , 'continue':'N'
        }
        return connect_msg
    else:
        connect_msg = {
            'msg':"Connected successfully!"
            , 'continue':'Y'
        }
        return connect_msg


# get 5 digit zip code
def zip_param():
    zip_code = input('Enter 5 digit zip code: ')
    try:  # if not 5 digits long or cannot convert to int then raise exception
        if len(zip_code) != 5:
            raise Exception
        else:
            int(zip_code)
    except:  # if not 5 digits and int, loop to get input until valid zip code returned
        while True:
            zip_code = input(f"{zip_code} is invalid! Please enter valid 5 digit zip code: ")
            try:
                if len(zip_code) != 5:
                    raise Exception
                else:
                    int(zip_code)
            except:
                continue
            else:
                zip_code = int(zip_code)
                break
    else:
        zip_code = int(zip_code)

    dic = {
        'cz':'zip'
        , 'value':zip_code
    }
    return dic


def city_param():
    city = input('Enter city: ')
    state = input(f'(Optional) Enter U.S. state abbreviation or press enter to continue: ')

    while city is None or city == '':
        city = input('No city entered! Enter city to search for: ')
    if state is None or state == '':
        pass
    else:
        state = ',US-' + state.upper()
    city = city+state

    dic = {
        'cz':'city'
        , 'value':city
    }
    return dic


# get input to determine if weather lookup will be by city or zip and then get url parameter values
def city_zip():
    cz = input('Search by (C)ity or (Z)ip?')
    while True:
        if cz.lower() not in ['city','zip','c','z']:
            cz = input(f"{cz} is invalid, search by (C)ity or (Z)ip?")
        else:
            cz = cz.lower()
            break
    # if searching by zip, get valid zip code entry
    if cz in ['zip','z']:
        cz_param = zip_param()
    # if searching by city, get valid city with optional country/state code
    else:
        cz_param = city_param()
    return cz_param


def unit_param():
    unit_value = 'imperial'
    unit = input(f'''Enter number below to display weather measures/temperature
    {tab}(1) Metric/Celsius
    {tab}(2) Imperial/Fahrenheit
    {tab}(3) Standard/Kelvin
    ''')

    while unit not in ['1','2','3']:
        unit = input(f'''Invalid entry! Enter number below to display weather measures/temperature
        {tab}(1) Metric/Celsius
        {tab}(2) Imperial/Fahrenheit
        {tab}(3) Standard/Kelvin
        ''')
        continue

    if unit == '1':
        unit_value = 'metric'
    elif unit == '2':
        unit_value = 'imperial'
    elif unit == '3':
        unit_value = 'standard'
    else:
        unit_value = 'imperial'

    return unit_value


def weather_data(url, param_dict):
    response = requests.request("GET", url, params=param_dict)
    json_text = response.text
    json_load = json.loads(json_text)
    weather_data_dict = {}
    if json_load.get("coord") is not None:
        lat = json_load.get("coord").get("lat")
        lon = json_load.get("coord").get("lon")
        weather_data_dict["lat"] = lat
        weather_data_dict["lon"] = lon
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.reverse(str(lat)+","+str(lon))
        address = location.raw["address"]
        weather_data_dict["state"] = address.get("state", None)
        weather_data_dict["country"] = address.get("country", None)

    else:
        weather_data_dict["lat"] = None
        weather_data_dict["lon"] = None
        weather_data_dict["state"] = None

    if json_load.get("weather") is not None:
        weather_data_dict["description"] = json_load.get("weather")[0].get("description")
        weather_data_dict["icon"] = json_load.get("weather")[0].get("icon")
    else:
        weather_data_dict["description"] = None
        weather_data_dict["icon"] = None

    if json_load.get("main") is not None:
        weather_data_dict["temp"] = json_load.get("main").get("temp")
        weather_data_dict["feels_like"] = json_load.get("main").get("feels_like")
        weather_data_dict["pressure"] = json_load.get("main").get("pressure")
        weather_data_dict["humidity"] = json_load.get("main").get("humidity")
    else:
        weather_data_dict["temp"] = None
        weather_data_dict["feels_like"] = None
        weather_data_dict["pressure"] = None
        weather_data_dict["humidity"] = None

    if json_load.get("wind") is not None:
        weather_data_dict["wind_speed"] = json_load.get("wind").get("speed")
        weather_data_dict["wind_direct"] = wind_direction(json_load.get("wind").get("deg"))
        weather_data_dict["wind_gust"] = json_load.get("wind").get("gust")
    else:
        weather_data_dict["wind_speed"] = None
        weather_data_dict["wind_direct"] = None
        weather_data_dict["wind_gust"] = None

    if json_load.get("clouds") is not None:
        weather_data_dict["cloud_percent"] = json_load.get("clouds").get("all")
    else:
        weather_data_dict["cloud_percent"] = None

    if json_load.get("rain") is not None:
        weather_data_dict["rain_1hr"] = json_load.get("rain").get("1h")
        weather_data_dict["rain_3hr"] = json_load.get("rain").get("3h")
    else:
        weather_data_dict["rain_1hr"] = None
        weather_data_dict["rain_3hr"] = None

    if json_load.get("snow") is not None:
        weather_data_dict["snow_1hr"] = json_load.get("snow").get("1h")
        weather_data_dict["snow_3hr"] = json_load.get("snow").get("3h")
    else:
        weather_data_dict["snow_1hr"] = None
        weather_data_dict["snow_3hr"] = None

    if json_load.get("dt") is not None:
        weather_data_dict["dt"] = datetime.fromtimestamp(json_load.get("dt"))
    else:
        weather_data_dict["dt"] = None

    if json_load.get("name") is not None:
        weather_data_dict["city_name"] = json_load.get("name")
    else:
        weather_data_dict["city_name"] = None

    if json_load.get("sys") is not None:
        weather_data_dict["country_code"] = json_load.get("sys").get("country")
        weather_data_dict["sunrise"] = datetime.fromtimestamp(json_load.get("sys").get("sunrise"))
        weather_data_dict["sunset"] = datetime.fromtimestamp(json_load.get("sys").get("sunset"))
    else:
        weather_data_dict["country_code"] = None
        weather_data_dict["sunrise"] = None
        weather_data_dict["sunset"] = None

    return weather_data_dict


def wind_direction(degree):
    if 348.75 <= degree < 11.25:
        direction = 'N'
    elif 11.25 <= degree < 33.75:
        direction = 'NNE'
    elif 33.75 <= degree < 56.25:
        direction = 'NE'
    elif 56.25 <= degree < 78.75:
        direction = 'ENE'
    elif 78.75 <= degree < 101.25:
        direction = 'E'
    elif 101.25 <= degree < 123.75:
        direction = 'ESE'
    elif 123.75 <= degree < 146.25:
        direction = 'SE'
    elif 146.25 <= degree < 168.75:
        direction = 'SSE'
    elif 168.75 <= degree < 191.25:
        direction = 'S'
    elif 191.25 <= degree < 213.75:
        direction = 'SSW'
    elif 213.75 <= degree < 236.25:
        direction = 'SW'
    elif 236.25 <= degree < 258.75:
        direction = 'WSW'
    elif 258.75 <= degree < 281.25:
        direction = 'W'
    elif 281.25 <= degree < 303.75:
        direction = 'WNW'
    elif 303.75 <= degree < 326.25:
        direction = 'NW'
    elif 326.25 <= degree < 348.75:
        direction = 'NNW'
    elif degree == 0:
        direction = '*No wind'
    else:
        direction = '*Unspecified'
    return direction


def url_params(api_key):
    param_dict = {
        'APPID':api_key
        , 'mode':'json'
    }

    cz_param = city_zip()
    unit_value = unit_param()

    if cz_param['cz'] == 'zip':
        param_dict['zip'] = cz_param['value']  # if searching by zip, insert zip code entered into url params dict
    else:
        param_dict['q'] = cz_param['value']  # if searching by city, insert city info into url params dict

    param_dict['units'] = unit_value

    return param_dict


def connect_retry(url, api_key):
    try_again = 'y'
    param_dict = url_params(api_key)  # get url parameters from url parameter function

    connect_msg_dict = url_connect_msg(url, param_dict)
    connect_msg = connect_msg_dict['msg']
    connect_continue = connect_msg_dict['continue']

    while connect_continue == 'N':
        print(f"{connect_msg}{nl}")
        try_again = input('Try again? (Y/N): ').lower()
        while try_again not in ['n','y','no','yes']:
            try_again = input('Invalid entry! Retry searching? (Y/N): ').lower()
        if try_again in ['y','yes']:
            param_dict = url_params(api_key)
            connect_msg = connect_msg_dict['msg']
            connect_continue = connect_msg_dict['continue']
            break
        elif try_again in ['n','no']:
            break
        else:
            continue

    retry_dict = {
        'try_again':try_again
        , 'connect_msg':connect_msg
    }

    connect_dict = {
        'retry_dict':retry_dict
        , 'param_dict':param_dict
    }
    return connect_dict


def pretty_print(url, param_dict):
    data_dict = weather_data(url, param_dict)

    if param_dict['units'] == 'metric':
        temp_unit = f"{degree}C"
    elif param_dict['units'] == 'imperial':
        temp_unit = f"{degree}F"
    else:
        temp_unit = f"{degree}K"

    if param_dict['units'] == 'imperial':
        speed_unit = "mph"
    else:
        speed_unit = "m/s"

    city_name = data_dict["city_name"]
    state = data_dict["state"]
    country = data_dict["country"]
    temp = data_dict["temp"]
    lat = data_dict["lat"]
    lon = data_dict["lon"]
    desc = data_dict["description"]
    feels_like = data_dict["feels_like"]
    pressure = data_dict["pressure"]
    if pressure is None:
        pressure = '*Unspecified'
    else:
        pressure = str(pressure) + ' hPa'
    humidity = data_dict["humidity"]
    if humidity is None:
        humidity = '*Unspecified'
    else:
        humidity = str(humidity) + '%'
    wind_speed = data_dict["wind_speed"]
    if wind_speed is None:
        wind_speed = '*Unspecified'
    else:
        wind_speed = str(wind_speed) + ' ' + speed_unit
    if data_dict["wind_direct"] is None:
        wind_direction = '*Unspecified'
    else:
        wind_direction = data_dict["wind_direct"]
    wind_gust = data_dict["wind_gust"]
    if wind_gust is None:
        wind_gust = '*Unspecified'
    else:
        wind_gust = str(wind_gust) + ' ' + speed_unit
    cloud_percent = data_dict["cloud_percent"]
    if cloud_percent is None:
        cloud_percent = '*Unspecified'
    else:
        cloud_percent = str(cloud_percent) + '%'
    rain_1hr = data_dict["rain_1hr"]
    if rain_1hr is None:
        rain_1hr = '*Unspecified'
    else:
        rain_1hr = str(rain_1hr) + ' mm'
    rain_3hr = data_dict["rain_3hr"]
    if rain_3hr is None:
        rain_3hr = '*Unspecified'
    else:
        rain_3hr = str(rain_3hr) + ' mm'
    snow_1hr = data_dict["snow_1hr"]
    if snow_1hr is None:
        snow_1hr = '*Unspecified'
    else:
        snow_1hr = str(snow_1hr) + ' mm'
    snow_3hr = data_dict["snow_3hr"]
    if snow_3hr is None:
        snow_3hr = '*Unspecified'
    else:
        snow_3hr = str(snow_3hr) + ' mm'
    dt = data_dict["dt"]
    sunrise = data_dict["sunrise"]
    sunset = data_dict["sunset"]

    data_header = f"Weather data for {city_name}"
    if data_dict["state"] is not None:
        data_header = data_header + "," + state
    else:
        data_header = data_header
    if data_dict["country"] is not None:
        data_header = data_header + f" {country}"
    else:
        data_header = data_header
    header_width = len(data_header)

    print(f"{dash*header_width}{nl}{data_header: ^}{nl}{dash*header_width}{nl}")
    print(f"Latitue: {lat}")
    print(f"Longitude: {lon}")
    print(f"Sunrise: {sunrise}")
    print(f"Sunset: {sunset}{nl}")

    print(f"Current weather: {desc.title()}")
    print(f"Current temp: {temp}{temp_unit}")
    print(f"Feels like: {feels_like}{temp_unit}")
    print(f"Cloud coverage: {cloud_percent}")
    print(f"Humidity: {humidity}")
    print(f"Pressure: {pressure}")
    print(f"Wind speed: {wind_speed}")
    print(f"Wind direction: {wind_direction}")
    print(f"Rain in last hour: {rain_1hr}")
    print(f"Rain in last 3hrs: {rain_3hr}")
    print(f"Snow in last hour: {snow_1hr}")
    print(f"Snow in last 3hrs: {snow_3hr}")
    print(f"{nl}")


def another_search():
    again = input('Do you want to search for another city? (Y/N): ')
    while again.lower() not in ['n','no','y','yes']:
        input('Invalid entry! Search for another city? (Y/N)')
        continue
    return again


def main():
    api_key = '7691d4d4070cca8bd0f78ab6b1f79ec6'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    while True:
        connect_dict = connect_retry(url, api_key)
        retry_dict = connect_dict['retry_dict']
        param_dict = connect_dict['param_dict']
        try_again = connect_dict['retry_dict']['try_again']
        connect_msg = connect_dict['retry_dict']['connect_msg']

        if try_again in ['n','no']:  # if user did not want to retry search then end
            print('App closed...')
            break
        else:
            print(f"{nl}{connect_msg}{nl}")
            pretty_print(url, param_dict)
            if another_search() in ['y','yes']:
                continue
            else:
                print('App closed...')
                break


if __name__ == '__main__':
    main()

