""" EXTRACT DATA """

from datetime import datetime
import time
import os

from dotenv import load_dotenv
import pandas as pd
import requests


load_dotenv()
pd.set_option("display.max_columns", None)


header = {
    "X-eBirdApiToken": os.getenv("api_token"),
}


def get_data(headers, endpoint, filepath):
    """Make GET requests, fetch data and return JSON"""
    response = requests.get(endpoint, headers=header)
    response_json = response.json()
    # print(len(response_json))
    df = pd.DataFrame(response_json)
    save_to_csv(df, filepath)
    return response_json


def save_to_csv(df, filepath):
    """Save a dataframe to a CSV file"""
    df.to_csv(filepath)


# get historical data for a specified year
hist_data = []

region = "US-PA"
y = 2024
months = range(10, 13)

for mo in months:
    print(f"Getting data for {mo}, {y}")

    if mo in (1, 3, 5, 7, 8, 10, 12):
        days = range(1, 32)
    elif mo == 2:
        days = range(1, 29)
    else:
        days = range(1, 31)

    for dd in days:
        timestamp = datetime.now().isoformat()
        filepath = f"data/{region}_{timestamp}"
        endpoint = f"https://api.ebird.org/v2/data/obs/{region}/historic/{y}/{mo}/{dd}"
        resp_json = get_data(header, endpoint, filepath)
        hist_data.extend(resp_json)
        time.sleep(1)

    df = pd.DataFrame(hist_data)
    df.to_csv(f"data/dashboard/hist_{mo}_{y}_full_US_PA.csv")
