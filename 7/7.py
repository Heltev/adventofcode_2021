def readfile():
    with open('input.txt') as f:
      for line in f:
        numbers=line.strip().split(',')
    for x in range(len(numbers)):
        numbers[x]=int(numbers[x])

    return numbers

def average(fuel_consumption):
    total_fuel=sum(fuel_consumption)
    return total_fuel/len(fuel_consumption)
    
positions=readfile()
# Part 1
#positions=[16,1,2,0,4,2,7,1,2,14]
averages={}
for element in positions:
    fuel=[]
    for x in range(len(positions)):
        distance=element-positions[x]
        if distance <0:
            distance=-distance
        fuel.append(distance)
        averages[element]=average(fuel)
total_fuel_consumption = min(averages.values())*len(positions)
print("Total fuel consumption, part 1: ",total_fuel_consumption)

averages={}
for x in range(max(positions)+1):
    fuel=[]
    for element in positions:
        distance=element-x
        if distance <0:
            distance=-distance
        for step in range(distance):
            distance+=step
        fuel.append(distance)
        averages[x]=average(fuel)
total_fuel_consumption = min(averages.values())*len(positions)
print("Total fuel consumption, part 2: ",total_fuel_consumption)