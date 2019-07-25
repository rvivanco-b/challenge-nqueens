from models.solution import Solution
from strategies.backtracking_nqueen import BacktrackingNQueensSolver

class NQueenService:

    def __init__(self, n):
        self.n = n


    def _find_calculated_solutions(self):
        database_solutions = Solution.find_by_n(self.n)
        if database_solutions:
            return True
        return False


    def calculate_solutions(self):
        queens_solver = BacktrackingNQueensSolver(self.n)
        all_solutions = queens_solver.find_all_solutions()
        if not self._find_calculated_solutions():
            self._save_solutions(all_solutions)

        return all_solutions


    def _save_solutions(self, solutions):
        for sol in solutions:
            s = Solution(self.n, str(sol).strip('[]'))
            s.save()
