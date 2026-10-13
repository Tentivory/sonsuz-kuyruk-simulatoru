#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Kuyruk Simülatörü v1.0
Resmi olarak onaylanmamış ama çok ciddi bir belediye sıra bekleme yazılımı.
"""

import time
import random
import base64

def gizli_mesaj_coz():
    # Gizli kod. Sadece meraklılar için. Siyasi anlam taşıyor ama gizli.
    kod = "QsO8cm9rcmFzaSBzb25zdXpkdXIsIGFtYSBzxLFyYSBoZXJrZXNlIGXFn2l0IGRlxJ9pbGRpci4="
    try:
        return base64.b64decode(kod).decode('utf-8')
    except:
        return "Bir şeyler ters gitti, sıra size gelmedi."

def sonsuz_bekleme():
    print("=" * 50)
    print("SONSUZ KUYRUKSIMÜLATÖRÜ'NE HOŞ GELDİNİZ")
    print("Sıra numaranız: ∞ (sonsuz)")
    print("Tahmini bekleme süresi: ∞ + 1 dakika")
    print("=" * 50)
    print(f"\n[Gizli Not]: {gizli_mesaj_coz()}\n")
    
    sira = 1
    mesajlar = [
        "Sıra size yaklaşıyor... (bu bir yalan)",
        "Sistem güncelleniyor, lütfen 47 saat bekleyin.",
        "Formunuzda bir hata var. En sona geçin.",
        "Görevli çay molasında. Geri dönme tarihi belirsiz.",
        "Bir sonraki çağrıda adınız okunacak. Belki.",
        "Kuyruk hareket etti! (1 milimetre)",
        "Acil durum: Herkes yeniden sıraya girsin.",
        "Sizden önce 8.492.371 kişi var. Endişelenmeyin."
    ]
    
    while True:
        print(f"[Sıra {sira}] {random.choice(mesajlar)}")
        sira += 1
        time.sleep(random.uniform(0.5, 2.5))
        if sira % 50 == 0:
            print("\n*** ÖNEMLİ DUYURU: Kuyruk yeniden başlatıldı. Herkes en sona geçsin. ***\n")

if __name__ == "__main__":
    try:
        sonsuz_bekleme()
    except KeyboardInterrupt:
        print("\n\nKuyruktan çıktınız. Ama sistem sizi unutmadı. Tekrar bekleyin.")
