import feedparser, os, hashlib
from datetime import datetime

RSS_URL = "https://saltedcaramel.tistory.com/rss"
OUTPUT_DIR = "posts"
DB_FILE = "history.db"

os.makedirs(OUTPUT_DIR, exist_ok=True)
history = set(open(DB_FILE).read().splitlines()) if os.path.exists(DB_FILE) else set()

feed = feedparser.parse(RSS_URL)
for item in feed.entries:
    guid = item.link
    if guid in history: continue
    title = item.title
    date = item.published
    content = item.content[0].value if hasattr(item, "content") else item.description
    fn = datetime(*item.published_parsed[:6]).strftime("%Y%m%d") + "_" + hashlib.md5(guid.encode()).hexdigest() + ".md"
    md = f"# {title}\n\n*발행: {date}*\n\n---\n\n{content}"
    with open(os.path.join(OUTPUT_DIR, fn), "w", encoding="utf-8") as f: f.write(md)
    history.add(guid)

with open(DB_FILE, "w") as f:
    f.write("\n".join(history))
