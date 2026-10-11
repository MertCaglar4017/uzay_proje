"""Yardımcı fonksiyonlar."""


def yakit_ekle(miktar: int, depo: list[int] | None = None) -> list[int]:
    """Miktarı depoya ekler; depo verilmezse her çağrıda yeni bir liste açar."""
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo