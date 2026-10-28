import pytest
from assertpy import assert_that

from src.arrays.max_number_of_points_with_cost import Solution


class TestSolution:
    @pytest.mark.parametrize(
        "matrix, expected",
        [
            ([[1, 2, 3]], 3),
            ([[1, 2, 3], [1, 5, 1], [3, 1, 1]], 9),
            ([[1, 5], [2, 3], [4, 2]], 11),
            ([[9, 0, 10], [10, 0, 0]], 19),
        ],
        ids=[
            "simplest",
            "3by3",
            "3by2",
            "breaking_greedy",
        ],
    )
    def test_solution(self, matrix, expected):
        result = Solution().maxPoints(matrix)
        assert_that(result).is_equal_to(expected)
