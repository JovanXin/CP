# Can also be modified to get max size of grids of only one type


class Solution:
    def solve(self, matrix):
        width = len(matrix)
        height = len(matrix[0])

        dp = [[0] * (height + 1) for _ in range(width + 1)]
        max_val = 0  # Keeping track of the greatest square size?

        for w in range(width):
            for h in range(height):
                if matrix[w][h] == 1:
                    dp[w + 1][h + 1] = (
                        min(dp[w + 1][h], dp[w][h + 1], dp[w][h]) + 1
                    )  # Check to see if square can be extended at all
                    max_val = max(
                        max_val, dp[w + 1][h + 1]
                    )  # Might be sketchy idk? Should be fine tho, just getting max value from matrix

        return max_val ** 2  # The area of the square with '1's
