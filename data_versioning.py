# Get url from DVC
import pandas as pd
import dvc.api

path='data/wine_original.csv'
repo='https://github.com/Enam88/mlops_lab'
version = "v2"

data_url = dvc.api.get_url(
  path=path,
  repo=repo,
  rev=version
  )

data = pd.read_csv(data_url, sep=";")
print(data)