from bs4 import BeautifulSoup
import requests


class Parser:
    html = ""
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, 'lxml')

    def parsing(self):
        news = self.html.find_all("div", class_="post-outer")
        for item in news:
            title = item.find("h3").text
            href = item.find("h3").find("a").get('href')
            author = item.find("a", class_="g-profile").text.strip()
            self.res.append({
                "title": title,
                "href": href,
                "author": author
            })

    def save(self):
        with open(self.path, "w") as f:
            i = 1
            for item in self.res:
                f.write(f"Новость № {i}\n\nНазвание: {item['title']}\n"
                        f"Ссылка: {item['href']}\nАвтор: {item['author']}"
                        f"\n\n{'*' * 20}\n")
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()
