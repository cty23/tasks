import unittest
from 8_queens_solver import solve_n_queens

class TestNQueensSolver(unittest.TestCase):
    def test_n_4(self):
        """Test the solver with N=4."""
        result = []
        def capture_solution(board):
            result.append([row[:] for row in board])

        solve_n_queens(4, capture_solution)
        self.assertEqual(len(result), 2)  # There are 2 solutions for N=4

    def test_n_8(self):
        """Test the solver with N=8."""
        result = []
        def capture_solution(board):
            result.append([row[:] for row in board])

        solve_n_queens(8, capture_solution)
        self.assertEqual(len(result), 92)  # There are 92 solutions for N=8

if __name__ == "__main__":
    unittest.main()
