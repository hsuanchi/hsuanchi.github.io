import requests
import json


def cache_article_info():
    response = requests.get(
        "https://us-central1-article-maxlist.cloudfunctions.net/get-articles"
    )
    data = response.json()
    with open("./static/article.json", "w") as f:
        json.dump(data, f, ensure_ascii=False)


if __name__ == "__main__":
    cache_article_info()
