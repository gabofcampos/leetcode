# You are given an m x n integer matrix points (0-indexed).
# Starting with 0 points, you want to maximize the number of points
#   you can get from the matrix.
#
# To gain points, you must pick one cell in each row.
# Picking the cell at coordinates (r, c) will add points[r][c] to your score.
#
# However, you will lose points if you pick a cell too far
#  from the cell that you picked in the previous row.
#  For every two adjacent rows r and r + 1 (where 0 <= r < m - 1),
#  picking cells at coordinates (r, c1) and (r + 1, c2)
#   will subtract abs(c1 - c2) from your score.
#
# Return the maximum number of points you can achieve.
#
# abs(x) is defined as:
#    x for x >= 0.
#   -x for x < 0.
class Solution:
    def max_points_greedy(self, points: list[list[int]]) -> int:
        """
        greedy approach:
            let's see if max points can be achieved when for each row
            we get the max points possible
            and reduce to the minimum the loses

        number of rows = n
        number of columns = m

        complexity?

        we loop over every row in the matrix,
            1. as n increases, we loop over more row → n
            2. max() scans over each element in a row → O(m) (grows as the number of cols does)
            3. points[row].index(gain) → O(m) (searches through m until finds idx wanted)
            4. abs() is direct so O(1)
            total cost per row = O(m) + O(m) + O(1) = O(2m) = O(m)
            total cost = n·O(m) = O(m·n)
        """
        max_points = 0
        for row in range(len(points)):
            gain = max(points[row])
            current_col = points[row].index(gain)
            if row == 0:
                max_points += gain
                prev_col = current_col
            else:
                lose = abs(prev_col - current_col)
                prev_col = current_col
                max_points += gain - lose

        return max_points

    def maxPoints(self, points: list[list[int]]) -> int:
        return self.max_points_greedy(points)
