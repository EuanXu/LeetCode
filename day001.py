"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：LMOsqabou2/t
    输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
    输出：7 -> 0 -> 8
    原因：342 + 465 = 807
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0);
        resTemp = res
        flag = 0
        nextSum = 0
        while l1 != None and l2 != None:
            if flag == 0:
                p = l1.val + l2.val
                res.val = p % 10
                nextSum = int(p / 10)
                flag += 1
            else:
                p = l1.val + l2.val + nextSum
                resTemp.next = ListNode(p%10)
                resTemp = resTemp.next
                nextSum = int(p / 10)
            l1 = l1.next
            l2 = l2.next
        while l1:
            p = l1.val + nextSum
            resTemp.next = ListNode(p%10)
            resTemp = resTemp.next
            nextSum = int(p / 10)
            l1 = l1.next
        while l2:
            p = l2.val + nextSum
            resTemp.next = ListNode(p%10)
            resTemp = resTemp.next
            nextSum = int(p / 10)
            l2 = l2.next
        if nextSum != 0:
            resTemp.next = ListNode(1)
        return res