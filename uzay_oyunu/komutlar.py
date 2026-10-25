"""Oyun içi komutlar: dekoratörle kayıt deseni."""

from collections.abc import Callable

KOMUTLAR: dict[str, tuple[Callable, str]] = {}


def komut(ad: str, aciklama: str = "") -> Callable:
    """Fonksiyonu KOMUTLAR sözlüğüne (fonksiyon, aciklama) olarak kaydeder.

    Fonksiyonu değiştirmez, olduğu gibi geri verir. Aynı ad ikinci kez
    kullanılırsa, tanım anında ValueError fırlatır.
    """

    def kaydet(fonksiyon: Callable) -> Callable:
        if ad in KOMUTLAR:
            raise ValueError(f"'{ad}' komutu zaten kayıtlı")
        KOMUTLAR[ad] = (fonksiyon, aciklama)
        return fonksiyon

    return kaydet


@komut("yardim", "komutları listeler")
def yardim(durum: dict) -> str:
    """Kayıtlı bütün komutları alfabetik sırayla açıklamalarıyla listeler."""
    return "\n".join(
        f"{ad} {aciklama}" for ad, (_, aciklama) in sorted(KOMUTLAR.items())
    )


@komut("envanter", "eşyalarını gösterir")
def envanter(durum: dict) -> str:
    """Oyuncunun eşyalarını gösterir."""
    # Döngüsel içe aktarmayı önlemek için oyun modülü burada içe aktarılır.
    from uzay_oyunu.oyun import envanter_metni

    metin = envanter_metni(durum["credits"], durum["engines"], durum["copilot"])
    return metin or "Hiçbir eşyan yok."


@komut("harita", "gidebileceğin gezegenleri gösterir")
def harita(durum: dict) -> str:
    """Bulunulan gezegenden gidilebilecek gezegenleri gösterir."""
    return ", ".join(durum["baglantilar"][durum["konum"]])