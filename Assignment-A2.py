import heapq

class Puzzle:
    def __init__(self, board, move="", depth=0, prev=None):
        self.b = board; self.m = move; self.d = depth; self.p = prev
        self.z = board.index(0)
        self.cost = self.d + self.h()

    def h(self):  # Manhattan distance
        goal = [1,2,3,4,5,6,7,8,0]
        return sum(abs((i%3)-(goal.index(self.b[i])%3)) + abs((i//3)-(goal.index(self.b[i])//3)) for i in range(9) if self.b[i] != 0)

    def neighbors(self):
        moves = [(-1,0,"Up"), (1,0,"Down"), (0,-1,"Left"), (0,1,"Right")]
        x, y = self.z % 3, self.z // 3
        for dx, dy, action in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                ni = ny * 3 + nx
                new_b = self.b[:]; new_b[self.z], new_b[ni] = new_b[ni], new_b[self.z]
                yield Puzzle(new_b, action, self.d + 1, self)

    def path(self):
        node, path = self, []
        while node.p:
            path.append(node.m); node = node.p
        return path[::-1]

    def __lt__(a, b): return a.cost < b.cost
    def is_goal(self): return self.b == [1,2,3,4,5,6,7,8,0]

def solve(start):
    start = Puzzle(start); seen = set(); q = [start]
    while q:
        curr = heapq.heappop(q)
        if tuple(curr.b) in seen: continue
        seen.add(tuple(curr.b))
        if curr.is_goal(): return curr.path()
        for n in curr.neighbors():
            if tuple(n.b) not in seen: heapq.heappush(q, n)
    return None
'''start = [1, 2, 3,
         4, 0, 6,
         7, 5, 8]

steps = solve(start)
print("Steps to solve:", steps)
'''
'''Steps to solve: ['Down', 'Right']
'''