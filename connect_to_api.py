import requests
import calendar
import time
import json
import os
import config_directories
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# suppress InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

current_GMT = time.gmtime()
time_stamp = calendar.timegm(current_GMT)
data = {
    "currentClientTimestamp": int(calendar.timegm(current_GMT)),
    "serverTimestamp": 0,
}


api_url = "https://api.zenmoney.ru/v8/diff/"
headers = config_directories.headers
response = requests.post(api_url, json=data, headers=headers, verify=False)
request = response.request


# check if the request was successful (status code 200)
if response.status_code == 200:
    print("API Request Successful.")

    # read data from the datasource
    # print(response.json())
    accounts = response.json().get('account', [])
    companies = response.json().get('company', [])
    countries = response.json().get('country', [])
    instruments = response.json().get('instrument', [])
    tags = response.json().get('tag', [])
    transactions = response.json().get('transaction', [])
    users = response.json().get('user', [])

    directory_path = config_directories.raw_area

    # create function for getting JSON files
    def save_data_to_json(data, table_name: str, directory_path):
        file_path = os.path.join(directory_path, f"{table_name}.json")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    # specify the list of tables and corresponding data
    list_of_tables = [
        ('accounts', accounts),
        ('companies', companies),
        ('countries', countries),
        ('instruments', instruments),
        ('tags', tags),
        ('transactions', transactions),
        ('users', users)
    ]

    # save data for each table to a separate JSON file
    for table_name, table_data in list_of_tables:
        save_data_to_json(table_data, table_name, directory_path)


else:
    print(f"Failed to connect to the API. Status Code: {response.status_code}")
    print("Error Message:")
    print(response.text)
