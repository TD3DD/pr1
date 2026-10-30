# ==========================================
# 1. Максимальна кількість повторень
# ==========================================
def find_max_consecutive_ones(nums: list[int]) -> int:
    max_count = 0
    current_count = 0
    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    return max_count

# ==========================================
# 2. Знайдіть числа з парною кількістю цифр
# ==========================================
def find_numbers(nums: list[int]) -> int:
    count = 0
    for num in nums:
        if len(str(num)) % 2 == 0:
            count += 1
    return count

# ==========================================
# 3. Квадрати відсортованого масиву
# ==========================================
def sorted_squares(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    
    for i in range(n - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[i] = nums[left] ** 2
            left += 1
        else:
            result[i] = nums[right] ** 2
            right -= 1
    return result

# ==========================================
# 4. Подвійні нулі
# ==========================================
def duplicate_zeros(arr: list[int]) -> None:
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            arr.insert(i, 0)
            arr.pop()
            i += 2
        else:
            i += 1

# ==========================================
# 5. Об’єднати відсортований масив
# ==========================================
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
    
    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

# ==========================================
# 6. Видалити дублікати з відсортованого масиву
# ==========================================
def remove_duplicates(nums: list[int]) -> int:
    if not nums:
        return 0
    
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
            
    return slow + 1

# ==========================================
# 7. Перевірте, чи існують N і його подвійник
# ==========================================
def check_if_exist(arr: list[int]) -> bool:
    seen = set()
    for num in arr:
        if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
            return True
        seen.add(num)
    return False

# ==========================================
# 8. Дійсний гірський масив
# ==========================================
def valid_mountain_array(arr: list[int]) -> bool:
    n = len(arr)
    if n < 3:
        return False
    
    i = 0
    while i + 1 < n and arr[i] < arr[i + 1]:
        i += 1
        
    if i == 0 or i == n - 1:
        return False
        
    while i + 1 < n and arr[i] > arr[i + 1]:
        i += 1
        
    return i == n - 1

# ==========================================
# 9. Замініть елементи на найбільший елемент з правого боку
# ==========================================
def replace_elements(arr: list[int]) -> list[int]:
    max_so_far = -1
    for i in range(len(arr) - 1, -1, -1):
        current = arr[i]
        arr[i] = max_so_far
        max_so_far = max(max_so_far, current)
    return arr

# ==========================================
# 10. Відсортувати масив за парністю
# ==========================================
def sort_array_by_parity(nums: list[int]) -> list[int]:
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] % 2 != 0 and nums[right] % 2 == 0:
            nums[left], nums[right] = nums[right], nums[left]
        
        if nums[left] % 2 == 0:
            left += 1
        if nums[right] % 2 != 0:
            right -= 1
            
    return nums


# ==========================================
# Блок для локального тестування коду
# ==========================================
if __name__ == "__main__":
    print("--- Завдання 1 ---")
    print(find_max_consecutive_ones([1, 1, 0, 1, 1, 1]))

    print("\n--- Завдання 2 ---")
    print(find_numbers([12, 345, 2, 6, 7896]))

    print("\n--- Завдання 3 ---")
    print(sorted_squares([-4, -1, 0, 3, 10]))

    print("\n--- Завдання 4 ---")
    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    duplicate_zeros(arr)
    print(arr)

    print("\n--- Завдання 5 ---")
    nums1 = [1, 2, 3, 0, 0, 0]
    merge(nums1, 3, [2, 5, 6], 3)
    print(nums1)

    print("\n--- Завдання 6 ---")
    nums_dup = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = remove_duplicates(nums_dup)
    print(f"k = {k}, nums = {nums_dup[:k]}")

    print("\n--- Завдання 7 ---")
    print(check_if_exist([10, 2, 5, 3]))

    print("\n--- Завдання 8 ---")
    print(valid_mountain_array([0, 3, 2, 1]))

    print("\n--- Завдання 9 ---")
    print(replace_elements([17, 18, 5, 4, 6, 1]))

    print("\n--- Завдання 10 ---")
    print(sort_array_by_parity([3, 1, 2, 4]))