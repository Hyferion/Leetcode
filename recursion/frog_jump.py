cache = {0: 1, 1: 1}


def frogjump(feet):
    if feet < 0:
        return 0
    if feet not in cache:
        cache[feet] = frogjump(feet - 1) + frogjump(feet - 3) + frogjump(feet - 5)
        return cache[feet]
    else:
        return cache[feet]


print(frogjump(111))
