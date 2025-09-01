from selenium import webdriver
import time
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from instagram_info import username,password

chromedriver_autoinstaller

site_url="https://www.instagram.com/accounts/login/"

class Instagram:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        self.driver.get("https://www.instagram.com/")
        self.driver.maximize_window()
        
        wait = WebDriverWait(self.driver, 15)
        usernameInput = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
        passwordInput = self.driver.find_element(By.NAME, 'password')

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)

        # Ana ekranın yüklenmesini bekle
        time.sleep(15)


    def GetFallowers(self):
        profile_link = self.driver.find_element(By.XPATH, "//a[contains(@href, '/{}/')]".format(self.username))
        profile_link.click()
        time.sleep(6)

        fallowing_button=self.driver.find_element(By.XPATH,f"//a[contains(@href, '/{self.username}/followers')]").click()
        time.sleep(6)

        fallowers_elements=self.driver.find_elements(By.CSS_SELECTOR,"div.x6nl9eh  div.x1rg5ohu")
        
        fallowers=[]

        for i in fallowers_elements:
            name=i.text.strip()
            if name and name not in fallowers:
                fallowers.append(name)
            
        
        for j,name in enumerate(fallowers,start=1):
            print(f"{j}. takipçi: {name}")
            
     


instagram = Instagram(username, password)
instagram.signIn()
instagram.GetFallowers()
