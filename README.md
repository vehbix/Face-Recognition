# Yüz Tanıma Projesi

Bu proje, belirli bir klasörde bulunan resimler içerisindeki yüzleri tanıyarak, tanınan yüzlerin bilgilerini JSON formatında saklamayı amaçlayan bir Python uygulamasıdır.

## Kurulum

Projeyi çalıştırmak için aşağıdaki adımları izleyin:

1. **Python Kurulumu**: Python 3.6 veya üzeri bir sürümün bilgisayarınıza kurulu olduğundan emin olun.
2. **Gerekli Kütüphanelerin Yüklenmesi**: Proje için gerekli olan Python kütüphanelerini yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

## Kullanım

Uygulamayı çalıştırmak için terminal veya komut istemcisinde aşağıdaki komutu çalıştırın:

```bash
python main.py
```
Çalıştırıldığında, belirli bir klasördeki resimleri tarayarak, tanıdığı yüzleri ve bu yüzlerin doğruluk oranlarını tespit eder. Bu bilgiler, daha sonra images.json dosyasına kaydedilir.

## Dosya Yapısı
- `main.py`: Ana uygulama dosyası.
- `faces`: Yüz tanıma için kullanılacak hedef yüzlerin bulunduğu klasör.
- `find`: Tanınan yüzlerin kaydedildiği klasör.
- `images.json`: Tanınan yüzlerin bilgilerini JSON formatında saklayan dosya.
Örnek Çıktılar
Yüz tanıma sonuçları aşağıdaki gibidir:
 ```
['Elon.jpg']
['.stfolder']
Resim yok
...
Elon.jpg 99.42% bulundu
 ```
Tanınan yüzlerin bilgileri images.json dosyasına kaydedilir:
 ```
{
    "images1": {
        "date": "2024-05-22",
        "time": " 14.15.58",
        "name": " Elon",
        "path": "2024-05-22 14.15.58 Elon.jpg"
    },
    "images2": {
        "date": "2024-05-22",
        "time": " 14.16.11",
        "name": " Elon",
        "path": "2024-05-22 14.16.11 Elon.jpg"
    },
    "images3": {
        "date": "2024-06-04",
        "time": " 11.55.09",
        "name": " Elon",
        "path": "2024-06-04 11.55.09 Elon.jpg"
    },
    "images4": {
        "date": "2024-06-04",
        "time": " 11.55.21",
        "name": " Elon",
        "path": "2024-06-04 11.55.21 Elon.jpg"
    }
}
 ```
## Görseller
Proje kapsamında elde edilen bazı örnek görseller:

Tanınan Yüz: ![jpg]/faces/Elon.jpg)

Tanıma Sonrası Görsel: ![jpg]/faces/2024-05-22 14.15.58 Elon.jpg)

JSON Dosya Yapısı: `./find/images.json`

## Sonuç ve Değerlendirme
Bu proje, yüz tanıma algoritmalarının pratik bir uygulamasını göstermektedir. Yüksek doğruluk oranı ile tanıma yapabilen uygulama, belirli klasörlerdeki yüzleri tespit ederek, bilgilerini organize bir şekilde saklayabilmektedir.

Projenin daha ileri aşamalarda, daha büyük veri kümeleri üzerinde test edilmesi ve farklı yüz tanıma algoritmalarının entegre edilmesi, performansının ve doğruluk oranının artırılmasına yardımcı olabilir.


