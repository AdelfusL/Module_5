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