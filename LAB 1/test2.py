import math

def find_cow_distance_to_boundary(cow_position, boundary_point):
    k = (boundary_point[0]-cow_position[0])**2
    z = (boundary_point[1]-cow_position[1])**2
    Distance_boundary = math.sqrt(k+z)
    return round(Distance_boundary,2)

if __name__ == '__main__':
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
