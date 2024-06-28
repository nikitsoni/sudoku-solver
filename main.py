from tabulate import tabulate
import time
import os
from typing import List, Set

class SudokuSolver:
    
    def backtracking(self, board: List[List[str]], row: int, col: int, rows_values: List[Set[str]], cols_values:List[Set[str]], row_col_values: List[List[Set[str]]]) -> True:
    
        clear_screen()
        print_sudoku(board)
        time.sleep(0.001)

        if row == 9:
            return True
        
        if col == 9:
            return self.backtracking(board, row + 1, 0, rows_values, cols_values, row_col_values)
        
        if board[row][col] != ".":
            return self.backtracking(board, row, col + 1, rows_values, cols_values, row_col_values)
        
        for digit in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            
            if not digit in rows_values[row] and not digit in cols_values[col] and not digit in row_col_values[row//3][col//3]:
                
                board[row][col] = digit
                rows_values[row].add(digit)
                cols_values[col].add(digit)
                row_col_values[row//3][col//3].add(digit)
                
                if self.backtracking(board, row, col+1, rows_values, cols_values, row_col_values):
                    return True
                
                board[row][col] = "."
                rows_values[row].remove(digit)
                cols_values[col].remove(digit)
                row_col_values[row//3][col//3].remove(digit)
        
        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
       
        rows_values: List[Set[str]] = [set() for _ in range(9)]
        cols_values:List[Set[str]] = [set() for _ in range(9)] 
        row_col_values: List[List[Set[str]]] = [
            [set() for _ in range(9)] 
            for _ in range(9)
        ]

        for row in range(9):
            for col in range(9):
                digit = board[row][col] 
                if digit != ".":
                    rows_values[row].add(digit)
                    cols_values[col].add(digit)
                    row_col_values[row//3][col//3].add(digit)
        
        for row in range(9):
            for col in range(9):
                digit = board[row][col] 
                if digit == ".":
                    self.backtracking(board, row, col, rows_values, cols_values, row_col_values)
        
        return board



def print_sudoku(board):
    # Replace dots and zeros with underscore for a cleaner look
    formatted_board = [['_' if num == 0 or num == '.' else num for num in row] for row in board]

    # Prepare the table with tabulate
    table = tabulate(formatted_board, tablefmt="mixed_grid", numalign="center", stralign="center")

    print(table)

def clear_screen():
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

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
    
    sudoku_solver_instance = SudokuSolver()
    solved_board = sudoku_solver_instance.solveSudoku(board)
    
    print("Solved Board: ")
    print_sudoku(solved_board)

if __name__ == "__main__":
    main()
