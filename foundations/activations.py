import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        
        n = len(z)

        for i in range(0,n):

            z[i] = round(1/(1+np.exp(-z[i])),5)

        return z

        

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise

        n = len(z)

        for i in range(0,n):

            z[i] = max(0,z[i])

        return z
