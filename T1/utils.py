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

