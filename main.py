"""
jwk

"""

import sys
from selenium import webdriver
import pywinmacro as pw
import time
import pyperclip as pc

# 아이디를 입력받습니다.
id = sys.argv[1]

# 패워드를 입력받습니다
ps = sys.argv[2]

# 검색어를 입력받습니다
keyword = sys.argv[3].strip()

# 크롬드라이버를 불러옵니다
driver = webdriver.Chrome(executable_path="chromedriver.exe")

# 구글 뉴스 검색 url 을 정리합니다.
search_url = "https://www.google.com/search?q=&tbm=nws&q="

# 구글에서 뉴스를 검색합니다.
driver.get(search_url + keyword)
time.sleep(5)

# 클릭할 좌표를 지정합니다
location = (119, 664)

# 화면을 클릭합니다.
pw.click(location)

# 컨트롤 a
pw.ctrl_a()

# 컨트롤 c
pw.ctrl_c()

time.sleep(3)

# 클립보드의 내용물을 뽑아옵니다.
news_text = pc.paste()

# 뉴스 텍스트를 스플릿합니다.
splt = news_text.split("\r\n\r\n")[2:-1]

# 트위터에 접속합니다
driver.get("https://twitter.com/login")

time.sleep(5)
# 아이디를 입력합니다
pw.typing(id)
# 탭을 입력합니다
pw.key_press_once("tab")
# 비밃번호를 입력합니다
pw.typing(ps)
# 엔터를 입력합니다
pw.key_press_once("enter")
# 5초를 기다립니다
time.sleep(5)

for el in splt:

    # 트위터에 글을 올립니다.
    # 게시물 작성페이지로 이동
    driver.get("https://twitter.com/intent/tweet")
    time.sleep(5)
    pw.type_in(el)
    time.sleep(2)

    # 컨트롤 + 엔터
    pw.key_on("control")
    pw.key_on("enter")
    pw.key_off("control")
    pw.key_off("enter")

    time.sleep(10)


