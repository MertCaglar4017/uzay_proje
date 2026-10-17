from uzay_oyunu.oyun import travel


def test_kara_delige_ulasilir(monkeypatch):
    cevaplar = iter(["2", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(cevaplar))
    assert travel() == "kara_delik"


def test_hamle_sayisi_yazilir(monkeypatch, capsys):
    cevaplar = iter(["2", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(cevaplar))
    travel()
    assert "Oyunu 2 hamlede bitirdin!" in capsys.readouterr().out