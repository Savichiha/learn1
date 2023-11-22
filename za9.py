def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)

    return one + delimiter + two
   
print(get_summ (4, 3))
