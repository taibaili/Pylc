from util.ListNode import ListNode

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        runner = head.next
        while runner.next is not None and runner.next.next is not None:
            if head == runner:
                return True
            head = head.next
            runner = runner.next.next
        return False

if __name__ == '__main__':
    solution = Solution

    # head0 = ListNode(0)
    # head0.next = head1 = ListNode(1)
    # head0.next.next = head2 = ListNode(2)
    # head0.next.next.next = head3 = ListNode(3)
    # head3.next = head1
    # print(solution.hasCycle(solution,head0))

    new_head0 = ListNode(1)
    # new_head0.next = new_head1 = ListNode(2)
    print(solution.hasCycle(solution,new_head0))
