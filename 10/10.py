def readfile(filename):
    with open('%s.txt' %filename) as f:
        chars=[]
        for line in f:
            temp_list=[]
            numbers=line
            for element in numbers:
                if element !='\n':
                  temp_list.append(element)
            chars.append(temp_list)
    return chars
lines=readfile('input')
left_side=['[','(','<','{']
right_side={}
right_side[')'] = 3
right_side[']'] = 57
right_side['}'] = 1197
right_side['>'] = 25137

def get_next_expected_right(character):
    if character == '[':
        return ']'
    elif character == '(':
        return ')'
    elif character == '<':
        return '>'
    elif character == '{':
        return '}'

next_expected = []
offending_chars = []
completion_strings=[]
line_corrupt = False
for line in lines:
    if line_corrupt == False:
        completion_strings.append(next_expected) # Part2
    line_corrupt = False
    next_expected = []    
    for char in line:
        if line_corrupt == False:
            if char in left_side:
                next_expected.append(get_next_expected_right(char))
            if char in right_side: #else kunne det vært
                if char != next_expected[-1]:
                    offending_chars.append(char)
                    line_corrupt = True
                else:
                    next_expected.pop(-1)
completion_strings.append(next_expected)                    
syntax_error_score = 0
for element in offending_chars:
    syntax_error_score += right_side[element]
print("Syntax error score: ", syntax_error_score)
char_values = {}
char_values[')'] = 1
char_values[']'] = 2
char_values['}'] = 3
char_values['>'] = 4
completion_score = []

for line in completion_strings:
    score = 0
    line.reverse()
    for char in line:

        score *= 5
        score += char_values[char] 
    completion_score.append(score)

# Removing an empty string that appeared for some reason
completion_score.pop(0)
completion_score.sort()

print("Middle score: ",completion_score[len(completion_score)//2])



    
                
        