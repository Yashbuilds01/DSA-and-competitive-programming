# 🧩 Contains Duplicate — Alternate Solution (Problem-217)

> **LeetCode; #217 — Easy**
> **Alternative Solution**

[![LeetCode](https://img.shields.io/badge/LeetCode-217-orange?style=for-the-badge\&logo=leetcode)](https://leetcode.com/problems/contains-duplicate/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problems/contains-duplicate/)
[![Language](https://img.shields.io/badge/Language-Python%203-blue?style=for-the-badge\&logo=python)](https://www.python.org/)
[![Accepted](https://img.shields.io/badge/Status-Accepted-success?style=for-the-badge)](https://leetcode.com/problems/contains-duplicate/)
---

## 📌 Problem

Given an integer array `nums`, return **`true`** if any value appears **at least twice** in the array.

Return **`false`** if every element in the array is distinct.

---

## 💡 Examples

### Example 1

**Input:**

```text
nums = [1,2,3,1]
```

**Output:**

```text
True
```

**Explanation:**

The element `1` appears more than once.

---

### Example 2

**Input:**

```text
nums = [1,2,3,4]
```

**Output:**

```text
False
```

**Explanation:**

Every element is unique.

---

### Example 3

**Input:**

```text
nums = [1,1,1,3,3,4,3,2,4,2]
```

**Output:**

```text
True
```

**Explanation:**

Several elements appear more than once.

---

## 📋 Constraints

* `1 <= nums.length <= 10⁵`
* `-10⁹ <= nums[i] <= 10⁹`

---

## 🚀 Approach

This is an **alternate and more concise solution** to the problem.

The key idea is to compare:

```text
Length of the original array
```

with:

```text
Length of the set containing its elements
```

### 🔹 Why does this work?

A Python `set` stores only **unique elements**.

For example:

```text
nums = [1,2,3,1]
```

The original array contains:

```text
4 elements
```

But:

```python
set(nums)
```

produces:

```text
{1,2,3}
```

which contains only:

```text
3 unique elements
```

Therefore:

```text
len(nums) != len(set(nums))
```

is `True`, meaning a duplicate exists.

If all elements are unique:

```text
nums = [1,2,3,4]

len(nums)       = 4
len(set(nums))  = 4
```

So:

```text
len(nums) != len(set(nums))
```

is `False`.

---


## 🔍 Code Explanation

### `set(nums)`

```python
set(nums)
```

Converts the array into a set and automatically removes duplicate values.

### `len(nums)`

Returns the total number of elements in the original array.

### `len(set(nums))`

Returns the number of **unique** elements.

### Final Comparison

```python
return len(nums) != len(set(nums))
```

If the two lengths are different, at least one duplicate exists.

Therefore:

```text
Different lengths → Duplicate exists → True
Same lengths      → All unique      → False
```

---

## ⏱️ Complexity Analysis

### Time Complexity

```text
O(n)
```

Creating the set requires traversing the array.

### Space Complexity

```text
O(n)
```

The set can contain up to `n` unique elements.

| Complexity | Value    |
| ---------- | -------- |
| ⏱️ Time    | **O(n)** |
| 💾 Space   | **O(n)** |

---

## 🏆 My LeetCode Result

**Status:** ✅ Accepted

```text
79 / 79 test cases passed
```

### ⚡ Performance

```text
Runtime: 5 ms
Beats: 93.85%

Memory: 32.29 MB
Beats: 54.69%
```

| Metric             | Result           |
| ------------------ | ---------------- |
| 🟢 Status          | **Accepted**     |
| 🧪 Test Cases      | **79 / 79**      |
| ⚡ Runtime          | **5 ms**         |
| 🏆 Runtime Ranking | **Beats 93.85%** |
| 💾 Memory          | **32.29 MB**     |
| 📊 Memory Ranking  | **Beats 54.69%** |
| 🐍 Language        | **Python 3**     |

---

## 🧠 What I Learned

This solution demonstrates how Python's built-in `set` can make a solution extremely concise.

Instead of manually checking every element, we can let the set automatically remove duplicates and then compare the number of unique elements with the original array size.

> **If the number of unique elements is smaller than the total number of elements, a duplicate exists.**

This provides the same asymptotic complexity as the previous solution:

```text
O(n) time
O(n) space
```

but with significantly less code.

---

## 🔄 Comparison With Previous Solution

### Previous Approach

```python
seen = set()

for i in nums:
    if i in seen:
        return True
    seen.add(i)

return False
```

### Alternate Approach

```python
return len(nums) != len(set(nums))
```

Both approaches have:

```text
Time:  O(n)
Space: O(n)
```

However, the alternate solution is **more concise and Pythonic**, while the previous solution makes the duplicate-detection process more explicit.

---

## 🔑 Concepts Used

* Arrays
* Sets
* Hashing
* Duplicate Detection
* `set()` Function
* `len()` Function
* Pythonic Solutions
* Time & Space Complexity

---

## 📚 Problem Link

🔗 [LeetCode — Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

---

## ⭐ Progress

**LeetCode Problems Solved:** `2`

**Problem:** Contains Duplicate

**Solution:** Alternate Approach

> Same problem. Different approach. Better understanding. 🚀
