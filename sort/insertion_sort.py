import time
import random
def sort(tab):
    for i in range(1, len(tab)):
        k = i
        while k > 0 and tab[k - 1] > tab[k]:
            tab[k - 1], tab[k] = tab[k], tab[k - 1]  # On inverse les deux elements d'indices k, et k-1
            k -= 1
    return tab


if __name__ == "__main__":
    n = 10 ** 4
    print((n * n - n) / 4 // 10 ** 6)  # base on complexity, expected number of operation (unit=million)
    tab = [random.randint(0, 100000) for i in range(n)]
    print("Stating algo")
    start_time = time.time()
    sort(tab)
    print("--- %s seconds ---" % (time.time() - start_time))
