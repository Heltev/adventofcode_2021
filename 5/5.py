def readfile():
    coordinates=[]
    with open('input.txt') as f:
      for line in f:
        start=[]
        stop=[]
        coord=[]
        numbers=line.strip().split('->')
        start = [int(i) for i in numbers[0].split(',')]
        stop = [int(i) for i in numbers[1].split(',')]
        coord.append(start)
        coord.append(stop)
        coordinates.append(coord)
    return coordinates

def remove_diagonal(coordinates):
    straight_coordinates=[]
    for line in coordinates:
        if (line[0][0] == line[1][0]) or (line[0][1] == line[1][1]):
            straight_coordinates.append(line)
    return straight_coordinates

def create_line(start,stop):
    line_segment=[]
    #Vertical line
    if start[0] == stop [0]:
        if (start[1] < stop[1]):
            for y in range(start[1],stop[1]+1):
                line_segment.append([start[0],y])
        else:
            for y in range(start[1],stop[1]-1,-1):
                line_segment.append([start[0],y])
    #Horizontal line
    elif start[1] == stop[1]:
        if start[0] < stop[0]:
            for x in range(start[0],stop[0]+1):
                line_segment.append([x,start[1]])
        else:
            for x in range(start[0],stop[0]-1,-1):
                line_segment.append([x,start[1]])
    #Diagonal line
    else:
        counter=0
        if start[1] > stop[1]:
            ## Descending y
            if start[0] > stop[0]:
                # Descending x
                for x in range(start[0],stop[0]-1,-1):
                    y=start[1]-counter
                    line_segment.append([x,y])
                    counter+=1
            else:
                # Ascending x
                for x in range(start[0],stop[0]+1):
                    y=start[1]-counter
                    line_segment.append([x,y])
                    counter+=1
        else:
            ## Ascending y
            if start[0] > stop[0]:
                # Descending x
                for x in range(start[0],stop[0]-1,-1):
                    y=start[1]+counter
                    line_segment.append([x,y])
                    counter+=1
            else:
                # Ascending x
                for x in range(start[0],stop[0]+1):
                    y=start[1]+counter
                    line_segment.append([x,y])
                    counter+=1

    return line_segment

def main():
    marked_points_straight = {}
    marked_points={}
    coordinates = readfile()
    straight_coordinates=remove_diagonal(coordinates)
    for end_points in coordinates:
        line_segment = create_line(end_points[0], end_points[1])
        for point in line_segment:
            if str(point) in marked_points:
                marked_points[str(point)] +=1
            else:
                marked_points[str(point)] = 1
            if end_points in straight_coordinates:
                if str(point) in marked_points_straight:
                    marked_points_straight[str(point)] +=1
                else:
                    marked_points_straight[str(point)] = 1
    danger_points = 0
    danger_points_straight = 0
    for value in marked_points.values():
        if value > 1:
            danger_points += 1
    for value in marked_points_straight.values():
        if value > 1:
            danger_points_straight += 1
    print("Number of danger points, straight lines: ", danger_points_straight)
    print("Number of danger points, all lines: ", danger_points)

main()