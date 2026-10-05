def discount(cart_total, vip=False):
    if cart_total < 0:
        raise ValueError("Cart total cannot be negative")

    if cart_total > 100:
        d = 0.20
    elif cart_total > 50:
        d = 0.10
    else:
        d = 0.0

    if vip:
        d += 0.05

    return min(d, 0.25)
