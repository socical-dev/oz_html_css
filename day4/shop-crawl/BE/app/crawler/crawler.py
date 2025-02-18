import sys
import os

# 프로젝트 최상위 경로 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from app.services.product_service import ProductService

def scrape_product():
    """KREAM 웹사이트에서 상품 데이터를 크롤링하여 DB에 저장하는 함수."""
    options = webdriver.ChromeOptions()
    
    # User-Agent 변경 (Chrome 브라우저처럼 위장)
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    options.add_argument(f"user-agent={user_agent}")

    # Headless 모드 비활성화 (테스트 후 다시 활성화 가능)
    # options.add_argument("--headless")  # 👉 Headless 모드 해제
    options.add_argument("--disable-blink-features=AutomationControlled")  # Selenium 탐지 방지
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get("https://kream.co.kr/search?tab=44")

        # JavaScript가 완전히 실행될 때까지 대기 (최대 15초)
        time.sleep(5)  # 기본 로딩 대기
        WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".search_result_item.product"))
        )

        # 상품 목록 찾기
        product_elements = driver.find_elements(By.CSS_SELECTOR, ".search_result_item.product")
        print(f"🔍 크롤링된 상품 개수: {len(product_elements)}")

        for product in product_elements:
            try:
                brand = product.find_element(By.CLASS_NAME, "brand").text
                name = product.find_element(By.CLASS_NAME, "name").text
                price_text = product.find_element(By.CLASS_NAME, "amount").text
                
                # 가격에서 "원" 제거 후 변환
                price = int(price_text.replace("₩", "").replace(",", "").replace("원", "").strip())
                
                category = "스니커즈"

                print(f"크롤링 성공: {brand} - {name} - {price}")

                # DB 저장
                result = ProductService.add_product(category, brand, name, price)
                if result:
                    print(f"DB 저장 성공: {brand} - {name} - {price}")
                else:
                    print(f"DB 저장 실패: {brand} - {name} - {price}")

            except Exception as e:
                print(f"상품 크롤링 오류: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    while True:
        scrape_product()
        print("10초 후 다시 크롤링 실행...")
        time.sleep(10)  # 10초마다 크롤링 실행
