from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
from time import sleep

chromedriver_autoinstaller.install()

driver=webdriver.Chrome()
site_url="https://www.monsternotebook.com.tr/?gad_source=1&gad_campaignid=22035761177&gbraid=0AAAAADnm1x8ZH7_UAWkWGvnVBqoyzyl_S&gclid=EAIaIQobChMI8K7b6N-0jwMV94r9BR2gMC5QEAAYASAAEgJPZPD_BwE"
driver.get(site_url)
sleep(2)

search_box=driver.find_element(By.NAME,"q")#arama kutusunu bulur bu değer her html kodu için arklı olabilir
search_box.send_keys("abra")# arama kutusuna yazı gönderir
search_box.send_keys(Keys.ENTER)# enter tuşuna basar

laptop_name = driver.find_elements(By.CSS_SELECTOR, ".product-list-wrapper h3")#elements sayasenide bir liste oluşturur bu birden çok nesneler için kullanılır
#**burda büyük bir class ın sahip olduğu alt kılaslarının sadece h3 etiketli kısmı yazzdırıldı 

laptop_price=driver.find_elements(By.CLASS_NAME,"fs-24")


print("=======================================================")
for i in range(len(laptop_name)):
    print(f"{i+1}. ürün adı: {laptop_name[i].text}")
    print(f"{i+1}. ürün fiyatı: {laptop_price[i].text}")
    print("==========================================")

sleep(4)
driver.quit()
