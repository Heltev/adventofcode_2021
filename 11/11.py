def readfile(filename):
    with open('%s.txt' %filename) as f:
        squids=[]
        for line in f:
            temp_list=[]
            numbers=line
            for element in numbers:
                if element !='\n':
                  temp_list.append(int(element))
            temp_list.insert(0,NEGATIVE)
            temp_list.append(NEGATIVE)
            squids.append(temp_list)
    border = [NEGATIVE]
    squids.insert(0,border*(len(squids)+2))
    squids.append(border*(len(squids)+1))
    return squids

NEGATIVE = -1

squids = readfile('input')
flashed=[]

def get_adjacent_points_coordinates(point_row,point_col):
    adj = []
    for row in range(point_row-1,point_row+2):
        for col in range(point_col-1,point_col+2):
            if row != point_row or col != point_col:
                if squids[row][col] >= 0:
                    adj.append((row,col))
    return adj

def iterate():
    for row in range(1,len(squids)-1):
        for col in range(1,len(squids[row])-1):
            squids[row][col] += 1
    
def find_flashes():
    flash = []
    for row in range(1,len(squids)-1):
        for col in range(1,len(squids[row])-1):
            if squids[row][col] >= 10:
                flash.append((row,col))
    return flash

def flash(flashers):
    total_flashes = 0
    flashes = 0
    new_flashes = []
    for flasher in flashers:
        flashes_sum,new_flashes = update_adj(flasher)
        total_flashes += flashes
        for point in new_flashes:
            if point not in flashers:
                flashers.append(point)
    return total_flashes

def update_adj(point):
    total_flashes = 0
    new_flashes = []
    adj_points = get_adjacent_points_coordinates(point[0],point[1])
    for adj_point in adj_points:
        if adj_point not in flashed and squids[adj_point[0]][adj_point[1]] > 0:
            squids[adj_point[0]][adj_point[1]] += 1
        if squids[adj_point[0]][adj_point[1]] >= 10:
            total_flashes += 1
            new_flashes.append(adj_point)
    flashed.append(point)
    return total_flashes,new_flashes

def reset_flashers():
    for row in range(1,len(squids)-1):
        for col in range(1,len(squids[row])-1):
            if squids[row][col] >= 10:
                squids[row][col] = 0
    
def count_flashes():
    flashes = 0
    for row in range(1,len(squids)-1):
        for col in range(1,len(squids[row])-1):
            if squids[row][col] == 0:
                flashes += 1
    return flashes

def display():
    for row in squids[1:len(squids)-1]:
        print(row[1:len(row)-1])

total_flashes = 0
iterations = 100
sync = False
counter = 0
while sync == False:
    iterate()
    flash(find_flashes())
    reset_flashers()
    if len(flashed) == iterations:
        sync = True
    flashed = []
    if counter < iterations:
        total_flashes += count_flashes()
    counter +=1
print("Squid flashes after", iterations, " steps: ", total_flashes)
print("Squids synced after step: ", counter)

