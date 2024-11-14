#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 02:19:22 2024

@author: ibrahimbugrasan
"""

import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from PIL import Image
from io import BytesIO

# Resimlerin kaydedileceği klasör
download_folder = '/Users/ibrahimbugrasan/Desktop/KazalıArabaResimleriSAHİBİNDENyeni12'

# Klasörü oluştur
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# ChromeDriver yolu
chrome_driver_path = "/Users/ibrahimbugrasan/Desktop/chromedriver-mac-arm64/chromedriver"

# ChromeDriver ayarları
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Tarayıcıyı görünmez yapmak için
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36")

# Base URL belirleme
base_url = "https://www.sahibinden.com/kategori-vitrin?viewType=Gallery&category=3538"
#https://www.sahibinden.com/kategori-vitrin?viewType=Gallery&pagingOffset=20&category=3538


# Webdriver'ı başlat
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

# İndirilmesi istenen sayfa sayısı
num_pages = 2  # Kaç sayfa taranacağı belirleniyor

# Tüm sayfalarda döngü
for page in range(1, num_pages + 1):  # Sayfa numarası 1'den başlıyor
    if page == 1:
        url = base_url
    else:
        url = f'https://www.sahibinden.com/kategori-vitrin?viewType=Gallery&pagingOffset=20&category=3538'  # page numarası ekleniyor

    print(f"Sayfa açılıyor: {url}")
    driver.get(url)

    # Sayfanın tamamen yüklenmesini bekle
    time.sleep(5)

    # Dinamik olarak yüklenen içerikleri almak için sayfa sonuna kadar kaydırma işlemi
    scroll_pause_time = 3  # Kaydırma sonrası bekleme süresi
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Sayfanın en altına kaydır
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Sayfanın yüklenmesini bekle
        time.sleep(scroll_pause_time)

        # Yeni yükseklik ile eski yüksekliği karşılaştır
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break  # Sayfa sonuna ulaşıldıysa döngüden çık
        last_height = new_height

    # Sayfanın HTML içeriğini al
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Resimleri bul
    image_links = soup.find_all('a',class_="classifiedTitle")
    print(f"{len(image_links)} resim bağlantısı bulundu.")  # Toplam resim sayısını yazdır

    for index, link in enumerate(image_links):
        # Resim detay sayfasının URL'sini al
        img_page_url = link.get('href')

        # URL'nin tam halini oluştur
        if img_page_url and img_page_url.startswith('/'):
            img_page_url = "https://www.sahibinden.com" + img_page_url

        if img_page_url:
            print(f"Resim detay sayfası açılıyor: {img_page_url}")
            driver.get(img_page_url)
            time.sleep(5)  # Sayfanın tamamen yüklenmesini bekle

            # Detay sayfasındaki tüm resim URL'lerini al
            img_soup = BeautifulSoup(driver.page_source, 'html.parser')
            img_tags = img_soup.find_all('img')  # Doğru class ismi kontrol edilmeli

            # Sayfadaki her bir resim için döngü
            for img_tag in img_tags:
                # Resim URL'sini 'data-src' veya 'src' özniteliğinden al
                real_img_url = img_tag.get('data-src') or img_tag.get('src')

                if real_img_url:
                    print(f"İndiriliyor: {real_img_url}")  # İndirme işlemi için bildirim
                    response = requests.get(real_img_url)

                    # İndirme işlemi başarılı mı kontrol et
                    if response.status_code == 200:
                        try:
                            # Resmi Pillow kullanarak aç
                            image = Image.open(BytesIO(response.content)).convert("RGB")  # Uyumluluk için RGB'ye çevir
                            image = image.resize((512, 512))

                            # Resmi dosya olarak kaydet
                            image.save(os.path.join(download_folder, f'image_{page}_{index}.jpg'), 'JPEG')
                            print(f"{real_img_url} 512x512 boyutunda indirildi.")
                        except Exception as e:
                            print(f"Hata: Resim işlenirken bir sorun oluştu. {e}")
                    else:
                        print(f"Hata: {real_img_url} indirilemedi, durum kodu: {response.status_code}")
                else:
                    print("Hata: Resim bulunamadı.")  # Resim etiketi bulunamadı
        else:
            print("Geçersiz URL.")  # Geçersiz URL durumu

# Tarayıcıyı kapat
driver.quit()