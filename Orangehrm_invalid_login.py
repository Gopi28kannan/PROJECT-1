from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class webpage:
     def __init__(self,url):
          self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
          self.url=url

     def get_url(self):
          #get url
          self.driver.get(self.url)
          time.sleep(2)
          #maximize window
          self.driver.maximize_window()

     def invalid_login(self):
          #use try method invalid login
          try:
               wait = WebDriverWait(self.driver, 20)
               wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys('Admin')
               time.sleep(1)
               self.driver.find_element(By.NAME, value="password").send_keys('invalid password')
               time.sleep(1)
               self.driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
               print("invalid credentials")
          #no such element exeption from invalid login
          except NoSuchElementException as selenium_error:
               print("invalid login errors : \n",selenium_error)

     def shutdown(self):
          time.sleep(5)
          self.driver.quit()

url='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
web=webpage(url)
web.get_url()
web.invalid_login()
web.shutdown()
