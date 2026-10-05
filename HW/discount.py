def discount(price, vip=False):
    if price >= 5000:
        d = 20
    elif price >= 1000:
        d = 10
    else:
        d = 0

    if vip:
        d += 5

    return min(d, 25)
