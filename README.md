# Jadi Net Blog Extractor

This Python script is used to extract posts from a WordPress blog (https://jadi.net/) and save them in HTML format. The script fetches the RSS feed, parses the posts, and saves each post as an individual HTML file.

## Requirements

To use the script, you need to install the following dependencies:

```
pip install -r requirements.txt
```

## Why This Project?

The website **jadi.net** has been blocked within Iran's internet network, making it difficult for users in Iran to access the site. To view the blog, one must use a VPN to bypass the restrictions. To address this issue, I created this GitHub repository to automatically fetch and extract the blog posts from **jadi.net** and save them in this repository.

This repository serves as a **clone blog** of **jadi.net**, where all blog posts are saved in a filter-less, easily accessible manner. You can now access the content directly on GitHub, which is not blocked by the Iranian government.

## How to Use

1. Clone this repository:
```
git clone https://github.com/BaseMax/jadi-net-blog.git
cd jadi-net-blog
```

2. Run the script:

```
python extract_posts.py
```

The script will fetch posts from the RSS feed and save them as HTML files in the current directory.

## License

MIT License

© 2024 Max Base
