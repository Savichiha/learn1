price = 100
discount = 5

def discounted(price, discount, max_discount=20):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if discount >= 100:
        raise ValueError('Слишком большая скидка')
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)

discounted(100, 50, max_discount=60)