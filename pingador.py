import requests

url = "https://promorar-hidro.onrender.com"
headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    r = requests.get(url, headers=headers, timeout=10)
    print(f"Ping enviado! Status: {r.status_code}")
except Exception as e:
    print(f"Erro ao pingar: {e}")
