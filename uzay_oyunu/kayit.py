"""Görev kayıtlarını biçimlendiren modül."""


def gorev_kaydi(baslik: str, *adimlar: str, oncelik: str = "normal", **ekler: str) -> str:
    """Bir görevi başlık, numaralı adımlar ve ek bilgilerle metin olarak döndürür."""
    satirlar = [f"[{oncelik.upper()}] {baslik}"]
    for numara, adim in enumerate(adimlar, start=1):
        satirlar.append(f" {numara}. {adim}")
    for anahtar, deger in ekler.items():
        satirlar.append(f" {anahtar}: {deger}")
    return "\n".join(satirlar)


if __name__ == "__main__":
    # 1. Biçim: normal çağrı
    print(
        gorev_kaydi(
            "Kara deliğe atla",
            "Kredi kazan",
            "Pilot bul",
            "Hiperdrive al",
            oncelik="yüksek",
            sorumlu="Mert",
        )
    )

    # 2. Biçim: liste ve sözlüğü açarak çağrı (* ve **)
    adimlar = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ekler = {"sorumlu": "Mert"}
    print(gorev_kaydi("Kara deliğe atla", *adimlar, oncelik="yüksek", **ekler))