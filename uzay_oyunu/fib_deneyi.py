"""Dekoratör sırası deneyi: say ve lru_cache'i üç farklı biçimde birleştirir."""

from functools import lru_cache

from uzay_oyunu.dekoratorler import say


@say
def fib_yalniz_say(n: int) -> int:
    """Özyinelemeli fibonacci; yalnızca çağrılar sayılır."""
    return n if n < 2 else fib_yalniz_say(n - 1) + fib_yalniz_say(n - 2)


@say
@lru_cache(maxsize=None)
def fib_say_ustte(n: int) -> int:
    """Özyinelemeli fibonacci; say üstte, lru_cache altta."""
    return n if n < 2 else fib_say_ustte(n - 1) + fib_say_ustte(n - 2)


@lru_cache(maxsize=None)
@say
def fib_lru_ustte(n: int) -> int:
    """Özyinelemeli fibonacci; lru_cache üstte, say altta."""
    return n if n < 2 else fib_lru_ustte(n - 1) + fib_lru_ustte(n - 2)


if __name__ == "__main__":
    fib_yalniz_say(20)
    fib_say_ustte(20)
    fib_lru_ustte(20)
    print(f"Yalnızca @say : {fib_yalniz_say.cagri}")
    print(f"@say üstte, @lru_cache altta: {fib_say_ustte.cagri}")
    print(f"@lru_cache üstte, @say altta: {fib_lru_ustte.__wrapped__.cagri}")