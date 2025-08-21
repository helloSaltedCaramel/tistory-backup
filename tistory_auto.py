import requests
from openai import OpenAI
import os

# GitHub Secrets에서 가져오기
ACCESS_TOKEN = os.getenv("TISTORY_ACCESS_TOKEN")
BLOG_NAME = os.getenv("TISTORY_BLOG_NAME")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_post(keyword: str):
    prompt = f"""
    키워드: {keyword}
    티스토리 블로그 글을 작성하라.
    - SEO 최적화 제목
    - 소제목(H2, H3)
    - 서론, 본문, 결론
    - 1000자 이상
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response.choices[0].message.content

def upload_post(title: str, content: str):
    url = "https://www.tistory.com/apis/post/write"
    data = {
        "access_token": ACCESS_TOKEN,
        "output": "json",
        "blogName": BLOG_NAME,
        "title": title,
        "content": content,
        "visibility": 3,  # 3=공개
    }
    r = requests.post(url, data=data)
    print(r.text)

if __name__ == "__main__":
    keyword = "여름철 건강 관리법"
    post_content = generate_post(keyword)
    lines = post_content.split("\n", 1)
    title = lines[0].strip()
    body = lines[1].strip() if len(lines) > 1 else post_content
    upload_post(title, body)
