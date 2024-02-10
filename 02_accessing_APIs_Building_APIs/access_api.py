import requests


def get_news(topic, from_date, api_key="2a06ec8c29214085aadbff6e96c0b514"):
    url = f"https://newsapi.org/v2/everything?q={topic}&from={from_date}&sortBy=popularity&apiKey={api_key}"
    r = requests.get(url)
    content = r.json()
    articles = content["articles"]
    results = []

    for article in articles:
        results.append(
            f"TITLE\n{article['title']}', '\nDESCRIPTION\n{article['description']}"
        )
    return results


print(get_news("Apple", "2024-02-9"))
