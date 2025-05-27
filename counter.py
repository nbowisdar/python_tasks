class Counter:
    pass


def Counter():
    pass


if __name__ == "__main__":
    counter = Counter()
    assert counter() == 1
    assert counter() == 2
    assert counter() == 3

    print("Ok")
