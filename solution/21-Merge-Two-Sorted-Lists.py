

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1:ListNode, l2:ListNode)  -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        if l1.val < l2.val:
            output, l1 = l1, l1.next
        else:
            output, l2 = l2, l2.next

        cur = output
        while (l1 and l2):
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2

        return output


nodeA = ListNode(1)
nodeB = ListNode(2)
nodeC = ListNode(4)
nodeA.next = nodeB
nodeB.next = nodeC

nodeX = ListNode(1)
nodeY = ListNode(3)
nodeZ = ListNode(4)
nodeX.next = nodeY
nodeY.next = nodeZ


testing = Solution()
result1= testing.mergeTwoLists(nodeA,nodeX)
print(">>>", result1.val," ",result1.next.val," ",result1.next.next.val," ",result1.next.next.next.val)