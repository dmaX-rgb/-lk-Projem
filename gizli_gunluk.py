dogru_sifre = "2780"
deneme_sayisi = 3

while deneme_sayisi > 0:
    girilen_sifre = input("Gizli Günlüğe Giriş için şifrenizi girin: ")
    
    if girilen_sifre == dogru_sifre:
        print("Giriş başarılı! Gizli günlüğe hoş geldiniz!")
        break
    else:
        deneme_sayisi -= 1
        if deneme_sayisi == 0:
            print("Deneme hakkınız doldu. Program sonlandırılıyor.")
            break
        else:
            print(f"Yanlış şifre! Kalan deneme hakkınız: {deneme_sayisi}")

