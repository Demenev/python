# Задание 1.
class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        return '\n'.join(map(str, self.my_list))

    def __add__(self, other):
        sum_matrix = []
        sum_lines = []
        for i in range(len(self.my_list)):
            for j in range(len(self.my_list[i])):
                sum_lines.append(self.my_list[i][j] + other.my_list[i][j])
                if len(sum_lines) == len(self.my_list[i]):
                    sum_matrix.append(sum_lines)
                    sum_lines = []
        return '\n'.join(map(str, sum_matrix))

matrix_1 = Matrix([[45, 32, 67], [43, 54, 56], [78, 54,98]])
matrix_2 = Matrix([[56, 76, 1], [23, 24, 54], [12, 43, 56]])
print(matrix_1)
print(matrix_2)
print(f'Итоговая матрица\n{matrix_1 + matrix_2}')

# Задание 2.
from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, number):
        self.number = number

    @abstractmethod
    def fabric_consumption(self):
        pass

class Costume(Clothes):
    def __init__(self, number):
        super().__init__(number)

    @property
    def fabric_consumption(self):
        return f'Расход ткани на костюм - {2*self.number + 0.3}'

class Coat(Clothes):
    def __init__(self, number):
        super().__init__(number)

    @property
    def fabric_consumption(self):
        return f'Расход ткани на пальто - {self.number/6.5 + 0.5}'

costume = Costume(178)
coat = Coat(52)
print(costume.fabric_consumption)
print(coat.fabric_consumption)

# Задание 3.
class Cell:
    def __init__(self, param):
        self.param = param

    def __str__(self):
        return self.param

    def __add__(self, other):
        return f'Объединение двух клеток - {self.param + other.param} ячеек'

    def __sub__(self, other):
        if self.param > other.param:
            return f'Вычитание двух клеток - {self.param - other.param} ячеек'
        else:
            print('Процесс не возможен')

    def __mul__(self, other):
        return f'Создание общей клетки - {self.param * other.param} ячеек'

    def __truediv__(self, other):
        return f'Деление клеток - {round(self.param / other.param)} ячеек'

    def make_order(self, number):
        return '\n'.join(["*" * number for i in range(self.param // number)]) + '\n' + '*' * (self.param % number)


cell_1 = Cell(int(input('Введите целое неотрицательное число ')))
cell_2 = Cell(int(input('Введите целое неотрицательное число ')))
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(5))
print(cell_2.make_order(4))