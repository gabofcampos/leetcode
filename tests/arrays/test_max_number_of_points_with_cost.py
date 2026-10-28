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
            (
                [
                    [0, 9, 6, 7, 0, 5, 4, 6, 6],
                    [8, 8, 9, 3, 7, 3, 4, 6, 7],
                    [0, 6, 5, 10, 10, 6, 2, 7, 2],
                    [9, 8, 0, 6, 9, 9, 10, 0, 1],
                    [10, 6, 2, 7, 2, 0, 4, 6, 5],
                    [3, 7, 5, 5, 6, 4, 6, 4, 1],
                    [7, 0, 8, 0, 5, 3, 10, 1, 10],
                    [0, 0, 3, 3, 0, 9, 2, 3, 2],
                ],
                61,
            ),
        ],
        ids=[
            "simplest",
            "3by3",
            "3by2",
            "breaking_greedy",
            "limit_exceeded",
        ],
    )
    def test_solution(self, matrix, expected):
        result = Solution().maxPoints(matrix)
        assert_that(result).is_equal_to(expected)
