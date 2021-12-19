from time import time
from tz3 import minimum, maximum, summa, multiplication
import math
import unittest

start = time()
test_data = []
with open("file.txt") as f:
    for line in f:
        test_data += [float(x) for x in line.split()]


class MinMaxTest(unittest.TestCase):
    def test_minimum(self):
        self.assertEqual(minimum(test_data), min(test_data))

    def test_maximum(self):
        self.assertEqual(maximum(test_data), max(test_data))

    def test_summa(self):
        self.assertEqual(summa(test_data), sum(test_data))

    def test_multiplication(self):
        self.assertEqual(multiplication(test_data), math.prod(test_data))

    def test_chis(self):
        self.assertEqual(float(summa(test_data)), float(sum(test_data)))
        # собственный тест, который проверяет, что результатом суммы является вещественное число


if __name__ == '__main__':
    unittest.main()

finish = time()
work_time = finish - start
print("Программа завершила работу за", work_time, "секунд")
