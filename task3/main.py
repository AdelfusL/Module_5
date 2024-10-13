from task_3 import House

if __name__ == '__main__':
    h1 = House(1,'ЖК Эльбрус', 10)
    h2 = House(1, 'ЖК Акация', 20)

    print(h1)
    print(h2)

    print(f'{h1.get_name()} == {h2.get_name()}: {h1 == h2}')  # __eq__

    h1.set_floors(h1+10)  # __add__
    print(f'({h1.get_name()} = {h1.get_name()} + 10): {h1}')
    print(f'{h1.get_name()} == {h2.get_name()}: {h1 == h2}')
    h1+=10  # __iadd__
    print(f'({h1.get_name()} += 10): {h1}')

    h2.set_floors(10 + h2)   # __radd__
    print(f'({h2.get_name()} = 10 + {h2.get_name()}): {h2}')

    print(f'{h1.get_name()} > {h2.get_name()}: {h1 > h2}')  # __gt__
    print(f'{h1.get_name()} >= {h2.get_name()}: {h1 >= h2}')  # __ge__
    print(f'{h1.get_name()} < {h2.get_name()}: {h1 < h2}')  # __lt__
    print(f'{h1.get_name()} <= {h2.get_name()}: {h1 <= h2}')  # __le__
    print(f'{h1.get_name()} != {h2.get_name()}: {h1 != h2}')  # __ne__
