import pytest
from assertpy import assert_that

from src.arrays.max_number_of_points_with_cost import Solution


class TestSolution:
    @pytest.mark.parametrize(
        "matrix, expected",
        [
            ([[1, 2, 3]], 3),
            ([[1, 2, 3], [1, 5, 1], [3, 1, 1]], 9),
        ],
    )
    def test_solution(self, matrix, expected):
        result = Solution().maxPoints(matrix)
        assert_that(result).is_equal_to(expected)
