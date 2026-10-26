import pytest
from assertpy import assert_that

from src.arrays.add_two_numbers import Solution


class TestSolution:
    @pytest.mark.parametrize(
        "expected",
        [
            None,
        ],
    )
    def test_solution(self, expected):
        result = Solution().addTwoNumbers(None, None)
        assert_that(result).is_equal_to(expected)
