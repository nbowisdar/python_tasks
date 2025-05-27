class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return self.count


# def Counter():
#     c = 0

#     def incr():
#         nonlocal c
#         c += 1
#         return c

#     return incr


if __name__ == "__main__":
    counter = Counter()
    assert counter() == 1
    assert counter() == 2
    assert counter() == 3

    print("Ok")
