# 🧩 Contains Duplicate (Problem-217)

> **LeetCode; #217 — Easy**

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
true
```

**Explanation:**

The element `1` occurs at indices `0` and `3`.

Therefore, the array contains a duplicate.

---

### Example 2

**Input:**

```text
nums = [1,2,3,4]
```

**Output:**

```text
false
```

**Explanation:**

All elements in the array are distinct.

---

### Example 3

**Input:**

```text
nums = [1,1,1,3,3,4,3,2,4,2]
```

**Output:**

```text
true
```

**Explanation:**

The value `1` appears multiple times, so the array contains a duplicate.

---

## 📋 Constraints

* `1 <= nums.length <= 10⁵`
* `-10⁹ <= nums[i] <= 10⁹`

---

## 🚀 Approach

A brute-force solution would compare every element with every other element.

This would result in:

```text
O(n²)
```

However, we can solve the problem more efficiently using a **Hash Set**.

### 🔹 Key Idea

A set stores only **unique elements**.

While traversing the array:

1. Check whether the current element already exists in the set.
2. If it exists, we have found a duplicate → return `true`.
3. Otherwise, add the element to the set.
4. If we finish traversing the array without finding a duplicate, return `false`.

### 🔄 Example

For:

```text
nums = [1,2,3,1]
```

| Index | Number | Seen Set  | Result       |
| ----: | -----: | :-------- | :----------- |
|     0 |      1 | `{1}`     | Add `1`      |
|     1 |      2 | `{1,2}`   | Add `2`      |
|     2 |      3 | `{1,2,3}` | Add `3`      |
|     3 |      1 | `{1,2,3}` | `1` exists ✅ |

Since `1` is already present in the set:

```text
return True
```

---





## ⏱️ Complexity Analysis

### Time Complexity

```text
O(n)
```

We traverse the array only once, and set lookups are `O(1)` on average.

### Space Complexity

```text
O(n)
```

In the worst case, the set can store all `n` elements.

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
Runtime: 23 ms
Beats: 28.54%

Memory: 32.30 MB
Beats: 54.69%
```

| Metric             | Result           |
| ------------------ | ---------------- |
| 🟢 Status          | **Accepted**     |
| 🧪 Test Cases      | **79 / 79**      |
| ⚡ Runtime          | **23 ms**        |
| 🏆 Runtime Ranking | **Beats 28.54%** |
| 💾 Memory          | **32.30 MB**     |
| 📊 Memory Ranking  | **Beats 54.69%** |
| 🐍 Language        | **Python 3**     |

---

## 🧠 What I Learned

This problem demonstrates an important technique for efficiently detecting duplicates:

> **Use a Hash Set when you need fast membership checking.**

Instead of comparing every pair of elements using `O(n²)` time, we can store previously encountered elements and check for duplicates in **O(1) average time**.

This reduces the solution from:

```text
O(n²) → O(n)
```

---

## 🔑 Concepts Used

* Arrays
* Sets
* Hashing
* Membership Checking
* One-pass Traversal
* Time & Space Complexity
* Problem-Solving Optimization

---




## 📚 Problem Link

🔗 [LeetCode — Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

---

## ⭐ Progress

**LeetCode Problems Solved:** `2`

**Previous Problem:** Two Sum

**Current Problem:** Contains Duplicate

> One problem at a time. One optimization at a time. 🚀
