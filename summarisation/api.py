import requests

def fetch_news(company_name, api_key):
    """
    Fetch news articles related to the given company name using the GNews API.
    Returns a list of articles with title, link, summary, and content.
    """
    url = f"https://gnews.io/api/v4/search?q={company_name}&lang=en&country=us&max=10&token={api_key}"
    response = requests.get(url)
    data = response.json()
    print("API Response:", data)
    
    articles = []
    if 'articles' in data:  # Check if 'articles' key exists
        for item in data['articles']:
            articles.append({
                "title": item['title'],
                "link": item['url'],
                "summary": item['description'],
                "content": item['content']
            })
    else:
        print("Error: 'articles' key not found in API response.")
        if 'message' in data:
            print(f"API Error: {data['message']}")

    return articles