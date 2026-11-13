# Forward Chaining Algorithm(ASHISH KUMAR SINHA - 1WA24CS064)

KB = [
    ("American", "Robert"),
    ("Enemy", "A", "America"),
    ("Owns", "A", "T1"),
    ("Missile", "T1")
]


rules = [
    # Missile(x) -> Weapon(x)
    ([("Missile", "?x")], ("Weapon", "?x")),

    # Missile(x) AND Owns(A,x) -> Sells(Robert,x,A)
    ([("Missile", "?x"), ("Owns", "A", "?x")],
     ("Sells", "Robert", "?x", "A")),

    # Enemy(x,America) -> Hostile(x)
    ([("Enemy", "?x", "America")], ("Hostile", "?x")),

    # American(p) AND Weapon(q) AND Sells(p,q,r)
    # AND Hostile(r) -> Criminal(p)
    ([("American", "?p"),
      ("Weapon", "?q"),
      ("Sells", "?p", "?q", "?r"),
      ("Hostile", "?r")],
     ("Criminal", "?p"))
]


def unify(pattern, fact, substitution):
    if pattern[0] != fact[0]:
        return None

    new_sub = substitution.copy()

    for p, f in zip(pattern[1:], fact[1:]):
        if p.startswith("?"):
            if p in new_sub and new_sub[p] != f:
                return None
            new_sub[p] = f
        elif p != f:
            return None

    return new_sub


def match_conditions(conditions, KB, substitution=None):
    if substitution is None:
        substitution = {}

    if not conditions:
        return [substitution]

    first = conditions[0]
    remaining = conditions[1:]
    results = []

    for fact in KB:
        sub = unify(first, fact, substitution)

        if sub is not None:
            results.extend(
                match_conditions(remaining, KB, sub)
            )

    return results



def forward_chaining(KB, query):
    while True:
        new_facts = []

        for conditions, conclusion in rules:
            substitutions = match_conditions(conditions, KB)

            for sub in substitutions:
                fact = tuple(
                    sub.get(item, item)
                    for item in conclusion
                )

                if fact not in KB and fact not in new_facts:
                    new_facts.append(fact)

        if not new_facts:
            break

        KB.extend(new_facts)

        print("New Facts:", new_facts)

        if query in KB:
            return True

    return query in KB



query = ("Criminal", "Robert")

if forward_chaining(KB, query):
    print("\nResult: Robert is Criminal.")
else:
    print("\nResult: Robert is NOT Criminal.")
