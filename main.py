def my_func(storage):
    it = iter(storage)

    try:
        while True:
            next_it = next(it)
            print(next_it)
    except StopIteration:
        print('End of iteration')


if __name__ == '__main__':
    storage = [1,2,3]
    my_func(storage)

    my_func(storage)

    it = iter(storage)


