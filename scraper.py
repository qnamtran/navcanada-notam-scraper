import pandas as pd
import requests
import json
import re
import warnings
import urllib3
from datetime import datetime
from tabulate import tabulate

# Suppress insecure request warning
warnings.filterwarnings("ignore", category=urllib3.exceptions.InsecureRequestWarning)

url = "https://plan.navcanada.ca/weather/api/alpha/?site=CYYW&site=CYAT&site=CNE3&site=CYTL&site=CYAC&site=CYVZ&site=CYFA&site=CYFH&site=CYER&site=CYAQ&site=CZKE&site=CPV8&site=CNM5&site=CYLH&site=CZMD&site=CKQ3&site=CYKP&site=CYPO&site=CYPL&site=CYPM&site=CPV7&site=CZRJ&site=CZPB&site=CZSJ&site=CKD9&site=CJV7&site=CKB6&site=CYWP&site=CKL3&alpha=notam&notam_choice=default&_=1710526447281"

# Fetch JSON data from the URL
response = requests.get(url, verify=False)
data = response.json()

# Extract relevant data from the JSON
data = data["data"]
formatted_data = []
for item in data:
    if item["location"]:
        text = json.loads(item["text"])["raw"]
        start_match = re.search(r"B\) (\d{10})", text)
        start_validity = start_match.group(1) if start_match else None
        if start_validity:
            start_validity = pd.to_datetime(start_validity, format="%y%m%d%H%M").strftime("%Y-%m-%d %H:%M")
        end_match = re.search(r"C\) (\d{10})", text)
        end_validity = end_match.group(1) if end_match else None
        if end_validity:
            end_validity = pd.to_datetime(end_validity, format="%y%m%d%H%M").strftime("%Y-%m-%d %H:%M")
        formatted_item = {
            "Location": item["location"],
            "Start Validity": start_validity,
            "End Validity": end_validity,
            "Text": text,
            "pk": item["pk"],
        }
        formatted_data.append(formatted_item)

# Create a DataFrame from the formatted data
df = pd.DataFrame(formatted_data)

# Drop duplicates based on "pk" field
df.drop_duplicates(subset="pk", inplace=True)

# Display the record count
print(f"Total NOTAMs: {len(df)}")

# Convert the DataFrame to a tabulated format and print it
print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))