"""file for testing budget_tangency"""
import unittest
import sympy as sp
from budget_tangency import BudgetFinder




class TestBudgetFinder(unittest.TestCase):
    """test class for budget_tangency"""

    def setUp(self):
        # Initialize a BudgetFinder object for testing
        self.budget_finder = BudgetFinder("x2*x1", 3, 2, 30)

    def test_find_optimal_mrs(self):
        """tests the find_optimal_mrs function"""
        # Test the find_optimal_mrs() method

        # Call the method
        result = self.budget_finder.find_optimal_mrs()

        # Extract the x1 and x2 values from the dictionary
        x1 = result[sp.Symbol('x1')]
        x2 = result[sp.Symbol('x2')]

        # Assert the result
        self.assertAlmostEqual(x1, 5)
        self.assertAlmostEqual(x2, 7.5)


        new_utility = "x1**3*x2"
        self.budget_finder.modify_utility(new_utility)

        # Recalculate optimal values after modifying the utility function
        result = self.budget_finder.find_optimal_mrs()

        # Extract the x1 and x2 values again
        x1 = result[sp.Symbol('x1')]
        x2 = result[sp.Symbol('x2')]

        self.assertAlmostEqual(x1, 7.5)
        self.assertAlmostEqual(x2, 3.75)


        new_utility = "x1*x2**3"
        self.budget_finder.modify_utility(new_utility)

        # Recalculate optimal values after modifying the utility function
        result = self.budget_finder.find_optimal_mrs()

        # Extract the x1 and x2 values again
        x1 = result[sp.Symbol('x1')]
        x2 = result[sp.Symbol('x2')]

        self.assertAlmostEqual(x1, 2.5)
        self.assertAlmostEqual(x2, 11.25)

        self.budget_finder.price_one = 10
        self.budget_finder.price_two = 5
        self.budget_finder.total_money = 60
        self.budget_finder.utility = "x1**5*x2**3"

        # Recalculate optimal values after modifying the attributes
        result = self.budget_finder.find_optimal_mrs()

        # Extract the x1 and x2 values again
        x1 = result[sp.Symbol('x1')]
        x2 = result[sp.Symbol('x2')]

        self.assertAlmostEqual(x1, 3.75)
        self.assertAlmostEqual(x2, 4.5)


    def test_budget_line_points(self):
        """tests whether the budget_line_points are accurate"""

        result = self.budget_finder.budget_line_points()
        self.assertEqual(result, [(0, 15.0), (1, 13.5), (2, 12.0), (3, 10.5), (4, 9.0),
                                  (5, 7.5), (6, 6.0), (7, 4.5), (8, 3.0), (9, 1.5), (10, 0.0)])

    def test_modify_price_one(self):
        """tests whether the modify price one works"""

        new_price = 5  # Set a new price

        self.budget_finder.modify_price_one(new_price)

        self.assertEqual(self.budget_finder.price_one, new_price)

    def test_modify_price_two(self):
        """tests whether the modify price two works"""

        new_price = 12
        self.budget_finder.modify_price_two(new_price)

        self.assertEqual(self.budget_finder.price_two, new_price)

    def test_modify_total(self):
        """tests whether the modify total works"""

        # Test the modify_total() method
        new_total = 100  # Set a new total

        # Call the method to modify the total
        self.budget_finder.modify_total(new_total)

        # Assert that the total has been modified
        self.assertEqual(self.budget_finder.total_money, new_total)

    def test_modify_utility(self):
        """tests whether the modify utility works"""

        new_utility = "x1**3*x2"  # Set a new utility function

        # Call the method to modify the utility function
        self.budget_finder.modify_utility(new_utility)
        test_case = sp.sympify(new_utility)
        # Assert that the utility function has been modified
        self.assertEqual(self.budget_finder.utility, test_case)

if __name__ == '__main__':
    unittest.main()

        # Assert the result

    # Add more test methods for other functionalities as needed

if __name__ == '__main__':
    unittest.main()
