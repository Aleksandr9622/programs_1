a = set(input(print('Введите множество a:')))
b = set(input(print('Введите множество b:')))


def superset(x: set, y: set):
    if x.issuperset(y):
        if y.issuperset(x):
            print(x, '=', y, 'множества равны')
        else:
            print(x, 'является супер множеством')
    elif y.issuperset(x):
        print(y, 'является супер множеством')
    else:
        print('Ни одно из множеств не является \n подмножеством другого')


superset(a, b)
