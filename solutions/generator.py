def generate_numbers():
    n = 0
    while True:
        n += 1
        yield n


# class generate_numbers:
#     def __init__(self):
#         self.c = 0

#     def __next__(self):
#         self.c += 1
#         return self.c


if __name__ == "__main__":
    generator = generate_numbers()
    assert 1 == next(generator)
    assert 2 == next(generator)
    assert 3 == next(generator)

    print("Ok")
