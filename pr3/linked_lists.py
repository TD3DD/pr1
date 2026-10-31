class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ==========================================
# 1. Об’єднати два відсортовані списки
# ==========================================
def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode()
    tail = dummy
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    
    tail.next = list1 if list1 else list2
    return dummy.next

# ==========================================
# 2. Видалити дублікати з відсортованого списку
# ==========================================
def deleteDuplicates(head: ListNode) -> ListNode:
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head

# ==========================================
# 3. Цикл пов’язаного списку
# ==========================================
def hasCycle(head: ListNode) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# ==========================================
# 4. Перевпорядкувати список
# ==========================================
def reorderList(head: ListNode) -> None:
    if not head or not head.next:
        return
    
    # 1. Знайти середину списку
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    # 2. Перевернути другу половину списку
    prev, curr = None, slow.next
    slow.next = None
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        
    # 3. З'єднати дві половини
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2

# ==========================================
# 5. Видалити вузол у зв’язаному списку
# ==========================================
def deleteNode(node: ListNode) -> None:
    """
    Модифікує вузол на місці, копіюючи значення наступного 
    і видаляючи наступний вузол.
    """
    node.val = node.next.val
    node.next = node.next.next

# ==========================================
# 6. Подвоїти число, представлене у вигляді зв’язаного списку
# ==========================================
def doubleIt(head: ListNode) -> ListNode:
    # Допоміжна функція для перевертання списку
    def reverse(node: ListNode) -> ListNode:
        prev, curr = None, node
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    head = reverse(head)
    
    curr = head
    carry = 0
    prev = None
    
    while curr:
        val = curr.val * 2 + carry
        curr.val = val % 10
        carry = val // 10
        prev = curr
        curr = curr.next
        
    if carry:
        prev.next = ListNode(carry)
        
    return reverse(head)

# ==========================================
# 7. Об’єднати k відсортованих списків
# ==========================================
def mergeKLists(lists: list[ListNode]) -> ListNode:
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]
        
    mid = len(lists) // 2
    left = mergeKLists(lists[:mid])
    right = mergeKLists(lists[mid:])
    
    return mergeTwoLists(left, right)

# ==========================================
# 8. Розвернути вузли в k-групі
# ==========================================
def reverseKGroup(head: ListNode, k: int) -> ListNode:
    def get_kth_node(curr: ListNode, k: int) -> ListNode:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
        
    dummy = ListNode(0, head)
    groupPrev = dummy
    
    while True:
        kth = get_kth_node(groupPrev, k)
        if not kth:
            break
            
        groupNext = kth.next
        
        # Перевертаємо групу
        prev, curr = kth.next, groupPrev.next
        while curr != groupNext:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            
        tmp = groupPrev.next
        groupPrev.next = kth
        groupPrev = tmp
        
    return dummy.next

# ==========================================
# 9. Розділити список
# ==========================================
def partition(head: ListNode, x: int) -> ListNode:
    less_head = ListNode()
    greater_head = ListNode()
    
    less = less_head
    greater = greater_head
    
    curr = head
    while curr:
        if curr.val < x:
            less.next = curr
            less = less.next
        else:
            greater.next = curr
            greater = greater.next
        curr = curr.next
        
    greater.next = None
    less.next = greater_head.next
    
    return less_head.next