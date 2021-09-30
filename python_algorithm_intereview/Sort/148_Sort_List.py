# see answer 
"""
    Given the head of a linked list, return the list after sorting it in ascending order.
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
"""
# 두 정렬 리스트 병합
def sortList(head): #: Optional[ListNode] ->   -> Optional[ListNode] 
    # 연결 리스트 -> 파이썬 리스트
    p = head
    _list = list()
    while p :
        _list.append(p.val)
        p = p.next
    
    _list.sort()

    # 파이썬 리스트 -> 연결 리스트
    p = head
    for i in range(len(_list)):
        p.val = _list[i]
        p = p.next
    
    return head

"""
1. 병합 정렬
def mergeTwoLists(self, l1, l2):
    if l1 and l2:
        if l1.val > l2.val:
            l1, l2 = l2, l1
        l1.next = self.mergeTwoLists(l1.next, l2)
    return l1 or l2 

def sortList(head):
    if not (head and head.next):
        return head
    
    # 런너 기법 활용
    half, slow, fast = None, head, head
    while fast and fast.next:
        half, slow, fast = slow, slow.next, fast.next.next
    half.next = None # half 위치 기준으로 연결리스트 관계를 끊는다. 
    # [ ..., (half) / (slow),  ... , (fast)]
    # head = [..... , (half)] <- half.next = None
    # slow = [(slow), ..... ] 

    # 분할 재귀 호출
    l1 = self.sortList(head)
    l2 = self.sortList(slow)

    return self.mergeTwoLists(l1, l2)
"""


