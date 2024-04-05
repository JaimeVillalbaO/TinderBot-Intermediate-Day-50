from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time
# import undetected_chromedriver as uc

# driver = uc.Chrome()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)  # keeps chrome open


driver = webdriver.Chrome(options=chrome_options)
driver.get('https://tinder.com/app/recs')

time.sleep(2)

cockies = driver.find_element(By.XPATH, value='//*[@id="q1434999767"]/div/div[2]/div/div/div[1]/div[1]/button')
cockies.click()

time.sleep(2)

log_in = driver.find_element(By.LINK_TEXT, value='Inicia sesión')
log_in.click()

time.sleep(1)

celular = driver.find_element(By.XPATH, value='//*[@id="q1656340203"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[3]/button/div[2]/div[2]/div/div')
celular.click()
time.sleep(1)

number_cel = driver.find_element(By.XPATH, value='//*[@id="q1656340203"]/main/div/div[1]/div/div[2]/div/div[2]/div/div[2]/input')
number_cel.send_keys('3215696357')

siguiente = driver.find_element(By.XPATH, value='//*[@id="q1656340203"]/main/div/div[1]/div/div[3]/button/div[2]/div[2]')
siguiente.click()

time.sleep(45)

allow_loc = driver.find_element(By.XPATH, value='//*[@id="q1656340203"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
allow_loc.click()

time.sleep(2)
try:
    allow_not = driver.find_element(By.XPATH, value='//*[@id="q1656340203"]/main/div/div/div/div[3]/button[2]/div[2]/div[2]')
    allow_not.click()
except:
    pass

time.sleep(4)
while True:
    try: 
        like = driver.find_element(By.XPATH, value='//*[@id="q1434999767"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button/span/span/svg/path')
        like.click()
        time.sleep(4)
        
    

    except ElementClickInterceptedException: 
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            time.sleep(2)
            

# //*[@id="q1434999767"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]
# //*[@id="q1434999767"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button
# //*[@id="q1434999767"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button/span/span/svg/path