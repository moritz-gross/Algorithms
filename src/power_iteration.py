import numpy as np
from numpy.linalg import norm

def power_iteration(A, num_iterations: int):
    tmp = np.random.rand(A.shape[1])

    for _ in range(num_iterations):
        tmp = np.dot(A, tmp) / norm(np.dot(A, tmp))

    return tmp

if __name__ == '__main__':

    result = power_iteration(
        np.array([
            [0.5, 0.5],
            [0.2, 0.8]
        ]),
        100
    )
    print(result)