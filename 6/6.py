def readfile():
    with open('input.txt') as f:
      for line in f:
        numbers=line.strip().split(',')
    for x in range(len(numbers)):
        numbers[x]=int(numbers[x])

    return numbers

## Part 2
fish = readfile()

fish_dict={}
fish_dict[0]=0
for x in range(1,6):
    fish_dict[x]=fish.count(x)
fish_dict[6]=0
fish_dict[7]=0
fish_dict[8]=0
for day in range(256):
    ready=fish_dict[0]
    for element in fish_dict:
        if element+1 in fish_dict:
            fish_dict[element] = fish_dict[element+1]
    fish_dict[8]=ready
    fish_dict[6]+=ready
sum=0
for element in fish_dict:
    sum+=fish_dict[element]

print("After 256 days: ", sum)

## Part 1
for day in range(80):
    ready=fish.count(0)
    for x in range(len(fish)):
        if fish[x]==0:
            fish[x]=6
        else:
            fish[x]-=1
    
    for x in range(ready):
        fish.append(8)

print("After 80 days: ",len(fish))