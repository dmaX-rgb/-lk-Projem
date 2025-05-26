import pygame
import sys
import random

pygame.init()

GENISLIK = 400
YUKSEKLIK = 600

ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
pygame.display.set_caption("Flappy Bird")

# Kuş resmi yükle
kus_resim = pygame.image.load("kus.png")
kus_x = 50
kus_y = 300
kus_hiz = 0
yercekimi = 0.5

# Boru ayarları
boru_genislik = 70
boru_hiz = 3
boru_araligi = 150  # üst ve alt boru arası boşluk

# Boruların ilk konumu (sağdan başlayacak)
boru_x = GENISLIK
boru_ust_yukseklik = random.randint(50, YUKSEKLIK - boru_araligi - 50)

clock = pygame.time.Clock()

while True:
    for etkinlik in pygame.event.get():
        if etkinlik.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if etkinlik.type == pygame.KEYDOWN:
            if etkinlik.key == pygame.K_SPACE:
                kus_hiz = -10

    # Kuş hareketi
    kus_hiz += yercekimi
    kus_y += kus_hiz
    if kus_y > YUKSEKLIK - kus_resim.get_height():
        kus_y = YUKSEKLIK - kus_resim.get_height()
        kus_hiz = 0
    if kus_y < 0:
        kus_y = 0
        kus_hiz = 0

    # Boru hareketi
    boru_x -= boru_hiz
    if boru_x < -boru_genislik:
        boru_x = GENISLIK
        boru_ust_yukseklik = random.randint(50, YUKSEKLIK - boru_araligi - 50)

    # Ekranı temizle
    ekran.fill((135, 206, 235))

    # Boruları çiz
    pygame.draw.rect(ekran, (0, 255, 0), (boru_x, 0, boru_genislik, boru_ust_yukseklik))  # üst boru
    pygame.draw.rect(ekran, (0, 255, 0), (boru_x, boru_ust_yukseklik + boru_araligi, boru_genislik, YUKSEKLIK))  # alt boru

    # Kuşu çiz
    ekran.blit(kus_resim, (kus_x, kus_y))

    # Çarpışma kontrolü
    kus_rect = pygame.Rect(kus_x, kus_y, kus_resim.get_width(), kus_resim.get_height())
    boru_ust_rect = pygame.Rect(boru_x, 0, boru_genislik, boru_ust_yukseklik)
    boru_alt_rect = pygame.Rect(boru_x, boru_ust_yukseklik + boru_araligi, boru_genislik, YUKSEKLIK)

    if kus_rect.colliderect(boru_ust_rect) or kus_rect.colliderect(boru_alt_rect):
        print("Çarpışma! Oyun bitti.")
        pygame.quit()
        sys.exit()

    pygame.display.update()
    clock.tick(60)

