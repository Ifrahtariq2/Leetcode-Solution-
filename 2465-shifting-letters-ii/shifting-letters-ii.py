class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift = [0] * (n + 1)  # Create a shift array of length n+1 to handle boundaries
        for shiftOp in shifts:
            start, end, direction = shiftOp
            shift[start] += (1 if direction == 1 else -1)
            if end + 1 < n:  # Ensure we don't go out of bounds
                shift[end + 1] -= (1 if direction == 1 else -1)

        currentShift = 0
        shiftList = list(s)  # Convert the string to a list for easy manipulation
        for i in range(n):
            currentShift += shift[i]
            netShift = (currentShift % 26 + 26) % 26  # Ensure netShift is always non-negative
            shiftList[i] = chr((ord(shiftList[i]) - ord('a') + netShift) % 26 + ord('a'))

        return ''.join(shiftList)  # Convert the list back to a string