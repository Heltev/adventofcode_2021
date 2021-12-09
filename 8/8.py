def readfile():
    lines=[]
    with open('input.txt') as f:
      for line in f:
        lines.append(line.strip().split('|'))
    return lines
#lines=['be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe','edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc']
#fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |
#cg cg fdcagb cbg
#fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |
#efabcd cedba gadfec cb
#aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |
#gecf egdcabf bgf bfgea
#fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |
#gebdcfa ecba ca fadegcb
#dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |
#cefg dcbef fcge gbcadfe
#bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |
#ed bcgafe cdgba cbgef
#egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |
#gbdfcae bgc cg cgb
#gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |
#fgae cfgab fg bagce
output=[]
def part1():
    targets_found=0
    target_length = [2,3,4,7]
    lines=readfile()
    output_values= [line[-1].split(' ') for line in lines]
    for line in output_values:
        for number in line:
            if len(number) in target_length:
                targets_found+=1

    print(targets_found)

def get_top(one,seven):
    for char in seven:
        if char not in one:
            return char

def get_bottom_sides(input_lines):
    occurrences = {}
    for element in input_lines:
        for char in ['a','b','c','d','e','f','g']:
            if char in occurrences:
                occurrences[char] += element.count(char)
            else:
                occurrences[char] = element.count(char)
    for element in occurrences:
        if occurrences[element] == 9:
            bottom_right = element
        if occurrences[element] == 4:
            bottom_left = element
    return bottom_right,bottom_left

def get_top_left(input_lines):
    occurrences = {}
    for element in input_lines:
        for char in ['a','b','c','d','e','f','g']:
            if char in occurrences:
                occurrences[char] += element.count(char)
            else:
                occurrences[char] = element.count(char)
    for element in occurrences:
        if occurrences[element] == 6:
            return element

def get_top_right(input_lines,decode_dict):
    for line in input_lines:
        if len(line) == 2:
            for char in line:
                if char not in decode_dict.values():
                    return char

def get_middle(input_lines,decode_dict):
    for line in input_lines:
        if len(line) == 4:
            for char in line:
                if char not in decode_dict.values():
                    return char

def get_bottom(decode_dict):
    for char in ['a','b','c','d','e','f','g']:
        if char not in decode_dict.values():
            return char

def get_code_for_one(codes):
    return [code for code in codes if len(code) == 2]

def get_code_for_seven(codes):
    return [code for code in codes if len(code) == 3]

def decode_line(line):
    decoded = {}
    one_code = str(get_code_for_one(line))
    seven_code = str(get_code_for_seven(line))
    decoded['t'] = get_top(one_code,seven_code)
    decoded['br'],decoded['bl'] = get_bottom_sides(line)
    decoded['tl']=get_top_left(line)
    decoded['tr'] = get_top_right(line,decoded)
    decoded['m'] = get_middle(line,decoded)
    decoded['b'] = get_bottom(decoded)
    return decoded

def code_to_number(decoder):
    code_to_number = {}
    code_to_number['0'] = decoder['t']+decoder['tr']+decoder['br']+decoder['b']+decoder['bl']+decoder['tl']
    code_to_number['1'] = decoder['tr']+decoder['br']
    code_to_number['2'] = decoder['t']+decoder['tr']+decoder['b']+decoder['bl']+decoder['m']
    code_to_number['3'] = decoder['t']+decoder['tr']+decoder['br']+decoder['b']+decoder['m']
    code_to_number['4'] = decoder['tr']+decoder['br']+decoder['tl']+decoder['m']
    code_to_number['5'] = decoder['t']+decoder['br']+decoder['b']+decoder['tl']+decoder['m']
    code_to_number['6'] = decoder['t']+decoder['br']+decoder['b']+decoder['bl']+decoder['tl']+decoder['m']
    code_to_number['7'] = decoder['t']+decoder['tr']+decoder['br']
    code_to_number['8'] = decoder['t']+decoder['tr']+decoder['br']+decoder['b']+decoder['bl']+decoder['tl']+decoder['m']
    code_to_number['9'] = decoder['t']+decoder['tr']+decoder['br']+decoder['b']+decoder['tl']+decoder['m']
    return code_to_number

def strings_equal(decoder, code):
    for char in code:
        if char not in decoder:
            return False
    for char in decoder:
        if char not in code:
            return False
    return True

## t,tr,br,b,bl,tl,m
## a,b,c,d,e,f,g
def part2():
    lines=readfile()
    output_answer=[]
    input_codes = [line[0].split(' ')[:-1] for line in lines]
    output_codes = [line[1].split(' ')[1:] for line in lines]
    for x in range(len(input_codes)):
        decoded_output =[]
        decoded_line = decode_line(input_codes[x])
        decoder=code_to_number(decoded_line)
        for code in output_codes[x]:
            for number in range(0,10):
                if strings_equal(decoder[str(number)],code) == True:
                    decoded_output.append(str(number))
        output_string = ''
        for element in decoded_output:
            output_string += element
        output_answer.append(int(output_string))
    print(sum(output_answer))

part2()
#for char in ['a','b','c','d','e','f','g']:
#    print(char)
#lines=readfile()
#input_codes = [line[0].split(' ')[:-1] for line in lines]
#dec={}
##print(input_codes)
#dec['t'] = get_top('abd','ab')
#dec['br'],dec['bl'] = get_bottom_sides(input_codes[0])
#dec['tl']=get_top_left(input_codes[0])
#dec['tr'] = get_top_right(input_codes[0],dec)
#dec['m'] = get_middle(input_codes[0],dec)
#dec['b'] = get_bottom(dec)
#d=decode_line(['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab'])
#c = ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf']
#b=[]
#e=code_to_number(d)
#w=''
#for l in c:
#    for x in range(0,10):
#        if strings_equal(e[str(x)],l) == True:
#            b.append(str(x))
#for element in b:
#    w+=element
#print(int(w)+1)
