import pytest
from assertpy import assert_that

from src.arrays.max_number_of_points_with_cost import Solution


class TestSolution:
    @pytest.mark.parametrize(
        "matrix, expected",
        [
            ([[1, 2, 3]], 3),
        ],
    )
    def test_solution(self, matrix, expected):
        result = Solution().maxPoints(matrix)
        assert_that(result).is_equal_to(expected)
