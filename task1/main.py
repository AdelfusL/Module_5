from task_1 import House

if __name__ == '__main__':
    house1 = House(1,"House №1", 17)
    print(f'House name: {house1.get_name()}')
    print(f'Quantity of floors: {house1.get_floors()}')
    print(f'Current floor: {house1.get_current_floor()}')
    print('moving')
    house1.go_to_floor(13)
    print(f'Current floor: {house1.get_current_floor()}')
    print('moving')
    house1.go_to_floor(-1)
    print('moving')
    house1.go_to_floor(18)

    print()
    house2 = House(1000, "House №2", -5)
    print(f'House name: {house2.get_name()}')
    print(f'Quantity of floors: {house2.get_floors()}')
    print(f'Current floor: {house2.get_current_floor()}')
    print('moving')
    house2.go_to_floor(19)
    print(f'Current floor: {house2.get_current_floor()}')


    #house1.current_floor = 25 'House' object has no attribute 'current_floor'
    #изменить атрибут можно только через сеттер
    #сеттер реализован в методе go_to_floor
    #print(house1.get_current_floor())
