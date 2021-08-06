#ESC180 Lab 1
# Connected Cows
# DO NOT modify any function or argument names
import math

def find_euclidean_distance(x1, y1, x2, y2):
    '''
    (float)->float
    find_euclidean_distance calculates the euclidean distance between
    two given 2D points P(x1,y1) and Q(x2,y2), and returs its Euclidean_distance
    '''
    Euclidean_distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
    return round(Euclidean_distance, 2)

   
def is_cow_within_bounds(cow_position, boundary_points):
    if (bx1>cx1>bx2 or bx2>cx1>bx1):
        if (by1>cy1>by2 or by2>cy1>by1):
            return 1
        else:
            return 0
    else:
        return 0
    '''
    Your docstring here
    #function body
    cow_position[0]
    '''

def find_cow_distance_to_boundary(cow_position, boundary_point):
    k = (boundary_point[0]-cow_position[0])**2
    z = (boundary_point[1]-cow_position[1])**2
    Distance_boundary = math.sqrt(k+z)
    return round(Distance_boundary,2)
    """
    Your docstring here
    """
    #function body

'''
def find_time_to_escape(cow_speed, cow_distance):
    """
    Your docstring here
    """
    #function body


def report_cow_status(cow_position1, cow_position2, delta_t, boundary_points):
    """
    Your docstring here
    """
    #function body

'''
if __name__ == '__main__':
    
    x1 = float(input("Please insert X coordinate of point P "))
    y1 = float(input("Please insert y coordinate of point P "))
    x2 = float(input("Please insert x coordinate of point Q "))
    y2 = float(input("Please insert y coordinate of point Q "))
    Euclidean_distance = find_euclidean_distance(x1, y1, x2, y2)
    print("The Euclidean distance is:",Euclidean_distance)
    
    cx1 = int(input("Please insert x coordinate for cow: "))
    cy1 = int(input("Please insert y coordinate for cow: "))
    bx1 = int(input("Please insert x coordinate for point1 and 4: "))
    by1 = int(input("Please insert y coordinate for point1 and 2: "))
    bx2 = int(input("Please insert x coordinate for point2 and 3: "))
    by2 = int(input("Please insert y coordinate for point3 and 4: "))

    cow_position = (cx1,cy1)
    boundary_points = (bx1,by1),(bx2,by1),(bx2,by2),(bx1,by2)
    position = is_cow_within_bounds(cow_position, boundary_points)
    print(position)

    a_list = [3,3]
    b_list = [2,5]
    c_list = [2,2]
    d_list = [0,1]
    w = find_cow_distance_to_boundary(a_list, b_list)
    g = find_cow_distance_to_boundary(c_list, d_list)
    print("Distance between cow",a_list,"and boundary point",b_list)
    print(w)
    print("Distance between cow",c_list,"and boundary point",d_list)
    print(g)
   
''' # Test your code by running your functions here, and printing the
    # results to the terminal.
    # This code will not be marked
    print('Testing functions...')
    # test_distance = find_euclidian_distance(3.0, 3.0, 2.0, 5.0)
    # print(test_distance)
    # test_distance should be 2.24
'''
