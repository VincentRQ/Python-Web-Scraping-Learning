
import pandas as pd


def get_jobs_for(lat=None, lng=None, postal_code=None, results=20):
  from pgeocode import Nominatim
  import requests

  if (lat is None or lng is None) and postal_code is None:
    raise ValueError("Both lat nad lng must be provided")

  if postal_code is not None:
    nomi = Nominatim("ca")
    geo = nomi.query_postal_code(postal_code)
    lat = geo.latitude
    lng = geo.longitude


  url = f"https://api.higherme.com/classic/jobs?page=1&includes=location,location.company,location.externalServiceReferences&limit={results}&filters\\[brand.id\\]=58bd9e7f472bd&filters\\[lat\\]={lat}&filters\\[lng\\]={lng}&filters\\[distance\\]=20&sort\\[distance\\]=asc"


  headers = {
    'authority': 'api.higherme.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.8',
    'higherme-client-version': '2023.03.07_10.0c',
    'origin': 'https://app.higherme.com',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Brave";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
  }

  response = requests.get(url, headers=headers).json()
  get_jobs_for(postal_code="m2e", results=8)

  df = pd.DataFrame(
    data=[r.get('attributes') for r in response.get('data')],
    columns=['title', 'full_time', 'part_time', 'requirements', 'distance']

  )

  return df

#
# nomi.query_location("Union Station") or
# nomi.query_postal_code("m5e") - which provides the lat and long