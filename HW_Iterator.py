class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.index_outside = 0
        self.index_inside = 0


    def __iter__(self):
        return self

    def __next__(self):
        while self.index_outside < len(self.list_of_list):
            if self.index_inside < len(self.list_of_list[self.index_outside]):
                item = self.list_of_list[self.index_outside][self.index_inside]
                self.index_inside += 1
                return item
            
            else:
                self.index_outside += 1
                self.index_inside = 0
                continue

        raise StopIteration


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
