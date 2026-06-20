import json
import os
import re
import requests
from bs4 import BeautifulSoup


os.makedirs("data", exist_ok=True)


with open("berlin_survival_links.json","r",encoding="utf-8") as f:
    data = json.load(f)


urls_to_scope = []

for category_name,items in data.items():
    if category_name == "meta":
        continue

    for item in items:
        url = item.get("url")
        title = item.get("title","untitled")

        if url:
            urls_to_scope.append({
                "url":url,
                "title":title,
                "category":category_name
            })

def make_filename(title):

    safe = re.sub(r"[^a-zA-Z0-9]+","_",title.lower().strip("_"))
    return f"{safe}.txt"




success_count = 0
fail_count = 0

for i,entry in enumerate(urls_to_scope,start=1):
    url = entry["url"]
    title = entry["title"]
    category = entry["category"]

    print(f"[{i}/{len(urls_to_scope)}] fetching:{title}")

    try:
        response = requests.get(url,timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text,"html.parser")
        for tag in soup(["script","style","nav","footer","header"]):
            tag.decompose()

        clean_text = soup.get_text(separator="\n",strip=True)

        filename = make_filename(title)
        filepath = os.path.join("data",filename)

        with open(filepath,"w",encoding="utf-8") as f:
            f.write(f"Title:{title}\n URL:{url}\ncategory:{category}\n\n")
            f.write(clean_text)

        print(f"saved{len(clean_text)} chars to data/{filename}\n")
        success_count+=1

    except requests.exceptions.Timeout:
        print(f"x Timeout(>15s)\n")
        fail_count += 1
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}\n")
        fail_count += 1
    except requests.exceptions.RequestException as e:
        print(f"Network error:{e}\n")
        fail_count +=1
    except Exception as e:
        print(f"Unexpected error: {e}\n")
        fail_count +=1


print("Done")
print(f"success: {success_count}")
print(f"Failed: {fail_count}")