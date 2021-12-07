def readfile():
    with open('input.txt') as f:
      lines = f.read().splitlines()
    return lines

def transpose_data(lines):
    n=[]
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if y==0:
                n.insert(x,lines[y][x])
            else:
                n[x]+=lines[y][x]
    return n

def get_most_frequent_number(numbers):
    n_numbers = len(numbers)
    if numbers.count('0') > n_numbers/2:
        return 0
    else:
        return 1

def binary_to_decimal(binary):
    decimal_sum=0
    for x in range(len(binary)):
        decimal_sum+=2**(len(binary)-x-1)*binary[x]
    return decimal_sum


def main():
    lines=readfile()
    lines_transposed = transpose_data(readfile())
    #lines_transposed = transpose_data(test)
    #print(lines_transposed)
    gamma_rate=[]
    epsilon_rate=[]
    for line in lines_transposed:
        most_frequent_number=get_most_frequent_number(line)
        gamma_rate.append(most_frequent_number)
        epsilon_rate.append((most_frequent_number-1)**2)
    gamma_rate_decimal = binary_to_decimal(gamma_rate)
    epsilon_rate_decimal = binary_to_decimal(epsilon_rate)
    
    print("Power consumotion: ",gamma_rate_decimal*epsilon_rate_decimal)

    # Part 2
    counter = -1
    oxy_lines=lines
    co2_lines=lines
    while len(oxy_lines) > 1:
        counter+=1
        next_list_oxy=[]
        transpose_element_oxy=transpose_data(oxy_lines)[counter]
        most_frequent_number = get_most_frequent_number(transpose_element_oxy)
        for line in oxy_lines:
            if int(line[counter]) == most_frequent_number:
                next_list_oxy.append(line)
        oxy_lines=next_list_oxy
    counter=-1
    while len(co2_lines) > 1:
        counter+=1
        next_list_co2=[]
        transpose_element_co2=transpose_data(co2_lines)[counter]
        least_frequent_number = (get_most_frequent_number(transpose_element_co2)-1)**2

        for line in co2_lines:
            if int(line[counter]) == least_frequent_number:
                next_list_co2.append(line)
        co2_lines=next_list_co2

    print("Oxygen generator rating: ", oxy_lines)
    print("CO2 scrubber rating: ",co2_lines)


main()
