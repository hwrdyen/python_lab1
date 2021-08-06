import math

def find_time_to_escape(cow_speed, cow_distance): 
    time = cow_distance/cow_speed
    return round(time,2)


if __name__ == '__main__':
    speed = float(input("Please insert the speed of cow: "))
    distance = float(input("Please insert cow's distance from the boundary: "))
    T = find_time_to_escape(speed, distance)
    print(T)
