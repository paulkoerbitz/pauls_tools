"""Unit test for math.py"""

from pauls_tools import math
import inspect
import unittest
import numpy as np
import itertools
import pdb

def close_enough(x, y, tol=1e-3):
    return np.abs(x-y) < tol

def matrix_close_enough(x, y, tol=1e-3):
    return np.linalg.norm(x-y) < tol

class DiffTest(unittest.TestCase):
    known_values = ({"f": (lambda x: 0), "x": 0.0, "i": 0, "expected": 0.0},
                    {"f": (lambda x: x), "x": 0.0, "i": 0, "expected": 1.0},
                    {"f": (lambda x: x**2), "x": 1.0, "i": 0, "expected": 2.0},
                    {"f": (lambda x: x**3), "x": 1.0, "i": 0, "expected": 3.0},
                    {"f": (lambda x: np.sin(x)), "x": 0.0, "i": 0, "expected": 1.0},
                    {"f": (lambda x: np.cos(x)), "x": 0.0, "i": 0, "expected": 0.0},
                    {"f": (lambda x: sum(x)), "x": np.zeros(2), "i": 0,
                     "expected": 1.0},
                    {"f": (lambda x: sum(x)), "x": np.zeros(2), "i": 1,
                     "expected": 1.0},
                    {"f": (lambda x: sum(x**2)), "x": np.ones(2), "i": 0,
                     "expected": 2.0},
                    {"f": (lambda x: sum(x**2)), "x": np.ones(2), "i": 1,
                     "expected": 2.0},
                    {"f": (lambda x: sum(x**2)), "x": np.ones(2), "i": 1,
                     "expected": 2.0},
                    {"f": (lambda x: sum(x**2)), "x": np.ones(2), "i": 1,
                     "expected": 2.0},
                    {"f": (lambda x: sum(x**2)), "x": np.ones(2), "i": 1,
                     "expected": 2.0},
                    {"f": (lambda x: sum(x**2)), "x": np.ones(2), "i": 1,
                     "expected": 2.0},
                    {"f": (lambda x: np.sin(x[0]**2)*np.cos(x[1])),
                     "x": np.pi/2*np.ones(2), "i": 0, "expected": 0.0},
                    {"f": (lambda x: np.sin(x[0]**2)*np.cos(x[1])),
                     "x": np.pi/2*np.ones(2), "i": 1,
                     "expected": -np.sin(np.pi**2/4.)},
                    )

    def test_known_values(self):
        """Test derivatives of functions with known derivatives"""
        for k in self.known_values:
            result = math.diff(k["f"], k["x"], k["i"])
            self.assertTrue(close_enough(result,k["expected"]))

class Diff2Test(unittest.TestCase):
    known_values = ({"f": lambda x: 1.0, "dim": 1, "exp": (lambda x: 0.0,)},
                    {"f": lambda x: x, "dim": 1, "exp": (lambda x: 0.0,)},
                    {"f": lambda x: sum(x**2), "dim": 2,
                     "exp": (lambda x: 2.0, lambda x: 0.0,
                                  lambda x: 0.0, lambda x: 2.0)},
                    {"f": lambda x: sum(x)**2, "dim": 2,
                     "exp": (lambda x: 2.0,)*4},
                    {"f": lambda x: np.product(x)**2, "dim": 2,
                     "exp": (lambda x: 2*x[1]**2, lambda x: 4*x[0]*x[1],
                             lambda x: 4*x[0]*x[1], lambda x: 2*x[0]**2)},
                    {"f": lambda x: np.exp(x[0]*x[1]), "dim": 2,
                     "exp": (lambda x: x[1]**2*np.exp(x[0]*x[1]),
                             lambda x: (1.0+x[0]*x[1])*np.exp(x[0]*x[1]),
                             lambda x: (1.0+x[0]*x[1])*np.exp(x[0]*x[1]),
                             lambda x: x[0]**2*np.exp(x[0]*x[1])),
                     "tol": 5e-2, "eps": 0.01},
                    )

    def run_assert(self, f, x, exp, i, j, no, tol=1e-3, eps=0.01):
        result = math.diff2(f, x, i, j, eps)
        expect = exp(x)
        try:
            self.assertTrue(close_enough(result,expect,tol))
        except AssertionError as e:
            print("Error in test case no. %d expected %f, got %f" \
                      % (no, expect, result))
            raise e

    def test_known_values(self):
        """Test diff2 against a series of known mixed second derivatives"""
        for no,k in enumerate(self.known_values):
            for ind,(i,j) in\
                    enumerate(itertools.product(range(k["dim"]), range(k["dim"]))):
                if k["dim"] == 1:
                    for x in np.linspace(-2.0,0.1,2.0):
                        self.run_assert(k["f"], x, k["exp"][ind], i, j, no,
                                        k.get("tol",1e-3))
                elif k["dim"] == 2:
                    for x in np.linspace(-2.0,0.1,2.0):
                        for y in np.linspace(-2.0,0.1,2.0):
                            z = np.array([x,y])
                            self.run_assert(k["f"], z, k["exp"][ind], i, j, no,
                                            k.get("tol",1e-3), k.get("eps",1e-2))
                else:
                    raise RuntimeError("Diff2Test: No testcase for dim > 2")

class ShrinkMatrixTest(unittest.TestCase):
    known_values = ({"factor": 0.5, "in": np.ones((2,2))/2,
                     "exp": np.array([[1+np.sqrt(6), 1.],[1, 1+np.sqrt(6)]])/4.0,
                     "tol": 0.001},)

    not_2d_matrices = (np.ones((3,3,3)), np.ones((3,)))

    not_square_matrices = (np.ones((3,4)),)

    def test_throws_if_not_2d(self):
        """
        Test that shrink_matrix throws a ValueError if the entered
        matrix is not 2d.
        """
        for n2d in self.not_2d_matrices:
            self.assertRaises(ValueError, math.shrink_matrix, n2d)

    def test_throws_if_not_square(self):
        """
        Test that shrink_matrix throws a ValueError if the entered
        matrix is not square.
        """
        for n_sq in self.not_square_matrices:
            self.assertRaises(ValueError, math.shrink_matrix, n_sq)

    def test_known_values(self):
        """
        Test that shrinkage returns the expected results for known values.
        """
        for k in self.known_values:
            self.assertTrue(
                matrix_close_enough(math.shrink_matrix(k["in"],k["factor"]),
                                    k["exp"], k["tol"]))


if __name__ == "__main__":
    unittest.main()
