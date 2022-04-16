import numpy as np
import time
def multGF28(p1, p2):
    """Multiplicación en GF(2^8)"""
    p = 0
    while p2:
        if p2 & 1:
            p ^= p1
        p1 <<= 1
        if p1 & 0b100000000:
            p1 ^= 0b100011011
        p2 >>= 1
    return p & 0b11111111

def rand_matrix(dim):
  """Genera una matriz cuadrada de dimension dim con valores aleatorios en GF(2^8).""" 
  return np.random.randint(256, size=(dim, dim))
import time

def time_me(f, *args):
  """Mide el tiempo de ejecución de `f` con los argumentos `*args`."""
  start = time.perf_counter()
  f(*args)
  end = time.perf_counter()
  return end - start