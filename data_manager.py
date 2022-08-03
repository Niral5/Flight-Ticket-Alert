import requests

Get_endpoint = "https://api.sheety.co/76089144fcb365a5b109727e664a5b07/flightDeals/prices"
Add_endpoint = "https://api.sheety.co/76089144fcb365a5b109727e664a5b07/flightDeals/prices/2"


def change_sheets(codes):
    for i in range(len(codes)):
        sheet_inputs = {
            'price':{
                "iataCode": codes[i]
            }
        }

        requests.put(f"https://api.sheety.co/76089144fcb365a5b109727e664a5b07/flightDeals/prices/{i+2}", json=sheet_inputs)


def get_sheets():
    response = requests.get(Get_endpoint)
    result = response.json()
    return result
