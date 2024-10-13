class House:
    __slots__ = ('__current_floor', '__name', '__floors')
    def __init__(self, current_floor, name = "MyHouse", floors = 20):
        if floors<1:
            print("Uncorrect quantity of floors, setting 20 as defult")
            self.__floors = 20
        else:
            self.__floors = floors
        if not (1 <= current_floor <= floors):
            print("Uncorrect floor, setting 1 as defult")
            self.__current_floor = 1
        else:
            self.__current_floor = current_floor
        self.__name = name

    def go_to_floor(self, floor):
        if not (1 <= floor <= self.__floors):
            print("Uncorrect floor")
        else:
            self.__current_floor = floor

    def get_floors(self):
        return self.__floors
    def get_name(self):
        return self.__name
    def get_current_floor(self):
        return self.__current_floor

    def set_floors(self, value):
        if isinstance(value, House):
            self.__floors = value.__floors
        if isinstance(value, int):
            self.__floors =  value
    def set_name(self, value):
        if isinstance(value, House):
            self.__name = value.__name
        if isinstance(value, str):
            self.__name = value


    def __len__(self):
        return self.__floors
    def __str__(self):
        return (f'Название: {self.__name}, кол-во этажей: {self.__floors}')

    def __lt__(self, other):
        if isinstance(other, House):
            return self.__floors < other.__floors
        if isinstance(other, int):
            return self.__floors < other

    def __gt__(self, other):
        if isinstance(other, House):
            return self.__floors > other.__floors
        if isinstance(other, int):
            return self.__floors > other

    def __eq__(self, other):
        if isinstance(other, House):
            return self.__floors == other.__floors
        if isinstance(other, int):
            return self.__floors == other

    def __le__(self, other):
        if isinstance(other, House):
            return self.__floors <= other.__floors
        if isinstance(other, int):
            return self.__floors <= other

    def __ge__(self, other):
        if isinstance(other, House):
            return self.__floors >= other.__floors
        if isinstance(other, int):
            return self.__floors >= other

    def __add__(self, other):
        if isinstance(other, House):
            return self.__floors + other.__floors
        if isinstance(other, int):
            return self.__floors + other

    def __radd__(self, other):
        if isinstance(other, House):
            return self.__floors + other.__floors
        if isinstance(other, int):
            return self.__floors + other

    def __iadd__(self, other):
        if isinstance(other, House):
            self.__floors += other.__floors
            return self
        if isinstance(other, int):
            self.__floors += other
            return self