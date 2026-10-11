"""Uzay oyunu: ana oyun dosyası."""

import json
from pathlib import Path

GALAKSI_YOLU = Path(__file__).with_name("galaksi.json")


def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    """Eldeki eşyaları "Sende: ..." biçiminde döndürür; eşya yoksa boş metin."""
    items = []
    if credits:
        items.append("bol kredi")
    if engines:
        items.append("hiperdrive motoru")
    if copilot:
        items.append("yetenekli bir pilot")
    if not items:
        return ""
    return "Sende: " + ", ".join(items)


def hedef_menusu(hedefler: list[str]) -> str:
    """Hedefleri numaralı menü metni olarak döndürür."""
    satirlar = ["Nereye gitmek istersin?"]
    for numara, hedef in enumerate(hedefler, start=1):
        satirlar.append(f"[{numara}] {hedef}")
    return "\n".join(satirlar)


def galaksi_kur(
    gezegenler: list[str],
    baglantilar: dict[str, list[str]],
    baslangic: str,
    **kwargs,
) -> dict:
    """Galaksi sözlüğünü kurar; başlangıç gezegeni listede yoksa ValueError verir."""
    if baslangic not in gezegenler:
        raise ValueError(f"Başlangıç gezegeni listede yok: {baslangic}")
    return {
        "gezegenler": gezegenler,
        "baglantilar": baglantilar,
        "konum": baslangic,
        "yakit": kwargs.get("yakit", 50),
    }


def galaksi_yukle(yol: Path = GALAKSI_YOLU) -> dict:
    """galaksi.json dosyasını okuyup galaksi sözlüğünü döndürür."""
    with open(yol, encoding="utf-8") as dosya:
        veri = json.load(dosya)
    return galaksi_kur(**veri)


def travel(credits=True, engines=False, copilot=True):
    """Oyunu oynatır; kara deliğe ulaşınca ya da yakıt bitince durur."""
    galaksi = galaksi_yukle()
    planet = galaksi["konum"]
    fuel = galaksi["yakit"]
    while planet != "kara_delik" and fuel > 0:
        print(f"Şu an {planet} gezegenindesin. Yakıt: {fuel}")

        envanter = envanter_metni(credits, engines, copilot)
        if envanter:
            print(envanter)

        destinations = galaksi["baglantilar"][planet]

        print(hedef_menusu(destinations))

        choice = int(input("> "))
        planet = destinations[choice - 1]
        fuel -= 5

    if planet == "kara_delik":
        print("Kara deliğe ulaştın!")
    else:
        print("Yakıtın bitti.")
    return planet


if __name__ == "__main__":
    travel()