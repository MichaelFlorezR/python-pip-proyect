import requests

def get_categories():
    r = requests.get("https://api.escuelajs.co/api/v1/categories")
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    categories = r.json()  # This converts the JSON string to a Python list of dictionaries
    for category in categories:  # Iterate through each dictionary in the list
        print(category["name"])  # Access the "name" key from each dictionary

