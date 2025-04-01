import pandas as pd

from config.path import root_folder
from helpers.clean_date import clean_date


df_2024_with_month = pd.read_parquet(f"{root_folder}/data/historical/2024/processed/2024_full_US_PA_with_month.parquet")

# observation number reported by month in 2024
obs_reported_by_month = pd.read_parquet(f"{root_folder}/data/historical/2024/processed/2024_full_US_PA_by_month.parquet")

# Montly species count by howMany
monthly_species_count = (
    df_2024_with_month.groupby(['Month', 'speciesCode'])
    .agg(ObservationCount=('howMany', 'sum'))  # Sum the howMany to get total observations
    .reset_index()
)

top_species_per_month = (
    monthly_species_count.loc[monthly_species_count.groupby('Month')['ObservationCount'].idxmax()]
    .reset_index(drop=True)
)

monthly_species_count_unique = (
    df_2024_with_month.groupby(['Month', 'comName'])
    .agg(ObservationCount=('comName', 'count'))  # Sum the howMany to get total observations
    .reset_index()
)

top_species_per_month = (
    monthly_species_count_unique
    .loc[monthly_species_count_unique.groupby('Month')['ObservationCount']
    .idxmax()]
    .reset_index(drop=True)
)

# this will return a series (Month - index and the count)
top_species_per_month_2 = (
    monthly_species_count_unique.
    groupby('Month')['ObservationCount']
    .idxmax()
    # .reset_index(drop=True)
)