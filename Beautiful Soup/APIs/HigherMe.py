def get_jobs_for(lat=None, lng=None, results=20):
  if lat is None or lng is None:
    raise ValueError("Both lat nad lng must be provided")

  import requests

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

  response = requests.request("GET", url, headers=headers)

  return response.json()


response_data = get_jobs_for(42.6532, -79.3832, 20)
response_data.get('data')
import pandas as pd
df = pd.DataFrame(
    data=[r.get('attributes') for r in response_data.get('data')],
    columns=['title', 'full_time', 'part_time', 'requirements', 'distance']
)

df.to_csv("open_positions.csv", index=False)

