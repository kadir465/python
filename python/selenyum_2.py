from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
from time import sleep

chromedriver_autoinstaller.install()

driver=webdriver.Chrome()
site_url="https://www.monsternotebook.com.tr/?gad_campaignid=22035761177"
driver.get(site_url)
sleep(2)

search_box=driver.find_element(By.NAME,"q")#arama kutusunu bulur bu değer her html kodu için arklı olabilir
search_box.send_keys("abra")# arama kutusuna yazı gönderir
search_box.send_keys(Keys.ENTER)# enter tuşuna basar

game_name = driver.find_elements(By.CSS_SELECTOR, ".product-list-wrapper h3")#elements sayasenide bir liste oluşturur bu birden çok nesneler için kullanılır
#**burda büyük bir class ın sahip olduğu alt kılaslarının sadece h3 etiketli kısmı yazzdırıldı 


for i in range(len(game_name)):#bir liste olduğu için len ile uzunluğu bulunur ve döngüye sokulur
    print(f"{i+1} oyun adı:  {game_name[i].text}")#text ile sadece yazı kısmı alınır
sleep(4)
driver.quit()