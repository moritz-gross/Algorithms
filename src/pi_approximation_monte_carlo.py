import random

def monte_carlo_pi(num_samples: int) -> float:
    counter = 0
    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        if x*x + y*y <= 1: # check if inside circle
            counter += 1

    return 4 * counter / num_samples # rescale from π/4

if __name__ == '__main__':
    # Number of random points
    pi_estimate = monte_carlo_pi(1000000)
    print("Monte Carlo estimate of π:", pi_estimate)