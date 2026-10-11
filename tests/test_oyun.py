from uzay_oyunu.oyun import travel


def test_kara_delige_ulasilir(monkeypatch):
    cevaplar = iter(["1", "2", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(cevaplar))
    assert travel() == "kara_delik"