import numpy as np
class MonkeyBananaProblem:
    def __init__(self):
        self.room_size = (5, 5)
        self.monkey_position = (0, 0)
        self.banana_position = (4, 4)
        self.box_position = (2, 2)
    def is_valid_move(self, new_position):
        x, y = new_position
        if x < 0 or x >= self.room_size[0] or y < 0 or y >= self.room_size[1]:
            return False
        return True
    def solve(self):
        queue = [(self.monkey_position, None)]
        while queue:
            current_position, action = queue.pop(0)
            if current_position == self.banana_position:
                return action
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                new_position = (current_position[0] + dx, current_position[1] + dy)
                if self.is_valid_move(new_position):
                    queue.append((new_position, "move"))
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                new_box_position = (self.box_position[0] + dx, self.box_position[1] + dy)
                new_position = (new_box_position[0], new_box_position[1])
                if self.is_valid_move(new_box_position) and new_position != self.monkey_position:
                    queue.append((new_position, "move box"))
        return None
problem = MonkeyBananaProblem()
solution = problem.solve()
if solution:
    print("Solution:")
    print(solution)
else:
    print("No solution found")
