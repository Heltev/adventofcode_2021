def readfile(filename):
    with open('%s.txt' %filename) as f:
      if filename == 'input':
        for line in f:
            numbers=line.strip().split(',')
            for x in range(len(numbers)):
                numbers[x]=int(numbers[x])
            return numbers
      if filename == 'boards':
          boards=[]
          for line in f:
              temp_list=[]
              #print(line)
              numbers=line.strip().split(' ')
              for element in numbers:
                  if element !='':
                    temp_list.append(int(element))
              boards.append(temp_list)
              #print(numbers)
              #boards+=numbers
    return boards

def is_winner(board):
    for row in board:
        if sum(row) == (-5):
            return 1
    temp_col=[]
    for col in range(5):
        for row in range(5):
            temp_col.append(board[row][col])
        if sum(temp_col) == -5:
            return 1
        temp_col = []
    return 0
    
def get_rest_sum(board):
    tot_sum=0
    for row in range(5):
        for col in range(5):
            if board[row][col] != -1:
                tot_sum += board[row][col]
    return tot_sum


def main():
    numbers=readfile('input')
    boards=readfile('boards')
    matrix=[]
    temp_row=[]
    last_row=boards[-1]
    for row in boards:
        if row == []:
            matrix.append(temp_row)
            temp_row=[]
        elif row == last_row:
            temp_row.append(row)
            matrix.append(temp_row)
        else:
            temp_row.append(row)
    num_winners=0
    winner_boards=[]
    winner_loser_score=[]
    for bingo_number in numbers:
        for board in range(len(matrix)):
            for row in range(len(matrix[board])):
                for number in range(len(matrix[board][row])):
                    if matrix[board][row][number] == bingo_number:
                        matrix[board][row][number] = -1
                        winner = is_winner(matrix[board])
                        if winner == 1 and board not in winner_boards:
                            num_winners+=1
                            winner_boards.append(board)
                            if num_winners == len(matrix):
                                total_sum = get_rest_sum(matrix[board])
                                final_score=bingo_number*total_sum
                                winner_loser_score.append(final_score)
                                return winner_loser_score
                            elif num_winners == 1:
                                total_sum = get_rest_sum(matrix[board])
                                final_score=bingo_number*total_sum
                                winner_loser_score.append(final_score)

print("Winner, loser: ", main())