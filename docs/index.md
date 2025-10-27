---
hide:
  - navigation
---

# power

An exponentiation Python package.

```python
>>> from poly import polymul, polyone
>>> from power import pow_N_binary
>>> p = (1, 2, 3)
>>> n = 3
>>> pow_N_binary(p, n, mul=polymul, one=polyone)
(1, 6, 21, 44, 63, 54, 27)
```

## Installation

```console
pip install git+https://github.com/goessl/power.git
```

## Usage

::: power

## Roadmap

- [ ] Perfect complexity
- [ ] [Modular exponentiation](https://en.wikipedia.org/wiki/Modular_exponentiation)
- [ ] [Addition-chain exponentiation](https://en.wikipedia.org/wiki/Addition-chain_exponentiation)
- [ ] C extension

## License (MIT)

Copyright (c) 2025 Sebastian Gössl

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
