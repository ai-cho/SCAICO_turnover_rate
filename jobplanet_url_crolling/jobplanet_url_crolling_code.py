from webdriver_manager.chrome import ChromeDriverManager
# chromedrivermangager를 통해 최신 크롬 버전이 발생해도 관리할 필요 없음. 캐시 형식임.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
'''
  company url의 경우,
  #listCompanies > div > div.section_group > section > div > div > div > a 
  여기서 숫자만 바뀜.
  
'''
'''
  회사 리뷰 개수의 경우도 마찬가지.
  #listCompanies > div > div.section_group > section > div > div > dl.content_col2_3.cominfo > dd.row_end > a:nth-child(1)
'''
file = open("manufacture_chemistry_company_url.txt", "w")
chrome_options = webdriver.ChromeOptions() # 브라우저의 옵션을 적용가능하나, 아무것도 적용하지 않았음.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = chrome_options)
for i in range(1, 200): # 홈페이지 번호를 바꾸는 i, 30page까지 볼 것임.
  driver.get("https://www.jobplanet.co.kr/companies?industry_id=200&page= "+str(i)) # 주소만 직종별로 바꾸면됨.
  print(i)
  time.sleep(5)
  #url 리스트와 회사 리뷰 개수 리스트
  url_list = driver.find_elements(By.CSS_SELECTOR, '#listCompanies > div > div.section_group > section > div > div > div > a')
  raw_volume_list = driver.find_elements(By.CSS_SELECTOR, '#listCompanies > div > div.section_group > section > div > div > dl.content_col2_3.cominfo > dd.row_end > a:nth-child(1)')
  volume_list=[]
  for i in raw_volume_list:
    volume_list.append(int(i.text.split(" ")[0])) # 개수들을 앞에꺼만 가져와서 int로 변경.
  warning_data = 0 # 이걸로, 개수가 100개 이상인 것만 뽑을 것임.
  for url in url_list:
    if volume_list[warning_data] < 100:
      print("데이터의 개수가 100개보다 적습니다.", volume_list[warning_data])
      break
    file.write(url.get_attribute('href')+"\n")
    warning_data +=1
  if warning_data != 10: # 그 분야의 100개 이상인 것을 다 뽑았다는 뜻.
    break
print("모든 작업이 끝났습니다.")
file.close()    
  
  
  




