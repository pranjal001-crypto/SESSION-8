def discount(cart_total, vip=False):
    if cart_total >= 50:
        d = 0.10
    elif cart_total > 100:
        d = 0.20
    else:
        d = 0.0

    if vip:
        d += 0.50

    return d
