from collections import Counter
from random import randint


class SearchDuplicate:
    duplicate = []

    def search(self, array):
        for i in array:
            if Counter(array)[i] > 1 and i not in self.duplicate:
                self.duplicate.append(i)
        return self.duplicate


if __name__ == '__main__':
    n = int(input('Введите размер массива: '))
    data = [randint(1, n) for _ in range(n+2)]
    print(SearchDuplicate().search(data))
