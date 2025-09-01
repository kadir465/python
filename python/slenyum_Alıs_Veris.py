from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import chromedriver_autoinstaller
from instagram_info import usurname0, password0,lastName,firstName,posta

chromedriver_autoinstaller.install()

class OtoShop():
    def __init__(self, usurname0, password0,lastName,firstName,posta):
        self.driver = webdriver.Chrome()
        self.usurname0 = usurname0
        self.password0 = password0
        self.firstName=firstName
        self.lastName=lastName
        self.posta=posta

    def signIn(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        
        wait = WebDriverWait(self.driver, 15)
        usurname_input = wait.until(EC.presence_of_element_located((By.ID,'user-name')))
        password_input = self.driver.find_element(By.ID,'password')

        usurname_input.send_keys(self.usurname0)
        password_input.send_keys(self.password0)
        password_input.send_keys(Keys.ENTER)

        time.sleep(3)  # sayfanın yüklenmesi için bekle

    def shop(self):
        # Ürün isimleri ve fiyat WebElementleri
        self.products = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        price_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")

        # Fiyatları float listesine çevir
        self.price = [float(p.text.replace("$","")) for p in price_elements]

        # Dosyaya yaz
        with open("shoping_list.txt", "w", encoding="utf-8") as file:
            for i in range(len(self.products)):
                line = f"{i+1}. ürün adı : {self.products[i].text} | fiyatı : {self.price[i]}\n"
                file.write(line)

        # En pahalı ürünü bul
        max_price = max(self.price)
        max_index = self.price.index(max_price)
        print(f"{max_index} En pahalı ürün: {self.products[max_index].text} | Fiyat: ${max_price}")
        
        add_buttons = self.driver.find_elements(By.CLASS_NAME, "btn")
        add_buttons[max_index].click()
        print(f"{self.products[max_index].text} sepete eklendi!")

        time.sleep(3)

        self.shop_button=self.driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
        time.sleep(2)
        self.check_button=self.driver.find_element(By.NAME,"checkout").click()
        time.sleep(2)
        self.firstName_input=self.driver.find_element(By.NAME,"firstName")
        self.lastName_input=self.driver.find_element(By.NAME,"lastName")
        self.posta_input=self.driver.find_element(By.NAME,"postalCode")

        self.firstName_input.send_keys(self.firstName)
        self.lastName_input.send_keys(self.lastName)
        self.posta_input.send_keys(self.posta)
        time.sleep(3)
        self.contiun=self.driver.find_element(By.NAME,"continue").click()
        time.sleep(5)

        self.driver.quit()


# Çalıştır
shoping = OtoShop(usurname0, password0,lastName,firstName,posta)
shoping.signIn()
shoping.shop()
