import random
import math

def calculate_cost(state):
    """Count pairs of queens attacking each other."""
    conflicts = 0
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            if (state[i] == state[j] or
                abs(state[i] - state[j]) == abs(i - j)):
                conflicts += 1

    return conflicts


def random_neighbor(state):
    """Create a neighbor by swapping two queens."""
    neighbor = state[:]
    i, j = random.sample(range(len(state)), 2)
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
    return neighbor, i, j


def simulated_annealing(initial_state):
    current = initial_state[:]
    temperature = 10.0
    cooling_rate = 0.95
    step = 0

    print("Initial state:", current)
    print("Initial cost:", calculate_cost(current))

    while temperature > 0.01:
        if calculate_cost(current) == 0:
            break

        next_state, i, j = random_neighbor(current)

        current_cost = calculate_cost(current)
        next_cost = calculate_cost(next_state)

        delta_E = current_cost - next_cost

        # Decide whether to accept the next state
        if delta_E > 0:
            accept = True
            probability = 1.0
        else:
            probability = math.exp(delta_E / temperature)
            accept = random.random() < probability

        print(f"\nStep {step + 1}")
        print("Temperature:", round(temperature, 4))
        print("Current state:", current)
        print("Current cost:", current_cost)
        print(f"Random swap: (x{i}, x{j})")
        print("Next state:", next_state)
        print("Next cost:", next_cost)
        print("Delta E:", delta_E)
        print("Acceptance probability:", round(probability, 4))

        if accept:
            current = next_state
            print("Decision: ACCEPT")
        else:
            print("Decision: REJECT")

        print("State after decision:", current)
        print("Cost after decision:", calculate_cost(current))

        temperature *= cooling_rate
        step += 1

    print("\nFinal state:", current)
    print("Final cost:", calculate_cost(current))

    if calculate_cost(current) == 0:
        print("Goal state reached!")
    else:
        print("Temperature ended before reaching the goal.")

    return current



random.seed(42)  
initial_state = [3, 1, 2, 0]

simulated_annealing(initial_state)

