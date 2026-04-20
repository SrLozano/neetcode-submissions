class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check rows
        for row in board:
            numbers_count = 0
            for element in row:
                if element != '.':
                    numbers_count +=1 
            
            if len(set(row)) - 1 != numbers_count:
                return False

        # check columns 
        for column in range(len(board)):
            numbers_count = 0
            numbers_set = set()
            for row in range(len(board)):
                if board[row][column] != '.':
                    numbers_count += 1
                    numbers_set.add(board[row][column])

            if len(numbers_set) != numbers_count:
                print("false 2")
                return False

        # check sub-boxes
        for square in range(9):
            numbers_count = 0
            numbers_set = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square//3) * 3 + j
                    
                    if board[row][col] != '.':
                        numbers_count += 1
                        numbers_set.add(board[row][col])

            if len(numbers_set) != numbers_count:
                print("false 3")
                return False

        return True