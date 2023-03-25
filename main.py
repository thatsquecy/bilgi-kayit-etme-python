# Kullanıcıdan Ad, Soyad, Yaş ve Telefon Numarası bilgilerini isteyen bir program

ad = input("Adınız: ")
soyad = input("Soyadınız: ")
yas = input("Yaşınız: ")
tel = input("Telefon Numaranız: ")

# Bilgileri bir .txt dosyasına yazdırmak için dosya adını oluşturun ve verileri dosyaya yazın
dosya_adi = ad + "_" + soyad + "_bilgileri.txt"
with open(dosya_adi, "a") as f:
    f.write(ad + " " + soyad + ", " + yas + " yaşında, telefon numarası: " + tel + "\n")

# Kullanıcıya bilgi kaydedildiğini bildirin
print("Bilgiler kaydedildi.")
