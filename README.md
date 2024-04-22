# Budget-Optimizer
Budget Optimizer // CS313E
Members: Minji & Jawad

**Project Description:**

The project is about understanding how people make decisions when they have a limited budget and need to buy two different things. We'll use a simple example to show how someone might decide how much of each thing to buy to get the most satisfaction (or utility) from their money. We'll draw two graphs: one that shows how much satisfaction they get from buying different amounts of each thing (called the utility function), and another that shows the various combinations of things they can buy with their budget (called the budget constraint). By looking at where these two graphs intersect, we can determine the best combination of things to buy that gives them the most satisfaction within their budget.

**Idea Statement:**

The project utilizes principles from microeconomics and mathematical optimization to determine the optimal allocation of resources for a rational consumer facing budget constraints. It employs Python programming to graphically represent the utility function, budget constraint, and tangency point, providing insights into consumer behavior and decision-making.

**No dataset used**

**Algorithm: Decision Tree**: A hierarchical structure guides user interactions, enabling dynamic adjustments to inputs and visualization of results.

**Data Structures:** Dictionary & Lists


### **Code Description:**

- **Graph Class**:
    - **Responsibility**: Plotting budget lines, tangency points, and utility contours.
    - **Dependencies**: Matplotlib and NumPy.
- **BudgetFinder Class**:
    - **Responsibility**: Determines optimal quantities of goods based on utility functions and budget constraints.
    - **Dependencies**: SymPy for symbolic math operations.
- **DecisionNode Class**:
    - **Responsibility**: Forms the decision tree structure for user interaction.
 

## **Libraries Used**

**1. Matplotlib:**

Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. It is widely used for generating plots, histograms, power spectra, bar charts, error charts, and scatterplots.

*What is it used for in this project?*
For graphing various economic concepts, such as budget lines, utility functions, tangency points, and utility contours. 

**2. SymPy:**

SymPy is a Python library for symbolic mathematics. It aims to become a full-featured computer algebra system (CAS) while keeping the code as simple as possible in order to be comprehensible and easily extensible. SymPy provides functions for symbolic computation, including algebraic manipulation, calculus, equation solving, and more.

*What is it used for in this project?*
For symbolic math operations, particularly in solving optimization problems related to utility maximization subject to budget constraints. It helps find the optimal quantities of goods by performing symbolic calculations.

**3. NumPy:**

NumPy is a fundamental package for scientific computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays.

*What is it used for in this project?*
For numerical operations required for graphing and optimization. It helps in creating arrays to represent different variables, performing mathematical operations on these arrays, and facilitating data manipulation tasks. 

### **Graph Class**

**Purpose:** Represents a graph for visualizing utility functions, budget lines, and tangency points

**Functions:**

- *init:* Initializes the Graph object with data points for x and y axes, budget line points, and utility function.

- *draw functions:* Draws the utility function, budget line, and tangency point on the graph using Matplotlib.

- *plot tangency point:* Plots the tangency point on the graph.

### **Budget Finder Class**

**Purpose:** Finds the optimal allocation of goods within the budget constraint and manages utility functions.

**Functions:**

- *init:* Initializes the BudgetFinder object with default or user-defined parameters.

- *find optimal mrs:* Finds the optimal Marginal Rate of Substitution (MRS) by solving equations for the tangency point.

- *budget line points:* Determines the points along the budget line based on prices and total budget.

- *modify price one:* Modifies the price of the first good and updates the budget line points accordingly.

- *modify price two:* Modifies the price of the second good and updates the budget line points accordingly.

- *modify total:* Modifies the total budget and updates the budget line points accordingly.

- *modify utility:* Modifies the utility function and updates the budget line points accordingly.

- *graph it:* Creates a graph with the utility function, budget line, and tangency point using the Graph class.

## **DecisionNode Class:**

**Purpose:** Represents a decision node in a decision tree for user interaction.
Functions:

**Functions:**

- *init:* Initializes the DecisionNode object with a label, list of choices, and associated action.

- *print label:* Prints the label of the decision node

- *print choices:* Prints the choices available for the decision node.

### **build_decision_tree():**

**Purpose:** Constructs a decision tree with decision nodes for modifying prices, utility function, total amount of money, showing graphs, and finding optimal solutions.


### **interact_with_user():**

**Purpose:**  Interacts with the user by presenting choices and performing actions based on user input, using the provided decision tree and budget object.

### **starter():**

**Purpose:** Initializes the BudgetFinder object with user-defined parameters for prices, total budget, and utility function.

- **Steps**:
    1. **Input Prices**: Prompts the user to input the prices of goods one and two.
    2. **Input Total Budget**: Prompts the user to input the total budget available.
    3. **Input Utility Function**: Prompts the user to input the utility function parameters.
    4. **Create BudgetFinder Object**: Initializes a BudgetFinder object with the inputted parameters.
    5. **Return BudgetFinder Object**: Returns the initialized BudgetFinder object for further interaction.

The **`starter()`** function serves as the entry point for initializing the BudgetFinder object with user-provided inputs, setting the stage for subsequent interactions and optimizations within the interactive tool.

### **main():**

**Purpose:**

Initializes the decision tree and budget object, then starts the interaction with the user.

## **Inputs & Outputs:**

**Inputs**

1. *Price of Good One (price_one)*: The price of the first good, inputted by the user.
2. *Price of Good Two (price_two)*: The price of the second good, inputted by the user.
3. *Total Amount of Money (total_money)*: The total budget available to the consumer, inputted by the user.
4. *Utility Function (utility)*: The utility function representing the preferences of the consumer, inputted by the user.

**Outputs**

1. *Optimal Quantities of Goods (x1, x2)*: The optimal quantities of goods one and two that maximize utility subject to the budget constraint.
2. *Graphical Representation*:

    - **Budget Line**: Visual representation of the budget constraint.

    - **Tangency Point**: Graphical depiction of the optimal consumption bundle where the budget line is tangent to the utility function.

    - **Utility Contours**: Contour plot representing different levels of utility.





