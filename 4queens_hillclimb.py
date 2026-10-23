def cost(x):
    h = 0
    for i in range(4):
        for j in range(i + 1, 4):
            if x[i] == x[j] or abs(x[i] - x[j]) == abs(i - j):
                h += 1
    return h

def display_state(x):
    print("(" + ", ".join(map(str, x)) + ")", end="")

def main():
    x = [3, 1, 2, 0]
    step = 0

    while True:
        print(f"\nStep {step}\nCurrent state: ", end="")
        display_state(x)

        current_cost = cost(x)
        print(f"\nCurrent cost: {current_cost}")

        if current_cost == 0:
            print("Goal state reached!")
            break

        best = list(x)
        best_cost = float('inf')
        bi, bj = -1, -1

        for i in range(4):
            for j in range(i + 1, 4):
                next_state = list(x)
                next_state[i], next_state[j] = next_state[j], next_state[i]

                c = cost(next_state)

                print(f"Swap ({i},{j}): ", end="")
                display_state(next_state)
                print(f" Cost = {c}")

                if c < best_cost:
                    best_cost = c
                    best = next_state
                    bi, bj = i, j

        if best_cost >= current_cost:
            print("No better neighbor. Stopped.")
            break

        print(f"Selected swap: ({bi},{bj})")
        x = best
        step += 1

    print("\nFinal board:")
    for r in range(4):
        for c in range(4):
            if x[c] == r:
                print("Q ", end="")
            else:
                print(". ", end="")
        print()

main()s