# HasarliAracTespiti
Hasarlı Araç Görsellerinden Hasar Tespiti
Bu proje, hasarlı araç görselleri üzerinden hasar tespitine yönelik bir görüntü işleme uygulamasıdır. İnternetten veri kazıma, veri işleme ve veri çoğaltma yöntemleri kullanılarak yapay zeka modelleri için uygun bir veri seti hazırlanmıştır.

📌 Proje Özeti
Amaç: Hasarlı araç görsellerinden hasar tespiti yapmak.
Veri Toplama:
Web Crawler (Selenium ve BeautifulSoup) kullanılarak internetten görseller kazındı.
Veri İşleme:
Görsellerin parlaklık, kontrast ve boyut ayarları Pillow kütüphanesiyle yapıldı.
Görseller 90 derece döndürülerek veri seti genişletildi.
Sonuç: İşlenmiş görseller, hasar tespiti için analizlerde kullanılmaya hazır hale getirildi.
💻 Geliştirme Ortamı ve Kullanılan Teknolojiler
Programlama Dili: Python
Kütüphaneler:
Selenium
BeautifulSoup
Pillow
DateTime
os
requests
io
Diğer Araçlar:
Anaconda Spyder (isteğe bağlı analiz ve testler için)
Python 3.9+
🚀 Projenin Yüklenmesi ve Çalıştırılması
Gereksinimler
Python 3.9 veya üzeri sürüm
Gerekli kütüphaneler:
bash
Kodu kopyala
pip install -r requirements.txt
Kurulum
Bu repoyu klonlayın:

bash
Kodu kopyala
git clone https://github.com/kullaniciadi/HasarliAracTespiti.git
cd HasarliAracTespiti
Gerekli bağımlılıkları yükleyin:

bash
Kodu kopyala
pip install -r requirements.txt
Çalıştırma
Veri Kazıma:

Eğer site görselleri bir link içinde saklıyorsa:
bash
Kodu kopyala
python genelCrawler.py
Eğer site görselleri doğrudan <img> etiketi içinde saklıyorsa:
bash
Kodu kopyala
python imgCrawler.py
Veri İşleme ve Çoğaltma:
Görselleri işlemek için aşağıdaki komutu çalıştırın:

bash
Kodu kopyala
python VeriArttirma.py

Katkıda Bulunma
Projeye katkıda bulunmak için pull request gönderin veya issue açın.

📝 Lisans
Bu proje MIT Lisansı altında lisanslanmıştır.
