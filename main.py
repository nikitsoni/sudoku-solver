from tabulate import tabulate
from collections import defaultdict
import time

class SudokuSolver:
    
    def __init__(self):
        
        self.row = defaultdict(set)
        self.column = defaultdict(set)
        self.square = defaultdict(set)
        self.result = []
    
    def verify(self, value, row, col):
        
        if value in self.row[row] or value in self.column[col] or value in self.square[(row // 3, col // 3)]:
            return False

        return True

    def backtrack_solver(self, idx, board):
        
        if idx == 81:
            temp_board = board.copy()
            self.result = temp_board
            return True
        
        row = idx // 9
        col = idx % 9

        if board[row][col] != ".":
            return self.backtrack_solver(idx + 1, board)
        else:
            for val in range(1, 10):
                if self.verify(val, row, col):
                    
                    self.row[row].add(val)
                    self.column[col].add(val)
                    self.square[(row//3, col//3)].add(val)

                    board[row][col] = str(val)
                    # print_sudoku(board)
                    # time.sleep(1)

                    if self.backtrack_solver(idx + 1, board):
                        return True

                    self.row[row].remove(val)
                    self.column[col].remove(val)
                    self.square[(row//3, col//3)].remove(val)
            
            return False 


    def solve_board(self, board):
        
        # Add given numbers in the respective positional hashmap
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num != ".":
                    self.row[row].add(num)
                    self.column[col].add(num)
                    self.square[(row // 3, col // 3)].add(num)
        
        # Initiate Backtracking for the solution.
        self.backtrack_solver(0, board)
        return self.result

def print_sudoku(board):
    # Replace dots and zeros with underscore for a cleaner look
    formatted_board = [['_' if num == 0 or num == '.' else num for num in row] for row in board]

    # Prepare the table with tabulaßte
    table = tabulate(formatted_board, tablefmt="fancy-grid", numalign="center", stralign="center")

    print(table)


def main():

    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    
    print("Unsolved Board: ")
    print_sudoku(board)

    sudoku_solver_instance = SudokuSolver()
    solved_board = sudoku_solver_instance.solve_board(board)
    
    print("Solved Board: ")
    print_sudoku(solved_board)

if __name__ == "__main__":
    main()
