import os
import time
from openai import OpenAI
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# OpenAI API
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TISTORY_ID = os.getenv("TISTORY_ID")
TISTORY_PW = os.getenv("TISTORY_PW")
BLOG_NAME = os.getenv("TISTORY_BLOG_NAME")  # 예: myblog (https://myblog.tistory.com)

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_post(keyword: str):
    prompt = f"""
    키워드: {keyword}
    티스토리 블로그 글 작성.
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
    options = Options()
    options.add_argument("--headless")  # 화면 없이 실행
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # 로그인
    driver.get("https://www.tistory.com/auth/login")
    time.sleep(3)

    driver.find_element(By.NAME, "loginId").send_keys(TISTORY_ID)
    driver.find_element(By.NAME, "password").send_keys(TISTORY_PW)
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

    time.sleep(5)

    # 글쓰기 페이지
    driver.get(f"https://{BLOG_NAME}.tistory.com/manage/newpost/")
    time.sleep(5)

    # 제목 입력
    driver.find_element(By.NAME, "title").send_keys(title)

    # 본문 입력 (iframe 안에 body 있음)
    driver.switch_to.frame(driver.find_element(By.ID, "tx_canvas_wysiwyg"))
    driver.find_element(By.TAG_NAME, "body").send_keys(content)
    driver.switch_to.default_content()

    time.sleep(2)

    # 발행 버튼 클릭
    driver.find_element(By.CLASS_NAME, "btn_publish").click()
    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    keyword = "여름철 피부 관리법"
    post_content = generate_post(keyword)
    lines = post_content.split("\n", 1)
    title = lines[0].strip()
    body = lines[1].strip() if len(lines) > 1 else post_content
    upload_post(title, body)
