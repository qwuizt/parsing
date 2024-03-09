import requests


def make_req(req: str):
    url = 'https://api.foursquare.com/v3/places/search'
    headers = {"accept": "application/json",
               "Authorization": "YOUR_foursquare_API" 
               }

    params = {
        "query": req,
        "ll": "55.74,37.61",
        "open_now": "true",
        "sort": "RATING",
        "limit": 3
    }
    respons = requests.get(url, params=params, headers=headers)
    return respons


while True:
    print("Type the category. For exit type 'end'")
    req = str(input())
    req.lower()
    if req != "end":
        data = make_req(req).json()
        for place in data.get("results"):
            print(f"{place.get("name")}, {place.get("location").get("address")}, {place.get('rating')}")
    else:
        break
