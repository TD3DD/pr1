# ==========================================
# Завдання 2: Допоміжний клас для вузлів (Node)
# ==========================================
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    # Допоміжний метод для зручного виводу списку при тестуванні
    def __str__(self):
        result = []
        current = self
        while current: # (Використовується лише для print, не для самої логіки завдання)
            result.append(str(current.val))
            current = current.next
        return "[" + ", ".join(result) + "]"


# ==========================================
# Завдання 1: Зворотній порядок рядка
# ==========================================
def reverse_string(s: str) -> str:
    if not s:
        return ""
    return reverse_string(s[1:]) + s[0]


# ==========================================
# Завдання 2: Заміна сусідніх вузлів
# ==========================================
def swap_pairs(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    
    new_head = head.next
    head.next = swap_pairs(new_head.next)
    new_head.next = head
    
    return new_head


# ==========================================
# Завдання 3: Числа Фібоначчі
# ==========================================
def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)


# ==========================================
# Завдання 4: Підйом по сходах
# ==========================================
def climb_stairs(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    return climb_stairs(n - 1) + climb_stairs(n - 2)


# ==========================================
# Завдання 5: Піднесення в ступінь
# ==========================================
def my_pow(x: float, n: int) -> float:
    if n == 0:
        return 1.0
    
    if n < 0:
        return 1.0 / my_pow(x, -n)
    
    half = my_pow(x, n // 2)
    
    if n % 2 == 0:
        return half * half
    else:
        return half * half * x


# ==========================================
# Блок для локального тестування коду
# ==========================================
if __name__ == "__main__":
    print("--- Завдання 1 ---")
    print(f"Input: 'tiger' -> Output: '{reverse_string('tiger')}'")
    
    print("\n--- Завдання 2 ---")
    node4 = ListNode(4)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    print(f"Input: {node1}")
    print(f"Output: {swap_pairs(node1)}")
    
    print("\n--- Завдання 3 ---")
    print(f"F(4) = {fibonacci(4)}")
    
    print("\n--- Завдання 4 ---")
    print(f"Ways to climb 3 stairs: {climb_stairs(3)}")
    
    print("\n--- Завдання 5 ---")
    print(f"2.0 ^ 10 = {my_pow(2.00000, 10):.5f}")
    print(f"2.1 ^ 3 = {my_pow(2.10000, 3):.5f}")
    print(f"2.0 ^ -2 = {my_pow(2.00000, -2):.5f}")