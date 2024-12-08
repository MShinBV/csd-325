# Miles Shinsato 12/08/2024 CSD325-A339 Module 9.2 Test Connection.py

# Import prompt for requests library
import requests

# Sends for a GET request Response from the given API URL
# Defined as response variable
response = requests.get('http://www.google.com')

# Used to print status_code of the response
print(response.status_code)