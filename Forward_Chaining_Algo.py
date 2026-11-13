# Initial Knowledge Base
KB = [
    ("American", "Robert"),
    ("Enemy", "A", "America"),
    ("Owns", "A", "T1"),
    ("Missile", "T1")
]

# Rules
rules = [
    ([("Missile", "?x")],
     ("Weapon", "?x")),

    ([("Missile", "?x"), ("Owns", "A", "?x")],
     ("Sells", "Robert", "?x", "A")),

    ([("Enemy", "?x", "America")],
     ("Hostile", "?x")),

    ([("American", "?p"),
      ("Weapon", "?q"),
      ("Sells", "?p", "?q", "?r"),
      ("Hostile", "?r")],
     ("Criminal", "?p"))
]


# Display Rules
def display_rules():
    print("\n----- AVAILABLE RULES -----")

    for i, (conditions, conclusion) in enumerate(rules, 1):
        lhs = " AND ".join(
            f"{c[0]}({', '.join(c[1:])})"
            for c in conditions
        )
        rhs = f"{conclusion[0]}({', '.join(conclusion[1:])})"

        print(f"{i}. {lhs} -> {rhs}")


# Unification
def unify(pattern, fact, substitution):
    if pattern[0] != fact[0]:
        return None

    new_sub = substitution.copy()

    if len(pattern) != len(fact):
        return None

    for p, f in zip(pattern[1:], fact[1:]):
        if p.startswith("?"):
            if p in new_sub and new_sub[p] != f:
                return None
            new_sub[p] = f
        elif p != f:
            return None

    return new_sub


# Match conditions
def match_conditions(conditions, KB, substitution=None):
    if substitution is None:
        substitution = {}

    if not conditions:
        return [substitution]

    results = []

    for fact in KB:
        sub = unify(conditions[0], fact, substitution)

        if sub is not None:
            results.extend(
                match_conditions(conditions[1:], KB, sub)
            )

    return results


# Apply selected rule
def apply_rule(rule_no):
    conditions, conclusion = rules[rule_no - 1]

    substitutions = match_conditions(conditions, KB)
    new_facts = []

    for sub in substitutions:
        fact = tuple(sub.get(item, item) for item in conclusion)

        if fact not in KB and fact not in new_facts:
            new_facts.append(fact)

    if new_facts:
        KB.extend(new_facts)
        print("\nNew Facts Generated:")
        for fact in new_facts:
            print(fact)
    else:
        print("\nNo new facts generated. Rule conditions may not be satisfied.")


# Forward Chaining Menu
while True:
    display_rules()

    print("\n----- MENU -----")
    print("1. Apply Rule 1")
    print("2. Apply Rule 2")
    print("3. Apply Rule 3")
    print("4. Apply Rule 4")
    print("5. Display Knowledge Base")
    print("6. Apply All Rules (Forward Chaining)")
    print("7. Check Query")
    print("8. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice in [1, 2, 3, 4]:
        print(f"\nApplying Rule {choice}...")
        apply_rule(choice)

    elif choice == 5:
        print("\nCurrent Knowledge Base:")
        for fact in KB:
            print(fact)

    elif choice == 6:
        print("\nApplying Forward Chaining...")
        while True:
            old_size = len(KB)

            for i in range(1, 5):
                apply_rule(i)

            if len(KB) == old_size:
                break

        print("\nForward Chaining Completed.")

    elif choice == 7:
        query = ("Criminal", "Robert")

        if query in KB:
            print("\nResult: Robert is Criminal.")
        else:0

    else:
        print("\nInvalid Choice! Please enter 1 to 8.")
