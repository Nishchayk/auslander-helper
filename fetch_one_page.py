import requests
from bs4 import BeautifulSoup
import os 


os.makedirs("data",exist_ok=True)


url = r"https://allaboutberlin.com/glossary/Anmeldung"

print(f"Featching {url}")

responce = requests.get(url=url)

print(f"Status code: {responce.status_code}")
print(f"content length {len(responce.text)} char")

soup = BeautifulSoup(responce.text,"html.parser")


for tag in soup(["script", "style", "nav", "footer", "header"]):
    tag.decompose()

clean_text = soup.get_text(separator="\n",strip=True)

print(f"Content length (cleaned): {len(clean_text)} characters\n")
print("--- First 1000 characters of cleaned text ---\n")
# print(clean_text[:1000])

with open(r"./data/anmeldung.txt","w",encoding="utf-8") as f:
    f.write(clean_text)

print(f"\nSaved cleaned text to data/anmeldung.txt ({len(clean_text)} chars)")