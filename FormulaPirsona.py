from statistics import mean
from math import sqrt

def count_formula_Pirsona(x: list, y: list) -> float:
    aver_x = mean(x)
    aver_y = mean(y)
    def auxiliary_formula(x_i, y_i):
        return (x_i - aver_x)*(y_i - aver_y)
    return sum(list(map(auxiliary_formula, x, y)))/sqrt(sum(list(map(lambda z: z**2, list(map(auxiliary_formula, x, y))))))

list1 = [1, 3, 5]
list2 = [2, 4, 6]

print(count_formula_Pirsona(list1, list2))