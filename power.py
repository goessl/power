"""power module including different power functions."""


from functools import reduce
from itertools import repeat
from operator import mul
from typing import Callable, TypeVar

__all__ = ('pow_N_naive', 'pow_N_binary',
           'pow_Z_naive', 'pow_Z_binary')



T = TypeVar('T')

def pow_N_naive(x: T,
                n: int,
                mul: Callable[[T, T], T] = mul,
                one: T|None = None) -> T:
    """Return `x` raised by a natural number `n`.
    
    Uses naive repeated multiplication.
    
    Parameters
    ----------
    x
        Base.
    n
        Exponent. Must be nonnegative.
    mul
        Multiplication function.
    one
        One. `type(x)(1)` is used if `None`.
    """
    if not isinstance(n, int):
        raise TypeError(f"unsupported exponent type for pow_N_naive(): '{type(n)}'")
    if not n>=0:
        raise ValueError(f'invalid exponent value for pow_N_naive(): {n}')
    
    return reduce(mul, repeat(x, n), one or type(x)(1))

def pow_N_binary(x: T,
                 n: int,
                 mul: Callable[[T, T], T] = mul,
                 one: T|None = None) -> T:
    """Return `x` raised by a natural number `n`.
    
    Uses binary exponentiation/exponentiation by squaring.
    
    Parameters
    ----------
    x
        Base.
    n
        Exponent. Must be nonnegative.
    mul
        Multiplication function.
    one
        One. `type(x)(1)` is used if `None`.
    
    References
    ----------
    - [Wikipedia - Exponentiation by squaring](https://en.wikipedia.org/wiki/Exponentiation_by_squaring)
    """
    if not isinstance(n, int):
        raise TypeError(f"unsupported exponent type for pow_N_binary(): '{type(n)}'")
    if not n>=0:
        raise ValueError(f'invalid exponent value for pow_N_binary(): {n}')
    
    r = one or type(x)(1)
    while n: #avoid unnecessary *1
        if n % 2 == 1:
            r = mul(r, x)
        x = mul(x, x)
        n //= 2
    return r


def pow_Z_naive(x: T,
                n: int,
                mul: Callable[[T, T], T] = mul,
                inv: Callable[[T], T] = lambda x: 1/x,
                one: T|None = None) -> T:
    """Return `x` raised by a whole integer `n`.
    
    Uses naive repeated multiplication.
    
    Parameters
    ----------
    x
        Base.
    n
        Exponent.
    mul
        Multiplication function.
    inv
        Multiplicative inversion function.
    one
        One. `type(x)(1)` is used if `None`.
    """
    if not isinstance(n, int):
        raise TypeError(f"unsupported exponent type for pow_Z_naive(): '{type(n)}'")
    
    if n < 0:
        return pow_N_naive(inv(x), -n, mul=mul, one=one)
    else:
        return pow_N_naive(x, n, mul=mul, one=one)

def pow_Z_binary(x: T,
                 n: int,
                 mul: Callable[[T, T], T] = mul,
                 inv: Callable[[T], T] = lambda x: 1/x,
                 one: T|None = None) -> T:
    """Return `x` raised by a whole integer `n`.
    
    Uses binary exponentiation/exponentiation by squaring.
    
    Parameters
    ----------
    x
        Base.
    n
        Exponent.
    mul
        Multiplication function.
    inv
        Multiplicative inversion function.
    one
        One. `type(x)(1)` is used if `None`.
    
    References
    ----------
    - [Wikipedia - Exponentiation by squaring](https://en.wikipedia.org/wiki/Exponentiation_by_squaring)
    """
    if not isinstance(n, int):
        raise TypeError(f"unsupported exponent type for pow_Z_binary(): '{type(n)}'")
    
    if n < 0:
        return pow_N_binary(inv(x), -n, mul=mul, one=one)
    else:
        return pow_N_binary(x, n, mul=mul, one=one)
