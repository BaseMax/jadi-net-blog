import os
import requests
import feedparser
from datetime import datetime

RSS_URL = 'https://jadi.net/feed/'
POSTS_DIR = 'posts'
INDEX_FILE = 'index.html'

if not os.path.exists(POSTS_DIR):
    os.makedirs(POSTS_DIR)

response = requests.get(RSS_URL)
feed = feedparser.parse(response.content)

post_links = []

for entry in feed.entries:
    title = entry.title
    link = entry.link
    published = entry.published
    description = entry.summary
    content = entry.content[0].value if 'content' in entry else description

    html_content = f"""
    <html lang="fa-IR" dir="rtl">
        <head><title>{title}</title></head>
        <body>
            <h1>{title}</h1>
            <p><strong>Published on:</strong> {published}</p>
            <div>{content}</div>
            <p><a href="{link}">Read more</a></p>
        </body>
    </html>
    """
    
    filename = f"{POSTS_DIR}/post_{datetime.now().strftime('%Y%m%d%H%M%S')}_{title.replace(' ', '_')}.html"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)

    post_links.append((title, filename))

post_links.sort(key=lambda x: os.path.getctime(x[1]), reverse=True)

index_html_content = """
<html lang="fa-IR" dir="rtl">
    <head><title>Jadi Clone Blog</title></head>
    <body>
        <h1>Jadi Clone Blog</h1>
        <h2>Recent Posts</h2>
        <ul>
"""

for title, filename in post_links:
    index_html_content += f'<li><a href="{filename}">{title}</a></li>\n'

index_html_content += """
        </ul>
    </body>
</html>
"""

with open(INDEX_FILE, 'w', encoding='utf-8') as f:
    f.write(index_html_content)

print("Posts and index.html updated.")
