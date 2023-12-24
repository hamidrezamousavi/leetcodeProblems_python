class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
        if list1 is None:
          return list2
        if list2 is None:
          return list1
        if list1.val < list2.val:
          head = list1
          pointerl1 = list1.next
          pointerl2 = list2
        else:
            head = list2
            pointerl1 = list1
            pointerl2 = list2.next

        temp = head
        while pointerl1 and pointerl2:
            if pointerl1.val < pointerl2.val:
                temp.next = pointerl1
                temp = pointerl1
                pointerl1 = pointerl1.next
            else:
                temp.next = pointerl2
                temp = pointerl2
                pointerl2 = pointerl2.next
        match pointerl1, pointerl2:
          case None, None:
            return head
          case None, _:
            temp.next = pointerl2
            return head
          case _, None:
            temp.next = pointerl1
            return head

