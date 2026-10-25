"""Dekoratörler: süre ölçme, çağrı sayma, loglama ve aralık sınırlama."""

import inspect
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


def say(fonksiyon: Callable) -> Callable:
    """Fonksiyonun kaç kez çağrıldığını, fonksiyonun cagri niteliğinde sayar."""

    @wraps(fonksiyon)
    def sarmalayici(*args, **kwargs):
        sarmalayici.cagri += 1
        return fonksiyon(*args, **kwargs)

    sarmalayici.cagri = 0
    return sarmalayici


def log_cagri(fonksiyon: Callable) -> Callable:
    """Her çağrıdan önce adı ve argümanları, sonra dönüş değerini yazdırır."""

    @wraps(fonksiyon)
    def sarmalayici(*args, **kwargs):
        parcalar = [repr(arg) for arg in args]
        parcalar += [f"{ad}={deger!r}" for ad, deger in kwargs.items()]
        print(f"-> {fonksiyon.__name__}({', '.join(parcalar)})")
        sonuc = fonksiyon(*args, **kwargs)
        print(f"<- {fonksiyon.__name__} = {sonuc!r}")
        return sonuc

    return sarmalayici


def sinirla(alt: float, ust: float) -> Callable:
    """İlk argümanı [alt, ust] aralığında değilse ValueError fırlatan dekoratör."""

    def dekorator(fonksiyon: Callable) -> Callable:
        ilk_ad = list(inspect.signature(fonksiyon).parameters)[0]

        @wraps(fonksiyon)
        def sarmalayici(*args, **kwargs):
            if args:
                deger = args[0]
            elif ilk_ad in kwargs:
                deger = kwargs[ilk_ad]
            else:
                return fonksiyon(*args, **kwargs)
            if not alt <= deger <= ust:
                raise ValueError(
                    f"{fonksiyon.__name__}: {deger} değeri {alt}-{ust} aralığında değil"
                )
            return fonksiyon(*args, **kwargs)

        return sarmalayici

    return dekorator


if __name__ == "__main__":
    from uzay_oyunu.akis import rota_sayaci_onbelleksiz
    from uzay_oyunu.oyun import galaksi_yukle

    baglantilar = galaksi_yukle()["baglantilar"]
    olculen = sure_olc(rota_sayaci_onbelleksiz(baglantilar))
    print(olculen("dünya", 20))