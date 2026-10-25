"""Uzay oyunu: ana oyun dosyası."""

import json
from pathlib import Path

from uzay_oyunu.akis import yakit_gostergesi
from uzay_oyunu.araclar import hamle_sayaci
from uzay_oyunu.dekoratorler import log_cagri
from uzay_oyunu.komutlar import KOMUTLAR

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


@log_cagri
def hedef_menusu(hedefler: list[str]) -> str:
    """Hedefleri numaralı menü metni olarak döndürür."""
    satirlar = ["Nereye gitmek istersin?"]
    for numara, hedef in enumerate(hedefler, start=1):
        satirlar.append(f"[{numara}] {hedef}")
    return "\n".join(satirlar)


@log_cagri
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
    gosterge = yakit_gostergesi(fuel, 5)
    sayac = hamle_sayaci()
    hamle = 0
    while planet != "kara_delik":
        print(f"Şu an {planet} gezegenindesin. Yakıt: {fuel}")

        envanter = envanter_metni(credits, engines, copilot)
        if envanter:
            print(envanter)

        destinations = galaksi["baglantilar"][planet]

        print(hedef_menusu(destinations))

        durum = {
            "konum": planet,
            "baglantilar": galaksi["baglantilar"],
            "credits": credits,
            "engines": engines,
            "copilot": copilot,
        }
        cevap = input("> ").strip()
        while cevap in KOMUTLAR:
            islev, _ = KOMUTLAR[cevap]
            print(islev(durum))
            print(hedef_menusu(destinations))
            cevap = input("> ").strip()
        choice = int(cevap)

        try:
            fuel = next(gosterge)
        except StopIteration:
            print("Yakıtın bitti, uzayda sürükleniyorsun…")
            break
        planet = destinations[choice - 1]
        hamle = sayac()

    if planet == "kara_delik":
        print("Kara deliğe ulaştın!")
    print(f"Oyunu {hamle} hamlede bitirdin!")
    return planet


if __name__ == "__main__":
    travel()