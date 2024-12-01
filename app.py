import requests
import feedparser
from datetime import datetime

rss_url = 'https://jadi.net/feed/'

response = requests.get(rss_url)
feed = feedparser.parse(response.content)

for entry in feed.entries:
    title = entry.title
    link = entry.link
    published = entry.published
    description = entry.summary
    content = entry.content[0].value if 'content' in entry else description

    html_content = f"""
    <html>
        <head><title>{title}</title></head>
        <body>
            <h1>{title}</h1>
            <p><strong>Published on:</strong> {published}</p>
            <div>{content}</div>
            <p><a href="{link}">Read more</a></p>
        </body>
    </html>
    """
    
    filename = f"post_{datetime.now().strftime('%Y%m%d%H%M%S')}_{title.replace(' ', '_')}.html"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Saved: {filename}")
