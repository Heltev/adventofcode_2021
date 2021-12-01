def readfile():
  with open('input.txt') as f:
    lines = f.read().splitlines()
  numbers = [int(line) for line in lines]
  return numbers
  

def find_sum_of_3(first,second,third):
  return first+second+third

def main():
  ## part 1
  prev_dep = 100000000
  n_increases = 0
  depths = readfile()
  for line in depths:
    if prev_dep < line:
      n_increases +=1
    prev_dep = line
  print(n_increases)
  
  ## part 2
  prev_sum=10000000
  n_sum_increases = 0
  for x in range(0,len(depths)-2,1):
    current_sum = find_sum_of_3(depths[x], depths[x+1],depths[x+2])
    if current_sum > prev_sum:
      n_sum_increases +=1
    prev_sum = current_sum
  print(n_sum_increases)
main()