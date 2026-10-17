"""Üreteçler, veri akışları ve önbellekli hesaplar."""

from collections.abc import Iterator


def fibonacci() -> Iterator[int]:
    """Sonsuz fibonacci dizisini (0, 1, 1, 2, ...) sırayla üretir."""
    onceki, simdiki = 0, 1
    while True:
        yield onceki
        onceki, simdiki = simdiki, onceki + simdiki