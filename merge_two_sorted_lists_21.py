from util.ListNode import ListNode

class merge_two_sorted_list_21:
    # iteration
    def mergeTwoLists(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

    #recursion
    def merge_two_list_recursion(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.merge_two_list_recursion(self, l1.next, l2)
            return l1
        else:
            l2.next = self.merge_two_list_recursion(self, l1, l2.next)
            return l2

if __name__ == '__main__':
    solution = merge_two_sorted_list_21
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(3)

    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)

    # print(solution.mergeTwoLists(solution,list1,list2).val)
    print(solution.merge_two_list_recursion(solution, list1, list2).val)

