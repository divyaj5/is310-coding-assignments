import requests
import os
import json

swapi_url = "https://swapi.py4e.com/api/people/1/"

europeana_api_key = os.getenv("EUROPEANA_API_KEY")
if not europeana_api_key:
    raise ValueError("EUROPEANA_API_KEY not set. Please export it in your terminal.")

response = requests.get(swapi_url)
if response.status_code == 200:
    luke_data = response.json()
    print("Luke Skywalker Data:")
    print(json.dumps(luke_data, indent=4))
else:
    print(f"SWAPI request failed with status code: {response.status_code}")
    exit()

europeana_url = "https://api.europeana.eu/record/v2/search.json"
params = {
    "query": "Luke Skywalker",
    "wskey": europeana_api_key,
    "rows": 5,
    "profile": "rich"
}

europeana_response = requests.get(europeana_url, params=params)
if europeana_response.status_code == 200:
    europeana_results = europeana_response.json().get("items", [])
    if europeana_results:
        europeana_data = europeana_results[0]  
        print("\nEuropeana Data for 'Luke Skywalker':")
        print(json.dumps(europeana_data, indent=4))
    else:
        print("No results found for 'Luke Skywalker' in Europeana.")
else:
    print(f"Europeana API request failed with status code: {europeana_response.status_code}")
    exit()

combined_data = {
    "SWAPI_Character": luke_data,
    "Europeana_Item": europeana_data if europeana_results else {"error": "No Europeana data found"}
}

with open("luke_skywalker_data.json", "w") as file:
    json.dump(combined_data, file, indent=4)

print("\nCombined data saved to 'luke_skywalker_data.json'")
