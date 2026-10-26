import pytest
from assertpy import assert_that

from src.arrays.add_two_numbers import ListNode, Solution


def list_to_linked_list(values: list[int]) -> ListNode | None:
    if not values:
        return None
    else:
        sentinel = ListNode(values[0])
        current = sentinel
        for value in values[1:]:
            aux_node = ListNode(value)
            current.next = aux_node
            current = aux_node
        return sentinel


def linked_list_to_list(list_nodes: ListNode) -> list[int]:
    pass


class TestSolution:
    @pytest.mark.parametrize(
        "list1, list2, expected",
        [
            # ([0], [0], [0]),
            # ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ],
    )
    def test_solution(self, list1, list2, expected):
        result = Solution().addTwoNumbers(list1, list2)
        assert_that(result).is_equal_to(expected)
