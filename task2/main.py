from task_2 import House

if __name__ == '__main__':
    h1 = House(1,'ЖК Эльбрус', 10)
    h2 = House(1, 'ЖК Акация', 20)

    # __str__
    print(h1)
    print(h2)

    # __len__
    print(len(h1))
    print(len(h2))