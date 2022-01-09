class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = (0, 1)
        x, y = 0, 0
        for ins in instructions:
            if ins =='G':
                x, y = x + direction[0], y + direction[1]
            elif ins == 'L':
                direction = (-direction[1], direction[0])
            else:
                direction = (direction[1], -direction[0])

        return (x == 0 and y == 0) or direction != (0, 1)
    