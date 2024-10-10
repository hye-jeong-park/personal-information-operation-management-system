from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import traceback
import getpass
from openpyxl import load_workbook
import sys

# 크롤링할 최대 게시글 수 설정
max_posts = 10 

# 엑셀 파일 경로 및 워크시트 이름 설정
excel_file = r'C:\Users\PHJ\output\개인정보 운영대장.xlsx'
worksheet_name = '개인정보 추출 및 이용 관리'

# 웹드라이버 설정
driver = webdriver.Chrome()

try:
    # 로그인 페이지로 이동
    driver.get('https://gw.com2us.com/')

    # 로그인 처리
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'Username')))
    username_input = driver.find_element(By.ID, 'Username')
    password_input = driver.find_element(By.ID, 'Password')

    username = input('아이디를 입력하세요: ')
    password = getpass.getpass('비밀번호를 입력하세요: ')

    username_input.send_keys(username)
    password_input.send_keys(password)

    login_button = driver.find_element(By.CLASS_NAME, 'btnLogin')
    login_button.click()

    # 로그인 성공 여부 확인
    WebDriverWait(driver, 30).until(EC.url_changes('https://gw.com2us.com/'))
    current_url = driver.current_url
    print(f"로그인 후 현재 URL: {current_url}")

    if 'login' in current_url.lower():
        print("로그인에 실패하였습니다.")
        driver.quit()
        sys.exit()