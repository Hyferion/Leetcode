def isHappy(n: int, seen=None) -> bool:
    seen_numbers = []
    if seen:
        seen_numbers = seen
        if n in seen_numbers:
            return False
    print(n)
    if n == 1:
        return True
    st = str(n)
    result = 0
    for s in st:
        result = result + int(s) * int(s)
    seen_numbers.append(n)
    try:
        return (isHappy(result, seen_numbers))
    except RecursionError as re:
        return False


print(isHappy(81))
