"""Üreteçler, veri akışları ve önbellekli hesaplar."""

import time
from collections.abc import Callable, Iterable, Iterator
from functools import lru_cache
from pathlib import Path


def fibonacci() -> Iterator[int]:
    """Sonsuz fibonacci dizisini (0, 1, 1, 2, ...) sırayla üretir."""
    onceki, simdiki = 0, 1
    while True:
        yield onceki
        onceki, simdiki = simdiki, onceki + simdiki


def yakit_gostergesi(yakit: int, tuketim: int) -> Iterator[int]:
    """Her adımda yakıtı tüketim kadar azaltıp kalanı üretir; 0'a inince durur."""
    while yakit > 0:
        yakit = max(yakit - tuketim, 0)
        yield yakit


def satirlari_oku(yol: str | Path) -> Iterator[str]:
    """Dosyayı satır satır okur; boş ve # ile başlayan satırları atlar."""
    with open(yol, encoding="utf-8") as dosya:
        for satir in dosya:
            satir = satir.strip()
            if satir and not satir.startswith("#"):
                yield satir


def ayristir(satirlar: Iterable[str]) -> Iterator[tuple[str, str, int]]:
    """Her "kaynak -> hedef yakit" satırından (kaynak, hedef, yakit) demeti üretir."""
    for satir in satirlar:
        kaynak, _, hedef, yakit = satir.split()
        yield kaynak, hedef, int(yakit)


def uzun_yolculuklar(
    kayitlar: Iterable[tuple[str, str, int]], esik: int
) -> Iterator[tuple[str, str, int]]:
    """Yakıtı eşikten büyük olan kayıtları süzer."""
    for kaynak, hedef, yakit in kayitlar:
        if yakit > esik:
            yield kaynak, hedef, yakit


def rota_sayaci(baglantilar: dict[str, list[str]]) -> Callable[[str, int], int]:
    """Önbellekli bir rota_sayisi(gezegen, adim) fonksiyonu döndürür."""

    @lru_cache(maxsize=None)
    def rota_sayisi(gezegen: str, adim: int) -> int:
        """Gezegenden başlayıp tam adim yolculuk yapan farklı rotaların sayısı."""
        if adim == 0:
            return 1
        return sum(rota_sayisi(hedef, adim - 1) for hedef in baglantilar[gezegen])

    return rota_sayisi


def rota_sayaci_onbelleksiz(
    baglantilar: dict[str, list[str]],
) -> Callable[[str, int], int]:
    """rota_sayaci ile aynı hesabı önbellek olmadan yapan fonksiyon döndürür."""

    def rota_sayisi(gezegen: str, adim: int) -> int:
        """Gezegenden başlayıp tam adim yolculuk yapan farklı rotaların sayısı."""
        if adim == 0:
            return 1
        return sum(rota_sayisi(hedef, adim - 1) for hedef in baglantilar[gezegen])

    return rota_sayisi


if __name__ == "__main__":
    from uzay_oyunu.oyun import galaksi_yukle

    baglantilar = galaksi_yukle()["baglantilar"]

    onbelleksiz = rota_sayaci_onbelleksiz(baglantilar)
    baslangic = time.perf_counter()
    sonuc_1 = onbelleksiz("dünya", 20)
    sure_1 = time.perf_counter() - baslangic

    say = rota_sayaci(baglantilar)
    baslangic = time.perf_counter()
    sonuc_2 = say("dünya", 20)
    sure_2 = time.perf_counter() - baslangic

    print(f"Önbelleksiz: {sonuc_1} rota, {sure_1:.4f} saniye")
    print(f"Önbellekli : {sonuc_2} rota, {sure_2:.6f} saniye")
    print(say.cache_info())