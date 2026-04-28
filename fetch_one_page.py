import requests


url = r"https://allaboutberlin.com/glossary/Anmeldung"

print(f"Featching {url}")

responce = requests.get(url=url)

print(f"Status code: {responce.status_code}")
print(f"content length {len(responce.text)} char")
print("/---------------First 500 char of html parse----------------/")
print(responce.text[:500])