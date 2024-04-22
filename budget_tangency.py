"""budget_tangency"""
import matplotlib.pyplot as plt
import sympy as sp
import numpy as np

class Graph():

    """graphs the functions"""
    def __init__(self, x, y, budget_line_points, utility):
        self.x = x
        self.y = y
        self.budget_line_points = budget_line_points
        self.utility = utility

    def draw_functions(self):
        """draws the functions on the graph"""
        # Plot budget line
        plt.plot([point[0] for point in self.budget_line_points],
                [point[1] for point in self.budget_line_points],
                label="Budget Line", color='blue')

        # Plot tangency point
        plt.plot(self.x, self.y, 'ro', label="Tangency Point")

        # Evaluate utility function for a range of x1 and x2 values
        x1_values = np.linspace(0, 10, 100)
        x2_values = np.linspace(0, 10, 100)

        # Calculate utility values for each combination of x1 and x2
        utility_values = np.outer(x2_values, x1_values)  # Outer product of x2 and x1

        # Plot utility function using a contour plot
        plt.contour(x1_values, x2_values, utility_values, levels=20, cmap='RdGy', alpha=0.5)

        # Label axes
        plt.xlabel("Quantity of Good 1")
        plt.ylabel("Quantity of Good 2")

        # Add legend
        plt.legend()

        # Show plot
        plt.show()

    def plot_tangency_point(self):
        """plots the tangency point"""
        plt.plot(self.x, self.y)


class BudgetFinder():
    """finds the optimal amount of each good, and the function of the budget"""
    def __init__(self, utility=0, price_one=0, price_two=0, total_money=0):
        self.utility = utility
        self.price_one = price_one
        self.price_two = price_two
        self.total_money = total_money
        self.budget_points = 0
        self.utility_quantities = {}



    def find_optimal_mrs(self):
        """finds the optimal MRS function"""
        # Define symbols
        x1 = sp.Symbol('x1')
        x2 = sp.Symbol('x2')

        # Calculate the MRS (Marginal Rate of Substitution)
        mrs = sp.diff(self.utility, x1) / sp.diff(self.utility, x2)
        # Set up equation: MRS = price_one / price_two
        equation = sp.Eq(mrs, self.price_one/self.price_two)

        budget_equation = sp.Eq(x2, self.total_money/self.price_two - \
                                self.price_one/self.price_two*x1)
        # Solve the equation
        sol = sp.solve([equation, budget_equation], (x1, x2))

        return sol

    def budget_line_points(self):
        "finds the points along the budget_line"
        slope = (self.price_one/self.price_two)*-1
        y_intercept = self.total_money/self.price_two
        good_one = range(0, int(self.total_money / self.price_one) + 1)

        budget_line_points = [(x1, slope * x1 + y_intercept) for x1 in good_one]

        return budget_line_points


    def modify_price_one(self, new_price):
        """modifies price one"""
        self.price_one = new_price
        if self.price_two != 0:
            self.budget_points = self.budget_line_points()


    def modify_price_two(self, new_price):
        """modifies price two"""
        self.price_two = new_price
        if self.price_one != 0:
            self.budget_points = self.budget_line_points()

    def modify_total(self, new_total):
        """modifies total"""
        self.total_money = new_total
        self.budget_points = self.budget_line_points()


    def modify_utility(self, new_utility):
        """Modifies utility function"""
        try:
            self.utility = sp.sympify(new_utility)
            self.budget_points = self.budget_line_points()
        except sp.SympifyError as e:
            print("Error: Invalid utility function:", e)


    def graph_it(self):
        """creates the graph with both functions and tangency point"""
        ans = self.find_optimal_mrs()
        x = ans[sp.Symbol('x1')]
        y = ans[sp.Symbol('x2')]

        graph = Graph(x, y, self.budget_points, self.utility)
        graph.draw_functions()
        graph.plot_tangency_point()


class DecisionNode:
    """creates the node"""
    def __init__(self, label, choices=None, action=None):
        self.label = label  # Label or description of the decision
        self.choices = choices or []  # List of possible choices (child nodes)
        self.action = action  # Action associated with the decision (e.g., modify price, utility
        #function)
    def print_label(self):
        """print label"""
        print (self.label)

    def print_choices(self):
        """print choices"""
        print (self.choices)

def build_decision_tree():
    """builds a decision tree"""
    # Define decision nodes
    root = DecisionNode("Root")
    price_one_node = DecisionNode("Change price of good one", action = "modify_price_one")
    price_two_node = DecisionNode("Change price of good two", action = "modify_price_two")
    utility_node = DecisionNode("Change utility function", action = "modify_utility")
    total_node = DecisionNode("Change total amount of money", action = "modify_total")
    show_node = DecisionNode("Show graph", action = "graph_it")
    optimal_node = DecisionNode("Find optimal solution", action = "find_optimal_mrs")

    # Connect nodes to form tree structure
    root.choices = [price_one_node, price_two_node, utility_node, total_node, show_node,
                        optimal_node]

    return root
def interact_with_user(decision_tree, user_budget):
    """interacts with user"""
    current_node = decision_tree
    while True:
        print("Current Decision:", current_node.label)
        print("Available Choices:")
        for idx, choice in enumerate(current_node.choices, start=1):
            print(f"{idx}. {choice.label}")

        choice_idx = input(f"Enter your choice (1-{len(current_node.choices)}) or 'q' to quit: ")
        if choice_idx.lower() == 'q':
            break
        if choice_idx.isdigit():
            choice_idx = int(choice_idx)
            if 1 <= choice_idx <= len(current_node.choices):
                chosen_node = current_node.choices[choice_idx - 1]
                if chosen_node.action == "modify_utility":
                    new_info = input("input what you would like to change utility to")
                    # Perform action associated with the chosen node
                    getattr(user_budget, chosen_node.action)(new_info)
                elif chosen_node.action == "find_optimal_mrs":
                    print(user_budget.find_optimal_mrs())
                elif chosen_node.action == "graph_it":
                    user_budget.graph_it()
                elif chosen_node.action:
                    new_info = input("input what you would like to change it to")
                    # Perform action associated with the chosen node
                    getattr(user_budget, chosen_node.action)(float(new_info))
                current_node = chosen_node
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Invalid input. Please enter a number or 'q' to quit.")
        current_node = decision_tree


def helper():
    """prints the commands available"""
    print("Enter 'help' to repeat the commands")
    print("Enter 'quit' to exit")
    print("Enter 'price one' to change the value of the first good")
    print("Enter 'price two' to change the value of the second good")
    print("Enter 'total' to change the total amount of money available")
    print("Enter 'utility' to change the utility function")
    print("For utility function enter using terms x1 and x2")
    print()
    print("NOTE THIS PROGRAM ONLY WORKS ACCURATELY WITH COBB DOUGLASS UTILITY FUNCTIONS")
    print("So that means, x1 and x2 should be multiplied by each other, not added")
    print()
    print("Enter 'show' to show the graph")
    print("Enter 'optimal' to find the optimal amount of good one and two")

def starter():
    """always requires that they input everything first"""
    user_budget = BudgetFinder()

    price = float(input("How much is good one priced at?"))
    user_budget.modify_price_one(price)
    price = float(input("How much is good two priced at?"))
    user_budget.modify_price_two(price)
    total = float(input("What is the total amount of money available?"))
    user_budget.modify_total(total)
    utility = input("What is the utility function?")
    user_budget.modify_utility(utility)

    return user_budget


def main():
    """main"""
    # Initialize decision tree

    decision_tree = build_decision_tree()

    # Initialize BudgetFinder
    user_budget = starter()

    # Start interaction with user
    interact_with_user(decision_tree, user_budget)

if __name__ == "__main__":
    main()
