"""Galaksi verisi üzerinde map/filter/reduce ve liste üreteci karşılaştırmaları."""

from functools import partial, reduce


def buyuk_harfli_adlar_map(galaksi: dict) -> list[str]:
    """Gezegen adlarını map ile büyük harfe çevirir."""
    return list(map(str.upper, galaksi["gezegenler"]))


def buyuk_harfli_adlar_liste(galaksi: dict) -> list[str]:
    """Gezegen adlarını liste üreteci ile büyük harfe çevirir."""
    return [gezegen.upper() for gezegen in galaksi["gezegenler"]]


def iki_baglantili_filter(galaksi: dict) -> list[str]:
    """En az iki bağlantısı olan gezegenleri filter ile bulur."""
    baglantilar = galaksi["baglantilar"]
    return list(filter(lambda g: len(baglantilar[g]) >= 2, galaksi["gezegenler"]))


def iki_baglantili_liste(galaksi: dict) -> list[str]:
    """En az iki bağlantısı olan gezegenleri liste üreteci ile bulur."""
    baglantilar = galaksi["baglantilar"]
    return [g for g in galaksi["gezegenler"] if len(baglantilar[g]) >= 2]


def toplam_baglanti_reduce(galaksi: dict) -> int:
    """Toplam bağlantı sayısını reduce ile hesaplar."""
    hedef_listeleri = galaksi["baglantilar"].values()
    return reduce(lambda toplam, hedefler: toplam + len(hedefler), hedef_listeleri, 0)


def toplam_baglanti_sum(galaksi: dict) -> int:
    """Toplam bağlantı sayısını sum ile hesaplar."""
    return sum(len(hedefler) for hedefler in galaksi["baglantilar"].values())


def yolculuk(mesafe: int, hiz: int = 1) -> float:
    """Verilen mesafeyi verilen hızla gitmek için gereken süreyi döndürür."""
    return mesafe / hiz


# partial: yolculuk fonksiyonunun hiz değerini 3 olarak sabitleyen yeni fonksiyon.
hizli_yolculuk = partial(yolculuk, hiz=3)

# Yorum: Bence liste üreteci ve sum daha okunaklı. map/filter/reduce içinde
# lambda ve iç içe çağrılar var, özellikle reduce'u okurken durup düşünmek gerekiyor.