import time
from tkinter import Tk, Text, Scrollbar, Frame, RIGHT, Y, LEFT
import matplotlib.pyplot as plt
import numpy as np

class NQueensSolverGUI:
    def __init__(self, root, solutions_list):
        self.root = root
        self.root.title("Soluciones Encontradas")
        self.create_gui(solutions_list)

    def create_gui(self, solutions_list):
        frame = Frame(self.root)
        frame.pack()

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        text = Text(frame, wrap="word", yscrollcommand=scrollbar.set, height=20, width=50)
        text.pack(side=LEFT)

        scrollbar.config(command=text.yview)

        for solutions in solutions_list:
            text.insert("end", self.solution_board_to_str(solutions))

    def solution_board_to_str(self, solutions):
        result = ""
        for solution in solutions:
            result += "\n".join([" ".join(["Q" if col == queen else "." for col, queen in enumerate(solution)])])
            result += "\n\n"
        return result

def is_safe(board, row, col, n):
    for i in range(col):
        if board[i] == row or board[i] - i == row - col or board[i] + i == row + col:
            return False
    return True

def solve_n_queens_backtracking_util(board, col, n, solutions):
    if col == n:
        solutions.append(board[:])
        return
    
    for row in range(n):
        if is_safe(board, row, col, n):
            board[col] = row
            solve_n_queens_backtracking_util(board, col + 1, n, solutions)

def solve_n_queens_backtracking(n):
    board = [-1] * n
    solutions = []
    solve_n_queens_backtracking_util(board, 0, n, solutions)
    return solutions

def solve_n_queens_alpha_beta_util(board, col, n, alpha, beta, solutions):
    if col == n:
        solutions.append(board[:])
        return
    
    for row in range(n):
        if is_safe(board, row, col, n):
            board[col] = row
            solve_n_queens_alpha_beta_util(board, col + 1, n, alpha, beta, solutions)
            alpha = max(alpha, row + 1)
            if alpha >= beta:
                return

def solve_n_queens_alpha_beta(n):
    board = [-1] * n
    solutions = []
    solve_n_queens_alpha_beta_util(board, 0, n, float('-inf'), float('inf'), solutions)
    return solutions

def solve_n_queens_heuristic_util(board, col, n, solutions):
    if col == n:
        solutions.append(board[:])
        return
    
    for row in range(n):
        if is_safe(board, row, col, n):
            board[col] = row
            solve_n_queens_heuristic_util(board, col + 1, n, solutions)
            if solutions:
                return

def solve_n_queens_heuristic(n):
    board = [-1] * n
    solutions = []
    solve_n_queens_heuristic_util(board, 0, n, solutions)
    return solutions

def run_experiment(algorithm, n_values):
    times = []
    solutions_list = []
    for n in n_values:
        start_time = time.time()
        solutions = algorithm(n)
        end_time = time.time()
        times.append(end_time - start_time)
        solutions_list.append(solutions)
        print(f"Solutions for N={n}:\n{solutions_list[-1]}\n")
    return times, solutions_list

def main():
    try:
        # Tamaños del problema (N)
        n_values = [10, 10, 10]

        # Medir el tiempo para la implementación inicial
        times_backtracking, solutions_backtracking = run_experiment(solve_n_queens_backtracking, n_values)
        gui_backtracking = NQueensSolverGUI(Tk(), solutions_backtracking)

        # Medir el tiempo para la implementación con poda alfa-beta
        times_alpha_beta, solutions_alpha_beta = run_experiment(solve_n_queens_alpha_beta, n_values)
        gui_alpha_beta = NQueensSolverGUI(Tk(), solutions_alpha_beta)

        # Medir el tiempo para la implementación con heurística inteligente
        times_heuristic, solutions_heuristic = run_experiment(solve_n_queens_heuristic, n_values)
        gui_heuristic = NQueensSolverGUI(Tk(), solutions_heuristic)

        # Graficar los tiempos de ejecución
        bar_width = 0.25
        index = np.arange(len(n_values))

        plt.bar(index, times_backtracking, width=bar_width, label='Backtracking')
        plt.bar(index + bar_width, times_alpha_beta, width=bar_width, label='Backtracking con poda')
        plt.bar(index + 2*bar_width, times_heuristic, width=bar_width, label='Heurísticas Inteligentes')

        plt.xlabel('Tamaño del tablero (N)')
        plt.ylabel('Tiempo de ejecución (segundos)')
        plt.xticks(index + bar_width, n_values)
        plt.legend()
        plt.show()

        Tk().mainloop()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()