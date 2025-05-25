while True:
    print("\n--- Not Defteri ---")
    print("1. Not Ekle")
    print("2. Notları Görüntüle")
    print("3. Çıkış")

    secim = input("Seçiminiz (1/2/3): ")

    if secim == "1":
        not_icerik = input("Notunuzu yazın: ")
        with open("notlar.txt", "a") as dosya:
            dosya.write(not_icerik + "\n")
        print("Not kaydedildi.")

    elif secim == "2":
        try:
            with open("notlar.txt", "r") as dosya:
                icerik = dosya.read()
                print("\nKaydedilen Notlar:\n")
                print(icerik)
        except FileNotFoundError:
            print("Henüz not bulunmuyor.")

    elif secim == "3":
        print("Not defteri kapatılıyor...")
        break

    else:
        print("Geçersiz seçim, tekrar deneyin.")


               