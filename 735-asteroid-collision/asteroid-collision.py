class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for asteroid in asteroids:
            # This loop handles all collisions until one asteroid survives or they both destroy each other
            while stack and asteroid < 0 and stack[-1] > 0:
                if stack[-1] < abs(asteroid):
                    # The asteroid in the stack is smaller, so it gets destroyed
                    stack.pop()
                    continue  # We need to continue checking as the current asteroid may collide again
                elif stack[-1] == abs(asteroid):
                    # Both asteroids destroy each other
                    stack.pop()
                    break
                else:
                    # The asteroid in the stack is larger, the current one is destroyed
                    break
            else:
                # If no collision or the current asteroid survived, push it to the stack
                stack.append(asteroid)
        
        return stack


        