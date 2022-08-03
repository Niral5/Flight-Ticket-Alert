import requests

api_key = "34Eg_VLly2oKPCouwiRXAW4d0jBm7RJi"
city_endpoint = "https://tequila-api.kiwi.com/locations/query"
prices_endpoint = "https://tequila-api.kiwi.com/v2/search"
FLY_FROM = "JFK"


def get_city_codes(cities):
    flight_code_list = []
    for city in cities:
        parameters = {
            "term": f"{city}",
            "limit": "1",
            "location_types": "city",
        }
        headers = {
            "apikey": api_key,
        }

        city_response = requests.get(url=city_endpoint, headers=headers, params=parameters)
        city_result = city_response.json()
        flight_code_list.append(city_result["locations"][0]["code"])
    return flight_code_list


def flight_prices(fly_to, date_from, date_to):
    parameter = {
        "fly_from": "JFK",
        "fly_to": fly_to,
        "date_from": date_from,
        "date_to": date_to,
        "nights_in_dst_from": 7,
        "nights_in_dst_to": 28,
        "flight_type": "round",
        "one_for_city": 1,
        "max_stopovers": 0,
        "curr": "USD"
    }

    headers = {
        "apikey": api_key,
    }
    response = requests.get(url=prices_endpoint, params=parameter, headers=headers)
    data = response.json()
    return data

