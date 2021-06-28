def solution(n):
    int_n = int(n)
    queue = [(int_n, 0)]
    best_steps = float('inf')
    visited = {}

    while len(queue) > 0:
        current_node = queue.pop(0)
        current_value = current_node[0]
        current_steps = current_node[1]

        if current_value in visited:
            continue

        visited[current_value] = True

        if current_value <= 1 and current_steps <= best_steps:
            best_steps = current_steps
            break

        if current_value % 2 == 0:
            divided = current_value / 2
            if not divided in visited:
                queue.append((divided, current_steps + 1))
        else:
            if not current_value + 1 in visited:
                queue.append((current_value + 1, current_steps + 1))

            if not current_value - 1 in visited:
                queue.append((current_value - 1, current_steps + 1))

    return best_steps



cases = [
    '2',
    '4',
    '6',  # 6 -> 3 -> 2 -> 1
    '13',  # 13 -> 12 -> 6 -> 3 -> 2 -> 1
    '14',  # 14 -> 7 -> 8 -> 4 -> 2 -> 1
    '15',
    '17', # 17 -> 16 -> 8 -> 4 -> 2 -> 1
    '90', # 90 -> 45 -> 44 -> 22 -> 11 -> 12 -> 6 -> 3 -> 2 -> 1
    '768',
    '549755813888',
    '9223372036854775708',
    '18923731619542357098500868790785326998466564056403945758400791312963993611579208923731619542357098500868790785326998466564056403945758400791312963993611579208923731619542357098500868790785326998466564056403945758400791312963993611579208923731619542357098500868790785326998466564056403945758400791312963993678'
]

for s in cases:
    print('{}: {}'.format(s, solution(s)))
