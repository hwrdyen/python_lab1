import math

def is_cow_within_bounds(cow_position, boundary_points):
    if (boundary_points[0][0]>cow_position[0]>boundary_points[1][0])or(boundary_points[1][0]>cow_position[0]>boundary_points[0][0]):
        if (boundary_points[0][1]>cow_position[1]>boundary_points[2][1])or(boundary_points[2][1]>cow_position[1]>boundary_points[0][1]):
            return 1
        else:
            return 0
    else:
        return 0


if __name__ == '__main__':
    cow_position_list = [3,3]
    boundary_list1 = [[2,5], [5,5], [5,1], [2,1]]
    boundary_list2 = [[4,4], [5,4], [5,2], [4,2]]
    within_bounds1 = is_cow_within_bounds(cow_position_list, boundary_list1)
    print("If cow is within bounds shows number '1'")
    print("If cow is not within bounds shows number '0'")
    print("When cow is at",cow_position_list,"and the boundary_points are",boundary_list1)
    print(within_bounds1)
    within_bounds2 = is_cow_within_bounds(cow_position_list, boundary_list2)
    print("When cow is at",cow_position_list,"and the boundary_points are",boundary_list2)
    print(within_bounds2)
