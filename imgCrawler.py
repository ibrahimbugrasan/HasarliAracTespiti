#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 03:34:31 2024

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
download_folder = '/Users/ibrahimbugrasan/Desktop/KazalıArabaResimleriCIZIK'

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
base_url = "https://www.istockphoto.com/tr/search/2/image-film?phrase=scratched%20car"
#https://www.istockphoto.com/tr/search/2/image-film?page=2&phrase=scratched%20car
#https://www.istockphoto.com/tr/search/2/image-film?page=3&phrase=scratched%20car



# Webdriver'ı başlat
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

# İndirilmesi istenen sayfa sayısı
num_pages = 3 # Kaç sayfa taranacağı belirleniyor

# Tüm sayfalarda döngü
for page in range(1, num_pages + 1):
    if page == 1:
        url = base_url
    else:
        url = f'https://www.istockphoto.com/tr/search/2/image-film?page={page}&phrase=scratched%20car'

    print(f"Sayfa açılıyor: {url}")
    driver.get(url)

    # Sayfanın tamamen yüklenmesini bekle
    time.sleep(5)

    # Dinamik olarak yüklenen içerikleri almak için sayfa sonuna kadar kaydırma işlemi
    scroll_pause_time = 5
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Sayfanın HTML içeriğini al
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Sayfadaki tüm resimleri bul
    img_tags = soup.find_all('img')
    print(f"{len(img_tags)} resim bulundu.")

    for index, img_tag in enumerate(img_tags):
        real_img_url = img_tag.get('data-src') or img_tag.get('src')

        # Geçerli bir URL kontrolü
        if real_img_url and real_img_url.startswith(('http://', 'https://')):
            print(f"İndiriliyor: {real_img_url}")
            response = requests.get(real_img_url)

            if response.status_code == 200:
                try:
                    image = Image.open(BytesIO(response.content)).convert("RGB")
                    image = image.resize((512, 512))
                    image.save(os.path.join(download_folder, f'image_{page}_{index}.jpg'), 'JPEG')
                    print(f"{real_img_url} 512x512 boyutunda indirildi.")
                except Exception as e:
                    print(f"Hata: Resim işlenirken bir sorun oluştu. {e}")
            else:
                print(f"Hata: {real_img_url} indirilemedi, durum kodu: {response.status_code}")
        else:
            print("Hata: Geçersiz resim URL'si veya URL bulunamadı.")

# Tarayıcıyı kapat
driver.quit()