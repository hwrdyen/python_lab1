import math

def report_cow_status(cow_position1, cow_position2, delta_t, boundary_points):
    if(boundary_points[0][0]>cow_position2[0]>boundary_points[1][0]) or (boundary_points[1][0]>cow_position2[0]>boundary_points[0][0]):
        if(boundary_points[0][1]>cow_position2[1]>boundary_points[2][1]) or (boundary_points[2][1]>cow_position2[1]>boundary_points[0][1]):
            if(boundary_points[0][0]>cow_position1[0]>boundary_points[1][0]) or (boundary_points[1][0]>cow_position1[0]>boundary_points[0][0]):
                if(boundary_points[0][1]>cow_position1[1]>boundary_points[2][1]) or (boundary_points[2][1]>cow_position1[1]>boundary_points[0][1]):
                    distance_for_unit1 = math.sqrt((cow_position2[0]-cow_position1[0])**2+(cow_position2[1]-cow_position1[1])**2)
                    p = round(distance_for_unit1,2)
                    unit = p/delta_t
                    distance_for_time1 = math.sqrt((boundary_points[0][1]-cow_position2[1])**2)
                    distance_for_time2 = math.sqrt((boundary_points[1][0]-cow_position2[0])**2)
                    distance_for_time3 = math.sqrt((boundary_points[2][1]-cow_position2[1])**2)
                    distance_for_time4 = math.sqrt((boundary_points[3][0]-cow_position2[0])**2)
                    o = min(distance_for_time1,distance_for_time2,distance_for_time3,distance_for_time4)
                    i = o/unit
                    return round(i,2)
                else:
                    return -1
            else:
                return -1
        elif(boundary_points[0][0]>cow_position1[0]>boundary_points[1][0]) or (boundary_points[1][0]>cow_position1[0]>boundary_points[0][0]):
            if(boundary_points[0][1]>cow_position1[1]>boundary_points[2][1]) or (boundary_points[2][1]>cow_position1[1]>boundary_points[0][1]):
                return 0
        else:
            distance_for_unit1 = math.sqrt((cow_position2[0]-cow_position1[0])**2+(cow_position2[1]-cow_position1[1])**2)
            p = round(distance_for_unit1,2)
            unit = p/delta_t
            distance_for_unit2 = math.sqrt((boundary_points[0][1]-cow_position2[1])**2+(boundary_points[0][0]-cow_position2[0])**2)
            m = distance_for_unit2/unit
            return round(m,2)
    elif(boundary_points[0][0]>cow_position1[0]>boundary_points[1][0]) or (boundary_points[1][0]>cow_position1[0]>boundary_points[0][0]):
        if(boundary_points[0][1]>cow_position1[1]>boundary_points[2][1]) or (boundary_points[2][1]>cow_position1[1]>boundary_points[0][1]):
            return 0
        else:
            distance_for_unit1 = math.sqrt((cow_position2[0]-cow_position1[0])**2+(cow_position2[1]-cow_position1[1])**2)
            p = round(distance_for_unit1,2)
            unit = p/delta_t
            distance_for_unit2 = math.sqrt((boundary_points[0][1]-cow_position2[1])**2+(boundary_points[0][0]-cow_position2[0])**2)
            m = distance_for_unit2/unit
            return round(m,2)
    else:
        distance_for_unit1 = math.sqrt((cow_position2[0]-cow_position1[0])**2+(cow_position2[1]-cow_position1[1])**2)
        p = round(distance_for_unit1,2)
        unit = p/delta_t
        distance_for_unit2 = math.sqrt((boundary_points[0][1]-cow_position2[1])**2+(boundary_points[0][0]-cow_position2[0])**2)
        m = distance_for_unit2/unit
        return round(m,2)
    
    '''if cow position 1 and 2 are both inside the bounds, count the time it takes for the c

'''

if __name__ == '__main__':
    cow_position1_list1 = [3,3]
    cow_position2_list1 = [4,4]
    cow_position1_list2 = [0,0]
    cow_position2_list2 = [3,7]
    cow_position1_list3 = [0,0]
    cow_position2_list3 = [3,3]
    cow_position1_list4 = [3,3]
    cow_position2_list4 = [3,6]
    boundary_points_list = [[2,5],[5,5],[5,1],[2,1]]
    delta_t = 10.0

    u = report_cow_status(cow_position1_list1,cow_position2_list1,delta_t,boundary_points_list)
    print("report_cow_status","(",cow_position1_list1,",",cow_position2_list1,",",delta_t,",",boundary_points_list,")")
    print(u)

    h = report_cow_status(cow_position1_list2,cow_position2_list2,delta_t,boundary_points_list)
    print("report_cow_status","(",cow_position1_list2,",",cow_position2_list2,",",delta_t,",",boundary_points_list,")")
    print(h)
    
    j = report_cow_status(cow_position1_list3,cow_position2_list3,delta_t,boundary_points_list)
    print("report_cow_status","(",cow_position1_list3,",",cow_position2_list3,",",delta_t,",",boundary_points_list,")")
    print(j)

    n = report_cow_status(cow_position1_list4,cow_position2_list4,delta_t,boundary_points_list)
    print("report_cow_status","(",cow_position1_list4,",",cow_position2_list4,",",delta_t,",",boundary_points_list,")")
    print(n)
