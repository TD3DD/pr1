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
    
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    prev, curr = None, slow.next
    slow.next = None
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        
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
    node.val = node.next.val
    node.next = node.next.next

# ==========================================
# 6. Подвоїти число, представлене у вигляді зв’язаного списку
# ==========================================
def doubleIt(head: ListNode) -> ListNode:
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


# ==========================================
# Блок для локального тестування коду
# ==========================================
if __name__ == "__main__":
    def to_ll(arr):
        if not arr: return None
        head = ListNode(arr[0])
        curr = head
        for val in arr[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head

    def to_list(head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res

    print("--- Завдання 1 ---")
    l1 = to_ll([1, 2, 4])
    l2 = to_ll([1, 3, 4])
    print("Output:", to_list(mergeTwoLists(l1, l2)))

    print("\n--- Завдання 2 ---")
    print("Output:", to_list(deleteDuplicates(to_ll([1, 1, 2, 3, 3]))))

    print("\n--- Завдання 3 ---")
    # Створюємо список і штучно робимо цикл для перевірки (хвіст вказує на вузол "2")
    l3 = to_ll([3, 2, 0, -4])
    l3.next.next.next.next = l3.next 
    print("Output (has cycle?):", hasCycle(l3))

    print("\n--- Завдання 4 ---")
    l4 = to_ll([1, 2, 3, 4])
    reorderList(l4)
    print("Output:", to_list(l4))

    print("\n--- Завдання 5 ---")
    l5 = to_ll([4, 5, 1, 9])
    deleteNode(l5.next) 
    print("Output:", to_list(l5))

    print("\n--- Завдання 6 ---")
    print("Output:", to_list(doubleIt(to_ll([1, 8, 9]))))

    print("\n--- Завдання 7 ---")
    list_arr = [to_ll([1, 4, 5]), to_ll([1, 3, 4]), to_ll([2, 6])]
    print("Output:", to_list(mergeKLists(list_arr)))

    print("\n--- Завдання 8 ---")
    print("Output:", to_list(reverseKGroup(to_ll([1, 2, 3, 4, 5]), 2)))

    print("\n--- Завдання 9 ---")
    print("Output:", to_list(partition(to_ll([1, 4, 3, 2, 5, 2]), 3)))