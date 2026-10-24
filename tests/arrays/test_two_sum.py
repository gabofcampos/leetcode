import pytest
from assertpy import assert_that

from src.arrays.two_sum import Solution


class TestSolution:
    @pytest.mark.parametrize(
        "input, target, expected",
        [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
        ],
    )
    def test_two_sum(self, input, target, expected):
        result = Solution().two_sum(input, target)

        assert_that(sorted(expected)).is_equal_to(sorted(result))
