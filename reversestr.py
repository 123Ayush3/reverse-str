# def find_largest_number(numbers):

#     if not numbers:
#         return None  
#     largest = numbers[0]
#     for num in numbers[1: ]:
#         if num > largest:
#             largest = num

#     return largest
# numbers_list = [14, 20, 3]
# largest_number = find_largest_number(numbers_list)

# print(f"The largest number is: {largest_number}")

board = [['R', 'N', 'B', 'Q', 'K'],
         ['P', 'P', 'P', 'P', 'P'],
         ['.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.'],
         ['p', 'p', 'p', 'p', 'p'],
         ['r', 'n', 'b', 'q', 'k']]
def print_board(board):
    separator = '   '
    for row in board:
        print(separator.join(row))
        print(separator)
    def initialize_game():
        print_board(board)
    def get_move():
      move = input("Enter your move: ")
      piece_type, source_row, source_column = move[0], move[1], move[2]
      return piece_type, source_row, source_column
    def main():
      initialize_game()
    while True:
        piece_type, source_row, source_column = get_move()
        if piece_type.lower() == 'q':
            break
        validate_move(piece_type, source_row, source_column)

        main()
        def validate_move(piece_type, source_row, source_column):
           if board[int(source_row) - 1][int(source_column) - 1] == piece_type.upper():
            print("Valid move.")
    else:
     print("Invalid move.")