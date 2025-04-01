import pandas as pd

from config.path import root_folder
from helpers.clean_date import clean_date


pd.set_option("display.max_columns", None)

data = pd.read_csv(
    f"{root_folder}/data/dashboard/hist_january_full_US_PA.csv", index_col=0
)

# Find top 5 species based on observation number (howMany field value)
species_count = (
    data.groupby(["sciName"])
    .agg(Count=("howMany", "sum"))
    .reset_index()
    .sort_values(by="Count", ascending=False)
    .head(5)
)

# clean date to make sure it's of the same format
date_data = data.assign(obsDtClean=data["obsDt"].apply(clean_date))

# group observations number by date
obs_by_date = (
    date_data.groupby("obsDtClean")
    .size()
    .reset_index(name="Count")
    .sort_values(by="Count")
)

# top 5 counties by observations
county_top_5 = (
    pd.read_csv(f"{root_folder}/data/location_with_address")
    .groupby("County")[["County"]]
    .size()
    .reset_index(name="Count")
    .sort_values(by="Count", ascending=False)
    .head(5)
)
