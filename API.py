import requests


def bing_search(query, API_Key):
    url = "https://api.bing.microsoft.com/v7.0/search"
    headers = {
        "Ocp-Apim-Subscription-Key": API_Key
    }
    params = {
        "q": query,
        "textDecorations": True,
        "textFormat": "HTML"
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        search_results = response.json()
        return search_results['webPages']['value']
    else:
        print(f"Error: {response.status_code}")
        return None


# APIキーを設定
API_Key = 'Own_Api_Key'

# 検索クエリを指定
query = input()

results = bing_search(query, API_Key)

if results:
    for result in results:
        print(f"Title: {result['name']}")
        print(f"URL: {result['url']}")
        print(f"Snippet: {result['snippet']}\n")
else:
    print("No results found.")
