# Miles Shinsato 12/08/2024 CSD325-A339 Module 9.2 Tutorial.py

# Import prompt for requests library
import requests

# Import prompt for json module
import json

# Defining variable url_api to reference later
# Limited the API to 9 otherwise we would have over a thousand returned values
url_api = ('https://pokeapi.co/api/v2/pokemon?limit=9')

# Sends for a GET request Response from the given url_api
# Defined as response variable
response = requests.get(url_api)

# Print message to give status code
print("Status Code:", response.status_code)

# Print message to give no format response
print("Unformatted Response:")

print(response.text)

# Define function jprint as a function to call
# There is (obj) to define it as an object
def jprint(obj):

    # json.dumnps() will convert the Python object from above to a json formated string
    # Indent=4 is there to specify that the output is to be indented 4 spaces, (can be another number)
    # Sort_keys=True is to alphabetize the list out before print
    print(json.dumps(obj, indent=4, sort_keys=True))

# This is just to call jprint function
jprint(response.json())


