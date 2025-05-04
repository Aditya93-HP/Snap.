import heapq
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
def h(state):
    return sum(1 for i in range(3) for j in range(3) if state[i][j] and state[i][j] != goal[i][j])
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
def to_tuple(state):
    return tuple(tuple(row) for row in state)
def a_star(start):
    q = [(h(start), 0, start, [])]
    seen = set()
    while q:
        f, g, state, path = heapq.heappop(q)
        if to_tuple(state) in seen:
            continue
        seen.add(to_tuple(state))
        if state == goal:
            return path + [state]
        x, y = find_zero(state)
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new = [row[:] for row in state]
                new[x][y], new[nx][ny] = new[nx][ny], new[x][y]
                heapq.heappush(q, (g + 1 + h(new), g + 1, new, path + [state]))
    return None
def input_state():
    print("Enter 3 rows (use 0 for blank):")
    return [list(map(int, input().split())) for _ in range(3)]
def print_path(path):
    for i, state in enumerate(path):
        print(f"Step {i}:")
        for row in state:
            print(row)
        print()
initial = input_state()
solution = a_star(initial)
print_path(solution) if solution else print("No solution found.")
'''INPUT
Enter 3 rows (use 0 for blank):
1 2 3
0 4 6
7 5 8
'''
'''OUTPUT
Step 0:
[1, 2, 3]
[0, 4, 6]
[7, 5, 8]

Step 1:
[1, 2, 3]
[4, 0, 6]
[7, 5, 8]

Step 2:
[1, 2, 3]
[4, 5, 6]
[7, 0, 8]

Step 3:
[1, 2, 3]
[4, 5, 6]
[7, 8, 0]
'''
