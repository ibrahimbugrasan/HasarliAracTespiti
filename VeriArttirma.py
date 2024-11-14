import os
from PIL import Image, ImageEnhance
from datetime import datetime

input_folder = r"/Users/ibrahimbugrasan/Desktop/BütünVeriler/Kazali_Arac_Resimleri"
output_folder = r"/Users/ibrahimbugrasan/Desktop/AyrısmısVeriler"

os.makedirs(output_folder, exist_ok=True)

def process_image(image_path, output_folder):
    try:
        img = Image.open(image_path)
        
        # Benzersiz isim için zaman damgası
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
        base_name = os.path.splitext(os.path.basename(image_path))[0]
        
        # Yeniden boyutlandırma
        resized_img = img.resize((224, 224))
        resized_path = os.path.join(output_folder, f"{base_name}_resized_{timestamp}.jpg")
        resized_img.save(resized_path)

        # Parlaklık artırma
        enhancer_brightness = ImageEnhance.Brightness(resized_img)
        bright_img = enhancer_brightness.enhance(1.5)
        bright_path = os.path.join(output_folder, f"{base_name}_bright_{timestamp}.jpg")
        bright_img.save(bright_path)

        # Kontrast artırma
        enhancer_contrast = ImageEnhance.Contrast(resized_img)
        contrast_img = enhancer_contrast.enhance(1.5)
        contrast_path = os.path.join(output_folder, f"{base_name}_contrast_{timestamp}.jpg")
        contrast_img.save(contrast_path)

        # 90 Derece döndürme işlemleri
        # Her döndürmeden sonra siyah arka plan sorununu engellemek için, yeni görsellerde şeffaf arka plan kullanıyoruz
        for i in range(1, 4):
            rotated_img = resized_img.rotate(90 * i, expand=True, fillcolor=(255, 255, 255))  # beyaz arka plan
            rotated_path = os.path.join(output_folder, f"{base_name}_rotated_{i}_{timestamp}.jpg")
            rotated_img.save(rotated_path)

        print(f"Tamamlandı: {image_path}")

    except Exception as e:
        print(f"İşlenirken hata oluştu: {image_path} - Hata: {e}")

# Tüm görüntüleri işleme
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        image_path = os.path.join(input_folder, filename)
        process_image(image_path, output_folder)