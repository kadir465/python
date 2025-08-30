from selenium import webdriver  # Selenium kütüphanesini import eder (tarayıcı otomasyonu için)
import chromedriver_autoinstaller  # ChromeDriver otomatik yükleyici (Chrome sürümüne uygun driver indirir)
from time import sleep  # Bekleme süreleri koymak için sleep fonksiyonu import edilir

# ChromeDriver otomatik olarak kurulur (eğer yoksa indirir, varsa günceller)
chromedriver_autoinstaller.install()

# Chrome tarayıcısını başlatır
driver = webdriver.Chrome()

# İlk açılacak sayfanın URL’si
video_url = "https://www.instagram.com/aselsanyasam/"
driver.get(video_url)  # Belirtilen URL’yi açar

sleep(5)  # 5 saniye bekler (sayfanın yüklenmesi için zaman tanır)

# Tarayıcı penceresini tam ekran yapar
driver.maximize_window()

# Başka bir Instagram sayfasına gider
driver.get("https://www.instagram.com/k.emirycl/")
sleep(5)  # 5 saniye bekler

# Bir önceki sayfaya geri döner
driver.back()
sleep(5)  # 5 saniye bekler

# İleriye (sonraki sayfaya) gider
driver.forward()
sleep(5)  # 5 saniye bekler

# Sayfayı yeniler
driver.refresh()
sleep(2)  # 2 saniye bekler

# Yeni sekme açarak YouTube videosuna gider
driver.execute_script("window.open('https://www.youtube.com/watch?v=zL0ncCO9mZ0&list=PLrtq9RLZ4JXtkroLL4l6-1OajPuKM6x_Y&index=3');")
driver.switch_to.window(driver.window_handles[-1])  # Açılan yeni sekmeye geçiş yapar
sleep(5)  # 5 saniye bekler

# Yeni sekme açarak ChatGPT sitesine gider
driver.execute_script("window.open('https://chatgpt.com/');")
driver.switch_to.window(driver.window_handles[-1])  # Açılan yeni sekmeye geçiş yapar
sleep(5)  # 5 saniye bekler

# Aktif olan sekmeyi kapatır (ChatGPT sekmesi kapanır)
driver.close()

# Geriye kalan tüm tarayıcı pencerelerini kapatır (YouTube, Instagram ve diğer sekmeler kapanır)
driver.quit()
