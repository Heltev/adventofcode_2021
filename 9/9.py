def readfile(filename):
    with open('%s.txt' %filename) as f:
        boards=[]
        for line in f:
            temp_list=[]
            numbers=line
            for element in numbers:
                if element !='\n':
                  temp_list.append(int(element))
            boards.append(temp_list)
    return boards

WIDTH=100
DEPTH=100

def is_low_point(adjacent_points,point):
    for adj_point in adjacent_points:
        if adj_point <= point:
            return False
    return True

def get_adjacent_points_coordinates(point_row,point_col):
    # Top line
    if point_row == 0:
        return get_adjacent_points_coordinates_top(point_row,point_col)
    # Left side
    elif point_col == 0:
        return get_adjacent_points_coordinates_left(point_row,point_col)
    # Bottom line
    elif point_row == DEPTH-1:
        return get_adjacent_points_coordinates_bottom(point_row,point_col)
    # Right side
    elif point_col == WIDTH-1:
        return get_adjacent_points_coordinates_right(point_row,point_col)
    # Point not on edge
    else:
        return ((point_row-1,point_col),(point_row,point_col+1),(point_row+1,point_col),(point_row,point_col-1))
    
def get_adjacent_points_coordinates_left(point_row,point_col):
    # Bottom left corner
    if point_row == DEPTH-1:
        return((DEPTH-2,0),(DEPTH-1,1))
    # Left side, not corner
    else:
        return((point_row-1,point_col),(point_row,point_col+1),(point_row+1,point_col))

def get_adjacent_points_coordinates_bottom(point_row,point_col):
    # Bottom right corner
    if point_col == WIDTH-1:
        return ((DEPTH-1,WIDTH-2),(DEPTH-2,WIDTH-1))
    # Bottom, not corner
    else:
        return ((DEPTH-1,point_col-1),(DEPTH-2,point_col),(DEPTH-1,point_col+1))

def get_adjacent_points_coordinates_right(point_row,point_col):
    # Right side, not corner
    return ((point_row-1,point_col),(point_row,point_col-1),(point_row+1,point_col))

def get_adjacent_points_coordinates_top(point_row,point_col):
    # Top left corner
    if point_col == 0:
        return ((1,0),(0,1))
    # Top right corner
    elif point_col == WIDTH-1:
        return ((0,WIDTH-2),(1,WIDTH-1))
    # Top line, not corner
    else:
        return ((0,point_col-1),(1,point_col),(0,point_col+1))

def get_adjacent_points(row,col):
    adj=get_adjacent_points_coordinates(row,col)
    return adj
    
def is_low_point(point_value,adj_points_value):
    for value in adj_points_value:
        if value <= point_value:
            return False
    return True

def get_point_value(point,all_points):
    return all_points[point[0]][point[1]]

def get_first_point_next_basin(checked_points,points):
    for row in range(DEPTH):
        for col in range(WIDTH):
            if (row,col) not in checked_points and points[row][col] < 9:
                return (row,col) 

def part1():
    points=readfile('input')
    low_points_sum=0
    for row in range(len(points)):
        for col in range(len(points[row])):
            adj_points_value=[]
            adj_points=get_adjacent_points(row,col)
            current_value=get_point_value((row,col),points)
            for point in adj_points:
                adj_points_value.append(get_point_value(point,points))
            if is_low_point(current_value,adj_points_value) == True:
                low_points_sum+=current_value+1
    print(low_points_sum)
                

part1()

def part2():
    points=readfile('input')
    checked = []
    n_nines = 0
    counter = 0
    basin_dict={}
    n_basins = 1
    for row in range(len(points)):
        for col in range(len(points[row])):
            if get_point_value((row,col),points) == 9:
                n_nines += 1
    current_basin = [(0,0)]
    while len(checked) < (DEPTH*WIDTH)-n_nines:
        found_new_point = False
        current_point = current_basin[counter]
        print(current_point)
        adj_points=get_adjacent_points(current_point[0],current_point[1])
        for point in adj_points:
            if get_point_value(point,points) < 9 and point not in current_basin:
                print("Found new point: ", point)
                current_basin.append(point)
                found_new_point = True
        if found_new_point == False and counter == len(current_basin)-1:
            print("No new points found")
            print("Adding to basin nr ", n_basins, " ", current_basin)
            basin_dict[n_basins] = current_basin
            n_basins += 1
            current_basin = [get_first_point_next_basin(checked,points)]
            counter = 0
        else:
            counter +=1
        if current_point not in checked:
            checked.append(current_point)

    # Find three largest basins
    largest_basin = 0
    three_largest_basins=[]
    while len(three_largest_basins) < 3:
        for key in basin_dict:
            if len(basin_dict[key]) > largest_basin:
                largest_basin = len(basin_dict[key])
                basin_key=key
        three_largest_basins.append(largest_basin)
        largest_basin = 0
        basin_dict.pop(basin_key)
    print(three_largest_basins[0]*three_largest_basins[1]*three_largest_basins[2])
part2()