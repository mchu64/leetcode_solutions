

class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        pos = [0, 0]
        direction = 0
        
        for x in instructions:
            if x == "G":
                if direction == 0:
                    pos[1] += 1
                elif direction == 1:  # East
                    pos[0] += 1
                elif direction == 2:  # South
                    pos[1] -= 1
                elif direction == 3:  # West
                    pos[0] -= 1
            else:
                if x == "L":
                    direction = (direction - 1) % 4  # Wrap left turn
                if x == "R":
                    direction = (direction + 1) % 4  # Wrap right turn

            
        if pos == [0,0]:
            return True
        if direction != 0:
            return True
        
        return False


        