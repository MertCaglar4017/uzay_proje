# Kapsam (Scope) Örnekleri

Bu örnekler, dersteki kapsam örneklerine benzer şekilde hazırlanmıştır.
Kapsam, bir değişkenin programın hangi bölümünde geçerli olduğunu belirler.

## Örnek 1: Fonksiyon içinde aynı isimle değişken tanımlamak

```python
x = 10

def f():
    x = 5
    print(x)

f()
print(x)
```

**Tahminim:** Önce 5, sonra 10 yazılır.

**Gerçek sonuç:**
```
5
10
```

**Neden:** Fonksiyonun içinde `x = 5` yazınca Python yeni bir yerel değişken
oluşturur. Bu `x` sadece `f` içinde geçerlidir ve dışarıdaki `x`'e dokunmaz.
Fonksiyon bitince yerel `x` yok olur, bu yüzden dışarıdaki `print(x)` hâlâ 10 yazar.

## Örnek 2: Dışarıdaki değişkeni sadece okumak

```python
x = 10

def f():
    print(x)

f()
```

**Tahminim:** 10 yazılır.

**Gerçek sonuç:**
```
10
```

**Neden:** `f` içinde `x`'e hiç değer verilmiyor, yalnızca okunuyor. Python,
fonksiyonun içinde `x`'i bulamayınca dışarıya bakar ve dışarıdaki `x = 10`'u
kullanır.

## Örnek 3: UnboundLocalError

```python
x = 10

def f():
    print(x)
    x = 5

f()
```

**Tahminim:** Hata verir (`UnboundLocalError`).

**Gerçek sonuç:**
```
UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
```

**Neden:** Fonksiyonun herhangi bir yerinde `x = 5` gibi bir atama varsa Python,
`x`'i fonksiyonun tamamında yerel değişken sayar. Python bunu fonksiyon çalışmadan
önce, kodu okurken karar verir. Bu yüzden `print(x)` satırı dışarıdaki `x`'i değil
yerel `x`'i okumaya çalışır. Ama yerel `x`'e bu satırda henüz değer verilmemiştir
(değer sonraki satırda veriliyor), o yüzden hata çıkar.

Örnek 2 ile aradaki fark: Örnek 2'de fonksiyonda `x`'e hiç atama yoktu, bu yüzden
`x` dışarıdan okunabildi. Örnek 3'te atama olduğu için `x` yerel oldu.