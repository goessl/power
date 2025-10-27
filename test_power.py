from power import *
from pytest import raises
from random import randint
from fractions import Fraction



def test_pow_N_naive():
    for _ in range(1000):
        x = randint(-100, +100)
        n = randint(0, 20)
        assert pow_N_naive(x, n) == x**n
    with raises(TypeError):
        pow_N_naive(1, 1.)
    with raises(ValueError):
        pow_N_naive(1, -1)

def test_pow_N_binary():
    for _ in range(1000):
        x = randint(-100, +100)
        n = randint(0, 20)
        assert pow_N_binary(x, n) == x**n
    with raises(TypeError):
        pow_N_binary(1, 1.)
    with raises(ValueError):
        pow_N_binary(1, -1)


def test_pow_Z_naive():
    for _ in range(1000):
        x = Fraction(randint(-100, +100), randint(1, +100))
        n = randint(-20, 20)
        if not (x==0 and n<0):
            assert pow_Z_naive(x, n) == x**n
    with raises(TypeError):
        pow_Z_naive(1, 1.)

def test_pow_Z_binary():
    for _ in range(1000):
        x = Fraction(randint(-100, +100), randint(1, +100))
        n = randint(-20, 20)
        if not (x==0 and n<0):
            assert pow_Z_binary(x, n) == x**n
    with raises(TypeError):
        pow_Z_binary(1, 1.)
