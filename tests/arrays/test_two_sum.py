from assertpy import assert_that

from src.arrays.two_sum import Solution


class TestSolution:
    def test_two_sum(self):
        input = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]

        result = Solution().two_sum(input, target)

        assert_that(expected).is_equal_to(result)
