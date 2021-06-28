def solution(l):
    count = 0
    l_len = len(l)

    if l_len < 3:
        return 0

    graph = {i: [
        l[i],
        list(filter(lambda j: l[j] % l[i] == 0, range(i + 1, l_len)))
    ] for i in range(l_len)}

    for key in graph:
        node = graph[key]
        for mul in node[1]:
            mul_node = graph[mul]
            count += len(mul_node[1])

    return count

print(solution([1, 1, 2, 5]))
print(solution([1, 1, 1]))
print(solution([1, 2, 3, 4, 5, 6]))
print(solution([2, 4, 8, 16, 32, 64]))
print(solution([1, 5, 7]))
print(solution([3, 3, 3, 3]))
print(solution([1, 1, 3, 5]))
