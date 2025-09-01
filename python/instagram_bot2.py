from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import chromedriver_autoinstaller
from instagram_info import username, password

chromedriver_autoinstaller.install()

class Instagram:
    def __init__(self, username, password):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.username = username
        self.password = password

    def signIn(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        self.driver.maximize_window()
        
        try:
            # Çerezleri kabul et (eğer çıkarsa)
            try:
                cookie_accept = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Allow')]"))
                )
                cookie_accept.click()
            except:
                pass
            
            wait = WebDriverWait(self.driver, 15)
            username_input = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
            password_input = self.driver.find_element(By.NAME, 'password')
            
            username_input.send_keys(self.username)
            password_input.send_keys(self.password)
            password_input.send_keys(Keys.ENTER)
            
            # 'Şimdi Değil' varsa tıkla
            try:
                not_now_btn = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))
                )
                not_now_btn.click()
            except:
                pass
            
            time.sleep(5)
            
        except Exception as e:
            print(f"Giriş hatası: {str(e)}")
            self.driver.quit()

    def get_followers(self):
      try:
        # Profil sayfasına git
        self.driver.get(f"https://www.instagram.com/{self.username}/")
        time.sleep(3)
        
        # Takipçiler düğmesini bul ve tıkla
        followers_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//a[contains(@href, '/{self.username}/followers/')]"))
        )
        followers_btn.click()
        time.sleep(2)
        
        # Takipçiler dialog kutusunu bekle
        dialog = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "x6nl9eh "))
        )
        
        followers_container = dialog
        followers_set = set()
        last_height = self.driver.execute_script("return arguments[0].scrollHeight", followers_container)
        scroll_attempts = 0
        
        while scroll_attempts < 10:
            # Container'ın en altına scroll yap
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_container)
            time.sleep(2)
            
            # Takipçi isimlerini al
            followers_elements = followers_container.find_elements(By.CSS_SELECTOR,"div.x6nl9eh  div.x1rg5ohu")
            for element in followers_elements:
                username_text = element.text
                if username_text:
                    followers_set.add(username_text)
            
            # Scroll yüksekliği değişmedi mi kontrol et
            new_height = self.driver.execute_script("return arguments[0].scrollHeight", followers_container)
            if new_height == last_height:
                scroll_attempts += 1
            else:
                last_height = new_height
                scroll_attempts = 0
        
        # Takipçileri yazdır
        for i, follower in enumerate(followers_set, 1):
            print(f"{i}. {follower}")
        
        print(f"\nToplam takipçi sayısı: {len(followers_set)}")
    
      except Exception as e:
        print(f"Hata oluştu: {str(e)}")
      finally:
        self.driver.quit()


# Kodu çalıştır
if __name__ == "__main__":
    instagram = Instagram(username, password)
    instagram.signIn()
    instagram.get_followers()