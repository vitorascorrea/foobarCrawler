from fractions import Fraction, gcd


def find_lcm(denominator_list):
    lcm = 1

    for i in denominator_list:
        lcm = lcm * i // gcd(lcm, i)

    return lcm


def normalize_matrix(m):
    matrix = []

    for row in m:
        row_sum = sum(row)
        norm_row = []
        for col in row:
            if row_sum > 0:
                # norm_row.append(Fraction(col, row_sum))
                norm_row.append(float(col) / float(row_sum))
            else:
                norm_row.append(0)
        matrix.append(norm_row)

    return matrix


def dot(m1, m2):
    return [
        [sum(x * y for x, y in zip(m1_r, m2_c)) for m2_c in zip(*m2)] for m1_r in m1
    ]


def solution(m):
    matrix = normalize_matrix(m)
    terminal_states = [i for i, row in enumerate(m) if sum(row) == 0]

    # s0 is a terminal state, what to do?
    if terminal_states[0] == 0:
        return [1, 1]

    states = [[0] for _ in range(len(m))]
    states[0][0] = 1
    state_acc = [0 for _ in range(len(m))]

    for _ in range(1000):
        states = dot(states, matrix)
        state_acc = [state_acc[i] + states[0][i] for i in range(len(states))]


    fractions = []
    for terminal_state in terminal_states:
        node_prob = state_acc[terminal_state]
        numerator, denominator = float(node_prob).as_integer_ratio()
        fractions.append(Fraction(numerator, denominator).limit_denominator())

    least_common_multiple = find_lcm([i.denominator for i in fractions])

    probabilities = [int(fraction.numerator * (float(least_common_multiple) / float(fraction.denominator))) for fraction in fractions]
    probabilities.append(int(least_common_multiple))

    return probabilities


print(
    solution([
        [0, 2, 1, 0, 0],
        [0, 0, 0, 3, 4],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ])
)

print(
    solution([
        [0, 1, 0, 0, 0, 1],  # s0, the initial state, goes to s1 and s5 with equal probability
        [4, 0, 0, 3, 2, 0],  # s1 can become s0, s3, or s4, but with different probabilities
        [0, 0, 0, 0, 0, 0],  # s2 is terminal, and unreachable (never observed in practice)
        [0, 0, 0, 0, 0, 0],  # s3 is terminal
        [0, 0, 0, 0, 0, 0],  # s4 is terminal
        [0, 0, 0, 0, 0, 0],  # s5 is terminal
    ])
)
