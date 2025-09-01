

---

# 🔹 1. Bubble Sort (مرتب‌سازی حبابی)

ایده:
هر بار لیست رو مرور می‌کنیم و اگر دو عنصر کنار هم برعکس بودن، جاشون رو عوض می‌کنیم.
این کارو تا وقتی ادامه می‌دیم که لیست مرتب شه.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):  # بعد از هر بار، بزرگ‌ترین عنصر ته لیست قرار می‌گیره
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubble_sort([5, 2, 9, 1, 7]))
# خروجی: [1, 2, 5, 7, 9]
```

---

# 🔹 2. Selection Sort (مرتب‌سازی انتخابی)

ایده:
کوچک‌ترین عنصر رو پیدا می‌کنیم و می‌بریم سرجای اول، بعدی رو می‌ذاریم دوم، و همینطور ادامه می‌دیم.

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort([5, 2, 9, 1, 7]))
# خروجی: [1, 2, 5, 7, 9]
```

---

# 🔹 3. Insertion Sort (مرتب‌سازی درجی)

ایده:
مثل کارت بازی – هر کارت جدید رو سرجای خودش بین کارت‌های مرتب شده می‌ذاریم.

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertion_sort([5, 2, 9, 1, 7]))
# خروجی: [1, 2, 5, 7, 9]
```

---

# 🔹 4. Merge Sort (مرتب‌سازی ادغامی)

ایده:
لیست رو نصف می‌کنیم → نصف‌ها رو مرتب می‌کنیم → دوباره ادغام می‌کنیم.

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

print(merge_sort([5, 2, 9, 1, 7]))
# خروجی: [1, 2, 5, 7, 9]
```

---

# 🔹 5. Quick Sort (مرتب‌سازی سریع)

ایده:
یه **pivot** انتخاب می‌کنیم → کوچکترها میرن چپ → بزرگترها میرن راست → بازگشتی ادامه می‌دیم.

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort([5, 2, 9, 1, 7]))
# خروجی: [1, 2, 5, 7, 9]
```

---

# 🔹 6. Heap Sort (مرتب‌سازی هیپ)

ایده:
لیست رو تبدیل به heap می‌کنیم → بزرگترین عنصر رو می‌گیریم → می‌ذاریم آخر → تا خالی شدن heap ادامه می‌دیم.

```python
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr

print(heap_sort([5, 2, 9, 1, 7]))
# خروجی: [1, 2, 5, 7, 9]
```

---

# 🔹 الگوریتم‌های خاص‌تر

* **Counting Sort** → فقط برای اعداد صحیح غیرمنفی، وقتی محدوده اعداد کوچیکه.
* **Radix Sort** → اعداد رو رقم به رقم مرتب می‌کنه.
* **Bucket Sort** → داده‌ها رو توی "سطل‌ها" تقسیم می‌کنه و هر سطل رو جدا مرتب می‌کنه.

---

📌 حالا تو کلکسیونت داری:

* الگوریتم‌های ساده (Bubble, Selection, Insertion)
* الگوریتم‌های سریع و پرکاربرد (Merge, Quick, Heap)
* الگوریتم‌های خاص‌تر برای شرایط ویژه (Counting, Radix, Bucket).

---
