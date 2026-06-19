class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places

        minimized_input = init

        for i in range (0,iterations):

            minimized_input = minimized_input - learning_rate*2*minimized_input

        return round(minimized_input,5)