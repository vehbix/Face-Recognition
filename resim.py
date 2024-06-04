import cv2
import time

# Kamera kaynağını aç (genellikle 0, dahili kamera için)
cap = cv2.VideoCapture(0)

# Kaydedilecek resimlerin sayacı
counter = 0

while True:
    # Kameradan bir kare oku
    ret, frame = cap.read()
    
    if not ret:
        break

    # Resmi kaydet
    filename = f"gelen/frame_.jpg"
    cv2.imwrite(filename, frame)
    print(f"{filename} kaydedildi.")

    # Bir saniye bekle
    time.sleep(1)
    counter += 1

    # q tuşuna basıldığında döngüyü kır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı serbest bırak
cap.release()
cv2.destroyAllWindows()
