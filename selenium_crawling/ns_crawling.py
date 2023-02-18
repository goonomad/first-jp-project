from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 크롬드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time

# 브라우즈 꺼짐방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메세지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=chrome_options)

# 홈페이지 해당주소 이동
browser.get("http://www.naver.com")
browser.implicitly_wait(10)
browser.find_element(By.CSS_SELECTOR, 'a.nav.shop').click()
time.sleep(2)


search = browser.find_element(By.CSS_SELECTOR, 'input._searchInput_search_text_fSuJ6')
search.click()

# 검색어 입력
search.send_keys('아이폰13')
search.send_keys(Keys.ENTER)

# 스크롤 전 높이
before_h = browser.execute_script("return window.scrollY")

# 무한스크롤
while True:
    # 맨 아래로 스크롤을 내린다
    browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
    # 스크랩 사이 페이지 로딩 시간
    time.sleep(1)
    # 스크롤 후 높이
    after_h = browser.execute_script("return window.scrollY")

    if after_h == before_h:
        break
    before_h = after_h

# 상품정보 div
items = browser.find_elements(By.CSS_SELECTOR, ".basicList_info_area__TWvzp")

for item in items:
    name = item.find_element(By.CSS_SELECTOR, ".basicList_title__VfX3c").text
    try:
        price = item.find_element(By.CSS_SELECTOR, ".price_num__S2p_v").text
    except:
        price = "판매중단"
    link = item.find_element(By.CSS_SELECTOR, ".basicList_title__VfX3c > a").get_attribute('href')
    print(name, price, link)
    