import multiprocessing
import time
from time import sleep


def factorize(number) -> list[int]:
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


def parallel_factorize(numbers):
    with multiprocessing.Pool() as pool:
        results = pool.map(factorize, numbers)
    return results


def main(numbers):
    start_time = time.time()
    results = parallel_factorize(numbers)
    end_time = time.time()
    factors = []
    for num, factors in zip(numbers, results):
        print(f"Factors of {num}: {factors}")

    print(f"Time taken for parallel execution: {end_time - start_time} seconds")
    return factors


if __name__ == "__main__":
    a = main([128])
    b = main([255])
    c = main([99999])
    d = main([10651060])
    sleep(2)
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]
    print('OK')
