'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    number1 = traverse(l1)
    number2 = traverse(l2)
    new_number = int(number1) + int(number2)
    resultNode = number_to_linked_list(new_number)
    return resultNode


def number_to_linked_list(number):
    number_string = number
    last_node = ListNode(0)
    for index, n in enumerate(str(number_string)):
        if index != 0:
            node = ListNode(n)
            node.next = prev_node
        else:
            node = ListNode(n)
        if index == len(str(number_string)) - 1:
            last_node.val = n
            if (len(str(number_string))) != 1:
                last_node.next = prev_node
        prev_node = node
    return last_node


def traverse(node):
    numbers = []
    n = node
    while n is not None:
        numbers.append(n.val)
        n = n.next

    numbers.reverse()
    number_string = ''
    for number in numbers:
        number_string = number_string + str(number)
    return number_string


l1 = ListNode(0)
l2 = ListNode(4)
l3 = ListNode(3)

l1.next = l2
l2.next = l3

l11 = ListNode(5)
l22 = ListNode(6)
l33 = ListNode(4)
l11.next = l22
l22.next = l33

result = addTwoNumbers(l1, l11)
print(result)