from selenium import webdriver # selnyum mödülünde tarayıcı kütüphanessinde web otomasyonu sağlar
from selenium.webdriver.common.by import By # web siteleri üzerinden web sitelerinde erişimleri sağlar 
from selenium.webdriver.support.ui import WebDriverWait  
# WebDriverWait -> Belirtilen süre boyunca bir koşulun gerçekleşmesini beklemek için kullanılır.  
# Örneğin: bir elementin görünmesini, tıklanabilir olmasını vb. bekleyebilirsin.  

from selenium.webdriver.support import expected_conditions as EC  
# expected_conditions (EC) -> Sık kullanılan hazır koşulları içerir.  
# Örneğin: EC.presence_of_element_located -> element DOM’da var mı?  
#          EC.visibility_of_element_located -> element görünüyor mu?  
#          EC.element_to_be_clickable -> element tıklanabilir mi?  

from selenium.webdriver.common.keys import Keys # tuşlara etkileşimleri sağlar tıklama işlemlerini sağlar
import time# time modülü indirim zamansam işlemleri yapar
import chromedriver_autoinstaller # Chromedriver otomtik yükleme import eder
from instagram_info import usurname0, password0,lastName,firstName,posta #instagram_info sayfasında bilgileri ister 

chromedriver_autoinstaller.install()# güncel olan chrome driver ı indirir

class OtoShop():
    def __init__(self, usurname0, password0,lastName,firstName,posta):
        self.driver = webdriver.Chrome()# webdeiverı driver a atar direver üzerinden işlem  yapar
        self.usurname0 = usurname0
        self.password0 = password0
        self.firstName=firstName
        self.lastName=lastName
        self.posta=posta

    def signIn(self):
        self.driver.get("https://www.saucedemo.com/")#adresi alır ve adrese gider
        self.driver.maximize_window()#sayfayı tam ekran yapar
        
   wait = WebDriverWait(self.driver, 15)  # WebDriverWait -> 15 saniyeye kadar bekler, şart sağlanırsa daha erken devam eder.
username_input = wait.until(EC.presence_of_element_located((By.ID,'user-name')))# 'user-name' ID'li element DOM'da var olana kadar bekler. Bulunca username_input'a atar.
password_input = self.driver.find_element(By.ID,'password')  # 'password' ID'li elementi anında bulmaya çalışır (explicit wait kullanılmadı).

        usurname_input.send_keys(self.usurname0)#usur name inputa kayıtlı olan usurt name i atar
        password_input.send_keys(self.password0)
        password_input.send_keys(Keys.ENTER)#şifredeyken entere tıklama yapar

        time.sleep(3)  # sayfanın yüklenmesi için bekle

    def shop(self):
        # Ürün isimleri ve fiyat WebElementleri
        self.products = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")#class ismi bu olan elemanti bulur ve string listesi halinde buna aktarır
        price_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")#

        # Fiyatları float listesine çevir
        self.price = [float(p.text.replace("$","")) for p in price_elements]#**string listesini float veri tipine çevirir

        # Dosyaya yaz
        with open("shoping_list.txt", "w", encoding="utf-8") as file:#dosya açar ve yazma modülü ile
            for i in range(len(self.products)):#product listesi boyutu kadar döner
                line = f"{i+1}. ürün adı : {self.products[i].text} | fiyatı : {self.price[i]}\n"
                file.write(line) #dosyaya yazma işlemi sağlanır

        # En pahalı ürünü bul
        max_price = max(self.price)#dizide max değeri bulur bu fonksiiyon sayesde
        max_index = self.price.index(max_price)#dizide iistenilen elemanın adresini bulur
        print(f"{max_index} En pahalı ürün: {self.products[max_index].text} | Fiyat: ${max_price}")
        
        add_buttons = self.driver.find_elements(By.CLASS_NAME, "btn")
        add_buttons[max_index].click()
        print(f"{self.products[max_index].text} sepete eklendi!")

        time.sleep(3)

        self.shop_button=self.driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()#sayfada bu clas adında isime sahip bir nesneye tıklama yapar
        time.sleep(2)
        self.check_button=self.driver.find_element(By.NAME,"checkout").click()#sayfada bu isme sahip nesneyi bulur ve tıklama yapar
        time.sleep(2)
        self.firstName_input=self.driver.find_element(By.NAME,"firstName")#firstname_input kısmına sayfada bu işsme sahip nesneyi atar
        self.lastName_input=self.driver.find_element(By.NAME,"lastName")
        self.posta_input=self.driver.find_element(By.NAME,"postalCode")

        self.firstName_input.send_keys(self.firstName)#firstname_input kısmına dah önceden tanımlanmış fırstnamei atar
        self.lastName_input.send_keys(self.lastName)
        self.posta_input.send_keys(self.posta)
        time.sleep(3)
        self.contiun=self.driver.find_element(By.NAME,"continue").click()
        time.sleep(5)

        self.driver.quit()#driverı kapatır


# Çalıştır
shoping = OtoShop(usurname0, password0,lastName,firstName,posta)
shoping.signIn()
shoping.shop()

