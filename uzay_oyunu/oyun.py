"""Uzay oyunu: ana oyun dosyası."""


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


def travel(planet="dünya", credits=True, engines=False, copilot=True):
    """Oyunu oynatır; kara deliğe ulaşınca ya da yakıt bitince durur."""
    fuel = 100
    while planet != "kara_delik" and fuel > 0:
        print(f"Şu an {planet} gezegenindesin. Yakıt: {fuel}")

        envanter = envanter_metni(credits, engines, copilot)
        if envanter:
            print(envanter)

        # Hedefler
        if planet == "dünya":
            destinations = ["orion", "centauri"]
        elif planet == "orion":
            destinations = ["dünya", "sirius"]
        elif planet == "sirius":
            destinations = ["dünya", "orion", "centauri", "kara_delik"]
        elif planet == "centauri":
            destinations = ["dünya", "sirius", "kara_delik"]

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