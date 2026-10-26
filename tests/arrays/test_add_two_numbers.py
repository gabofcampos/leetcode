import pytest
from assertpy import assert_that

from src.arrays.add_two_numbers import ListNode, Solution


def list_to_linked_list(values: list[int]) -> ListNode | None:
    if not values:
        return None
    else:
        sentinel = ListNode()
        current = sentinel
        for value in values:
            current.next = ListNode(value)
            current = current.next
        return sentinel.next


def linked_list_to_list(list_node: ListNode) -> list[int]:
    result = []
    while list_node:
        result.append(list_node.val)
        list_node = list_node.next
    return result


class TestSolution:
    @pytest.mark.parametrize(
        "list1, list2, expected",
        [
            ([0], [0], [0]),
            ([2, 4], [3, 1], [5, 5]),
            # ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ],
    )
    def test_solution(self, list1, list2, expected):
        result = Solution().addTwoNumbers(
            list_to_linked_list(list1),
            list_to_linked_list(list2),
        )
        assert_that(linked_list_to_list(result)).is_equal_to(expected)
