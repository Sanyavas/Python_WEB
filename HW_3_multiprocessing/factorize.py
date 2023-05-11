import time


def factorize(*numbers):
    for num in numbers:
        list_num = []
        for i in range(1, num + 1):
            if num % i == 0:
                list_num.append(i)
        print(list_num)


def main():
    start = time.time()
    factorize(128, 100_651_060, 99_999, 100_651_060, 123_002_846)
    end = time.time()
    print(f'\nEnd! Total time: {end - start} sec')


if __name__ == '__main__':
    main()


