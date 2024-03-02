import CarClass as cc

def main():
    The_car = cc.Car(2017, 'Toyota Tundra')

    for count in range(5):
        The_car.accelerate()
        print(f"The speed of the car is {The_car.get_speed()}.")
    print('\n')

    for count in range(5):
        The_car.brake()
        print(f"The speed of the car is {The_car.get_speed()}")

main()
       
    