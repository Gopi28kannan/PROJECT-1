from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class webpage1:
     def __init__(self,url):
          self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
          self.url=url
     def get_url(self):
          #get url
          self.driver.get(self.url)
          #maximize window
          self.driver.maximize_window()

     def login(self):
          #use try in login process
          try:
               #use wait some loading issues
               wait = WebDriverWait(self.driver, 20)
               wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys('Admin')
               time.sleep(1)
               self.driver.find_element(By.NAME, value="password").send_keys('admin123')
               time.sleep(1)
               self.driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
               print("logged in successfully")
          #No such element exception from login errors
          except NoSuchElementException as selenium_error:
               print("login errors ;\n",selenium_error)

     def shutdown(self):
          #close window
          time.sleep(4)
          self.driver.quit()
url='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
web1=webpage1(url)
web1.get_url()
web1.login()
web1.shutdown()
