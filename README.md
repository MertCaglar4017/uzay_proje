# Uzay Oyunu

Ad Soyad: Mert Emir Çağlar
Öğrenci No: 20253004017
GitHub: https://github.com/MertCaglar4017/uzay_proje

## Çalıştırma

Oyunu oynamak için:

    python -m uzay_oyunu.oyun

Testleri çalıştırmak için:

    uv run pytest

(`uv` yoksa aynı testler `python -m pytest` ile de çalışır.)

## Hafta 4: Önbellek ölçümü

`rota_sayisi("dünya", 20)` hesabı 4315343 rota buluyor.

| Sürüm | Süre |
|---|---|
| Önbelleksiz | 0.9509 saniye |
| Önbellekli (`lru_cache`) | 0.000052 saniye |

`cache_info()` çıktısı:

    CacheInfo(hits=47, misses=51, maxsize=None, currsize=51)
