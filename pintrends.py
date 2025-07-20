import requests

access_token = "YOUR_ACCESS_TOKEN"  # from your Pinterest Dev App
headers = {
    "Authorization": f"Bearer {access_token}"
}

params = {
    "trend_type": "top",
    "region": "fr",  # for France
    "limit": 20
}

response = requests.get(
    "https://api.pinterest.com/v5/trends/keywords/fr/top", 
    headers=headers, 
    params=params
)

if response.status_code == 200:
    data = response.json()
    for i, trend in enumerate(data.get("items", []), 1):
        print(f"{i}. {trend.get('keyword')}")
else:
    print("Error:", response.status_code, response.text)
