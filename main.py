import math

class MathSolver:
    """
    Represents a simulated AI math solver with specific capabilities and cost.
    """
    def __init__(self, name, cost_per_query, max_complexity_level):
        self.name = name
        self.cost_per_query = cost_per_query
        # max_complexity_level: 1 for simple problems, 2 for complex problems
        self.max_complexity_level = max_complexity_level

    def can_solve(self, problem_complexity):
        """
        Checks if the solver can handle the given problem complexity.
        """
        return problem_complexity <= self.max_complexity_level

    def solve(self, problem_description):
        """
        Simulates solving the problem and returns a placeholder solution.
        """
        return f"[{self.name}] Solved '{problem_description}' with a simulated result."

def calculate_problem_complexity(problem_description):
    """
    A simple heuristic to estimate problem complexity based on keywords.
    1: Low complexity (basic arithmetic, simple linear equations)
    2: High complexity (derivatives, integrals, systems of equations, non-linear)
    """
    problem_description_lower = problem_description.lower()
    # Keywords indicating high complexity, requiring a more powerful model
    if any(keyword in problem_description_lower for keyword in ["derivative", "integral", "system", "solve for x and y", "non-linear"]):
        return 2
    # Keywords indicating low/medium complexity, suitable for a simpler model
    elif any(keyword in problem_description_lower for keyword in ["solve for x", "equation", "find x", "+", "-", "*", "/"]):
        return 1
    else:
        return 1 # Default to low complexity for anything else

def choose_and_solve(problem, budget):
    """
    Chooses the most cost-effective AI math solver based on problem complexity and available budget.
    """
    print(f"\n--- Problem: '{problem}' (Budget: ${budget:.2f}) ---")
    complexity = calculate_problem_complexity(problem)
    print(f"Calculated problem complexity: {complexity} ({'High' if complexity == 2 else 'Low'})")

    # Define our simulated AI models, representing Gemma 4 (low-cost) and Gemini 4 (high-power)
    # Gemma 4 equivalent: lower cost, lower capability (max_complexity_level=1)
    gemma_solver = MathSolver("Gemma 4 (Low-Cost)", cost_per_query=0.05, max_complexity_level=1)
    # Gemini 4 equivalent: higher cost, higher capability (max_complexity_level=2)
    gemini_solver = MathSolver("Gemini 4 (High-Power)", cost_per_query=0.50, max_complexity_level=2)

    # Decision logic: Prioritize the low-cost solver if it can handle the problem and fits the budget.
    if gemma_solver.can_solve(complexity) and budget >= gemma_solver.cost_per_query:
        print(f"Decision: {gemma_solver.name} can solve this low-complexity problem within budget.")
        solution = gemma_solver.solve(problem)
        remaining_budget = budget - gemma_solver.cost_per_query
        print(f"SUCCESS! {solution} Cost: ${gemma_solver.cost_per_query:.2f}")
        return solution, remaining_budget
    # If the low-cost solver can't handle it or is too expensive for its capability, try the high-power solver.
    elif gemini_solver.can_solve(complexity) and budget >= gemini_solver.cost_per_query:
        print(f"Decision: {gemini_solver.name} is required for this complexity and fits budget.")
        solution = gemini_solver.solve(problem)
        remaining_budget = budget - gemini_solver.cost_per_query
        print(f"SUCCESS! {solution} Cost: ${gemini_solver.cost_per_query:.2f}")
        return solution, remaining_budget
    else:
        print("Decision: FAILED to find a suitable solver within budget or capability constraints.")
        if not gemma_solver.can_solve(complexity) and not gemini_solver.can_solve(complexity):
             print("Reason: Neither solver can handle this problem's complexity.")
        elif budget < gemma_solver.cost_per_query and budget < gemini_solver.cost_per_query:
             print("Reason: Budget is too low for any available solver.")
        elif gemma_solver.can_solve(complexity) and budget < gemma_solver.cost_per_query:
             print(f"Reason: '{gemma_solver.name}' could solve it, but budget (${budget:.2f}) is less than its cost (${gemma_solver.cost_per_query:.2f}).")
        elif not gemma_solver.can_solve(complexity) and budget < gemini_solver.cost_per_query:
             print(f"Reason: '{gemini_solver.name}' could solve this high-complexity problem, but budget (${budget:.2f}) is less than its cost (${gemini_solver.cost_per_query:.2f}).")
        return None, budget

if __name__ == "__main__":
    initial_budget = 1.00 # Starting budget for demonstration

    problems_to_solve = [
        "What is 5 + 7?", # Low complexity, should use Gemma (cost: $0.05)
        "Solve for x: 3x - 9 = 0", # Low complexity, should use Gemma (cost: $0.05)
        "Find the derivative of x^3 + 2x", # High complexity, should use Gemini (cost: $0.50)
        "Solve the system: x+y=10, 2x-y=5", # High complexity, should use Gemini (cost: $0.50)
        "Calculate the integral of sin(x) from 0 to pi", # High complexity, should use Gemini (cost: $0.50)
        "What is 10 / 2?", # Low complexity, should use Gemma (cost: $0.05)
    ]

    current_budget = initial_budget
    print(f"--- Starting AI Math Solver Demo ---")
    print(f"Initial Total Budget: ${current_budget:.2f}")

    for i, problem in enumerate(problems_to_solve):
        if current_budget <= 0:
            print("\nBudget exhausted. Cannot process more problems.")
            break
        
        _, new_budget = choose_and_solve(problem, current_budget)
        current_budget = new_budget
        print(f"Current Total Budget remaining: ${current_budget:.2f}")

    print("\n--- Demo Finished ---")
