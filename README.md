# HasarliAracTespiti

Hasarlı Araç Görsellerinden Hasar Tespiti

Bu proje, hasarlı araç görsellerinden hasar tespiti yapmak amacıyla geliştirilen bir görüntü işleme uygulamasıdır. İnternetten veri kazıma, veri işleme ve veri çoğaltma yöntemleri kullanılarak yapay zeka modelleri için uygun bir veri seti hazırlanmıştır.

Proje Özeti

Amaç: Hasarlı araç görsellerinden hasar tespiti yaparak hasar durumunu analiz etmek.

Veri Toplama:
	•	Web Crawler (Selenium ve BeautifulSoup) kullanılarak internetten araç görselleri kazındı.

Veri İşleme:
	•	Görsellerin parlaklık, kontrast ve boyut ayarları Pillow kütüphanesiyle düzenlendi.
	•	Veri seti genişletmek için görseller 90 derece döndürüldü.

Sonuç: İşlenmiş görseller, hasar tespiti analizlerinde kullanılmaya hazır hale getirildi.

Geliştirme Ortamı ve Kullanılan Teknolojiler

	•	Programlama Dili: Python
	•	Kütüphaneler:
	•	Selenium
	•	BeautifulSoup
	•	Pillow
	•	DateTime
	•	os
	•	requests
	•	io
	•	Diğer Araçlar:
	•	Anaconda Spyder (isteğe bağlı analiz ve testler için)
	•	Python 3.9+

 Projenin Yüklenmesi ve Çalıştırılması

Gereksinimler

	•	Python 3.9 veya üzeri
	•	Gerekli kütüphaneler

 Kurulum

	1.	Bu repoyu klonlayın:
 git clone https://github.com/kullaniciadi/HasarliAracTespiti.git
 cd HasarliAracTespiti

 	2.	Gerekli bağımlılıkları yükleyin:
  pip install -r requirements.txt

  Çalıştırma

	•	Veri Kazıma:
	•	Eğer site görselleri bir link içinde saklıyorsa:
  python genelCrawler.py

  •	Eğer site görselleri doğrudan <img> etiketi içinde saklıyorsa:
  python imgCrawler.py

  	•	Veri İşleme ve Çoğaltma:
	•	Görselleri işlemek için aşağıdaki komutu çalıştırın:
  python VeriArttirma.py

  
  Katkıda Bulunma

  Projeye katkıda bulunmak için pull request gönderin veya issue açın.

  Lisans

 Bu proje MIT Lisansı ile lisanslanmıştır.
