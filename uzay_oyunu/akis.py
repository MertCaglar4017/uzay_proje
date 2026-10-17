"""Üreteçler, veri akışları ve önbellekli hesaplar."""

from collections.abc import Iterable, Iterator
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