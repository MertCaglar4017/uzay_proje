"""Yardımcı fonksiyonlar."""

import time
from collections.abc import Callable


def yakit_ekle(miktar: int, depo: list[int] | None = None) -> list[int]:
    """Miktarı depoya ekler; depo verilmezse her çağrıda yeni bir liste açar."""
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo


def hamle_sayaci() -> Callable[[], int]:
    """Her çağrıldığında bir artan değer döndüren bir sayaç fonksiyonu üretir."""
    sayi = 0

    def say() -> int:
        nonlocal sayi
        sayi += 1
        return sayi

    return say


def en_bagli_gezegenler(galaksi: dict) -> list[str]:
    """Gezegenleri bağlantı sayısına göre azalan, eşitlikte alfabetik sıralar."""
    baglantilar = galaksi["baglantilar"]
    return sorted(
        galaksi["gezegenler"],
        key=lambda gezegen: (-len(baglantilar[gezegen]), gezegen),
    )


def sure_olc(fonksiyon: Callable) -> Callable:
    """Verilen fonksiyonun çalışma süresini yazan bir sarmalayıcı döndürür."""

    def sarmalayici(*args, **kwargs):
        baslangic = time.perf_counter()
        sonuc = fonksiyon(*args, **kwargs)
        sure = time.perf_counter() - baslangic
        print(f"{fonksiyon.__name__} {sure:.6f} saniyede çalıştı")
        return sonuc

    return sarmalayici


if __name__ == "__main__":
    from uzay_oyunu.oyun import galaksi_yukle

    en_bagli_gezegenler = sure_olc(en_bagli_gezegenler)
    print(en_bagli_gezegenler(galaksi_yukle()))