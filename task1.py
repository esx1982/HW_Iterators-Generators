#Доработать класс FlatIterator в коде ниже. Должен получиться итератор, который принимает список списков и возвращает их плоское представление,
#т. е. последовательность, состоящую из вложенных элементов. Функция test в коде ниже также должна отработать без ошибок.

class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.count = 0
        self.count_1 = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.count_1 += 1
        if self.count_1 >= len(self.list_of_list[self.count]):
            self.count_1 = 0
            self.count += 1

        if self.count >= len(self.list_of_list):
            raise StopIteration
        item = self.list_of_list[self.count][self.count_1]
        return item
def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()