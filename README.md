# Face Recognition Project

This project is a Python application designed to recognize faces in images located 
in a specific folder and store the information of recognized faces in JSON format.

## Installation

Follow these steps to run the project:

1. **Install Python**: Ensure that Python 3.6 or above is installed on your computer.
2. **Install Required Libraries**: Install the required Python libraries for the project:
     ```bash
     pip install -r requirements.txt
     ```

## Usage

To run the application, execute the following command in your terminal or command prompt:

 ```bash
 python main.py
 ```

When executed, the application scans images in a specific folder, recognizes faces and 
their confidence levels. This information is then saved to the images.json file.

## File Structure
- `main.py`: The main application file.
- `faces`: The folder containing target faces for recognition.
- `find`: The folder where recognized faces are saved.
- `images.json`: The file that stores information of recognized faces in JSON format.

## Example Outputs
Face recognition results are as follows:
```
['Elon.jpg']
['.stfolder']
No image
...
Elon.jpg 99.42% found
```

The information of recognized faces is saved in the images.json file:
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

## Images
 Some sample images obtained during the project:

Recognized Face: `./faces/Elon.jpg`

Post-Recognition Image: `./find/2024-05-22 14.15.58 Elon.jpg`

JSON File Structure: `./find/images.json`

## Conclusion and Evaluation
This project demonstrates a practical application of face recognition algorithms. 
The application is capable of detecting faces in specific folders with high accuracy and 
organizing the information effectively.

Future work on the project could involve testing on larger datasets and integrating different 
face recognition algorithms to improve performance and accuracy.







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

Tanınan Yüz: 
![jpg]/faces/Elon.jpg)

Tanıma Sonrası Görsel: 
![jpg]/faces/2024-05-22 14.15.58 Elon.jpg)

JSON Dosya Yapısı: `./find/images.json`

## Sonuç ve Değerlendirme
Bu proje, yüz tanıma algoritmalarının pratik bir uygulamasını göstermektedir. Yüksek doğruluk oranı ile tanıma yapabilen uygulama, belirli klasörlerdeki yüzleri tespit ederek, bilgilerini organize bir şekilde saklayabilmektedir.

Projenin daha ileri aşamalarda, daha büyük veri kümeleri üzerinde test edilmesi ve farklı yüz tanıma algoritmalarının entegre edilmesi, performansının ve doğruluk oranının artırılmasına yardımcı olabilir.


