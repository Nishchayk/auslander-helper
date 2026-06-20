import json
import requests
from bs4 import BeautifulSoup
import os



class scarping_information():
    def __init__(self):
        pass
    def reading_json(self):
        with open("./berlin_survival_links.json","r") as f:
            data = json.load(f)

        
        count = 0
        for category_name,items in data.items():
            if category_name == 'meta':
                continue

            for item in items:
                url = item.get('url')
                if url:
                    count += 1
                    print(f"{count}.[{category_name}] {url}")

scarping_information().reading_json()
