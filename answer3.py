def without_recur(n, cur):
    if cur is None:
        cur = 0

    if not isinstance(n, int):
        raise ValueError('Invalid input')

    if n < 2:
        raise ValueError('Invalid input')

    return cur + (n - 1) / n

print(without_recur(4,4))





