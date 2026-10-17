"""Üreteçler, veri akışları ve önbellekli hesaplar."""

from collections.abc import Iterator


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