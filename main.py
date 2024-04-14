import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content of the response
soup = BeautifulSoup(response.content, "html.parser")

# Find all elements with class "sitebit comhead" in the HTML
news_headers = soup.find_all("span", class_="titleline")
i = 0
# Extract and print the text of all news headers found
if news_headers:
    for header in news_headers:
        i+=1
        header_text = header.text.strip()
        print(i,":",header_text)
else:
    print("No news headers found on the page.")
