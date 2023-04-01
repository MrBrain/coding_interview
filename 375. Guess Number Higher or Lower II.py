class Solution:
    def guessNumber(self, n: int) -> int:
        low=1
        high=n
        while low <= high:
            mid = (low+high) // 2
            if guess(mid) == 1:
                low = mid + 1
            else:
                high = mid - 1
        return low