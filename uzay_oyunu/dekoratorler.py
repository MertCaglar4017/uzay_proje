"""Dekoratörler: süre ölçme, çağrı sayma, loglama ve aralık sınırlama."""

import time
from collections.abc import Callable
from functools import wraps


def sure_olc(fonksiyon: Callable) -> Callable:
    """Fonksiyonun çalışma süresini "ad: 0.0123 sn" biçiminde yazdırır."""

    @wraps(fonksiyon)
    def sarmalayici(*args, **kwargs):
        baslangic = time.perf_counter()
        sonuc = fonksiyon(*args, **kwargs)
        sure = time.perf_counter() - baslangic
        print(f"{fonksiyon.__name__}: {sure:.4f} sn")
        return sonuc

    return sarmalayici


if __name__ == "__main__":
    from uzay_oyunu.akis import rota_sayaci_onbelleksiz
    from uzay_oyunu.oyun import galaksi_yukle

    baglantilar = galaksi_yukle()["baglantilar"]
    olculen = sure_olc(rota_sayaci_onbelleksiz(baglantilar))
    print(olculen("dünya", 20))