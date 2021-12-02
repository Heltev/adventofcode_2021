def readfile():
  with open('input.txt') as f:
    lines = f.read().splitlines()
  return lines


def part1():
  course=readfile()
  x_pos,y_pos=0,0
  for line in course:
    command,value=line.split()
    if command == "up":
      y_pos -= int(value)
    elif command == "down":
      y_pos += int(value)
    else:
      x_pos += int(value)
  print(x_pos*y_pos)

part1()

def part2():
  course=readfile()
  x_pos,y_pos,aim=0,0,0
  for line in course:
    command,value=line.split()
    if command == "up":
      aim -= int(value)
    elif command == "down":
      aim += int(value)
    else:
      x_pos += int(value)
      y_pos += (aim*int(value))
  print(x_pos*y_pos)

part2()