#price = input('Введите цену: ')
#discount = input('Введите скидку: ')

try:
    def discounted(price, discount, max_discount=20):
        price = float((price))
        discount = float((discount))
        max_discount = int((max_discount))
        if discount >= 100:
            raise ValueError('Слишком большая скидка')
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
except(Exception, ValueError, TypeError):
    print('Неверные данные')

print(discounted(100, 10))