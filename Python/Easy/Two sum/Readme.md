# 🧩 Two Sum

> **LeetCode #1 — Easy**

[![LeetCode](https://img.shields.io/badge/LeetCode-1-orange?style=for-the-badge\&logo=leetcode)](https://leetcode.com/problems/two-sum/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problems/two-sum/)
[![Language](https://img.shields.io/badge/Language-Python%203-blue?style=for-the-badge\&logo=python)](https://www.python.org/)
[![Accepted](https://img.shields.io/badge/Status-Accepted-success?style=for-the-badge)](https://leetcode.com/problems/two-sum/)

---

## 📌 Problem

Given an array of integers `nums` and an integer `target`, return the **indices of the two numbers** such that they add up to `target`.

You may assume that each input has **exactly one solution**, and you may not use the same element twice.

The answer can be returned in any order.

---

## 💡 Examples

### Example 1

**Input:**

```text
nums = [2,7,11,15]
target = 9
```

**Output:**

```text
[0,1]
```

**Explanation:**

`nums[0] + nums[1] = 2 + 7 = 9`

Therefore, the answer is `[0, 1]`.

---

### Example 2

**Input:**

```text
nums = [3,2,4]
target = 6
```

**Output:**

```text
[1,2]
```

**Explanation:**

`nums[1] + nums[2] = 2 + 4 = 6`

---

### Example 3

**Input:**

```text
nums = [3,3]
target = 6
```

**Output:**

```text
[0,1]
```

**Explanation:**

`nums[0] + nums[1] = 3 + 3 = 6`

---

## 📋 Constraints

* `2 <= nums.length <= 10⁴`
* `-10⁹ <= nums[i] <= 10⁹`
* `-10⁹ <= target <= 10⁹`
* Exactly **one valid answer** exists.
* The same element cannot be used twice.

---

## 🚀 Approach

A brute-force solution would check every possible pair of numbers, resulting in:

```text
O(n²)
```

However, we can do better using a **Hash Map (Dictionary)**.

### 🔹 Key Idea

While traversing the array, for every number `num`, calculate its required complement:

```text
complement = target - num
```

Then check whether that complement has already been seen.

If it exists:

```text
num + complement = target
```

and we can immediately return their indices.

Otherwise, store the current number and its index in the dictionary.

### 🔄 Example

For:

```text
nums = [2,7,11,15]
target = 9
```

| Index | Number | Complement | Seen         |
| ----: | -----: | ---------: | ------------ |
|     0 |      2 |          7 | `{2: 0}`     |
|     1 |      7 |          2 | `2` exists ✅ |

Therefore:

```text
[0, 1]
```

---


---

## ⏱️ Complexity Analysis

### Time Complexity

```text
O(n)
```

We traverse the array only once, and dictionary lookups are `O(1)` on average.

### Space Complexity

```text
O(n)
```

The dictionary can store up to `n` elements.

| Complexity | Value    |
| ---------- | -------- |
| ⏱️ Time    | **O(n)** |
| 💾 Space   | **O(n)** |

---

## 🏆 My LeetCode Result

**Status:** ✅ Accepted

```text
65 / 65 test cases passed
```

### ⚡ Performance

```text
Runtime: 0 ms
Beats: 100.00%

Memory: 20.58 MB
Beats: 18.44%
```

| Metric             | Result            |
| ------------------ | ----------------- |
| 🟢 Status          | **Accepted**      |
| 🧪 Test Cases      | **65 / 65**       |
| ⚡ Runtime          | **0 ms**          |
| 🏆 Runtime Ranking | **Beats 100.00%** |
| 💾 Memory          | **20.58 MB**      |
| 📊 Memory Ranking  | **Beats 18.44%**  |
| 🐍 Language        | **Python 3**      |

---

## 🧠 What I Learned

This problem demonstrates one of the most important patterns in array problems:

> **Use a Hash Map to trade space for faster lookups.**

Instead of searching for the required pair repeatedly, we remember the numbers we have already encountered.

This reduces the solution from:

```text
O(n²) → O(n)
```

which is a major improvement.

---

## 🔑 Concepts Used

* Arrays
* Hash Maps / Dictionaries
* Complement Technique
* One-pass Traversal
* Time & Space Complexity
* Problem-Solving Optimization

---

## 🎯 Follow-Up

**Can you come up with an algorithm that is less than `O(n²)` time complexity?**

### Answer

Yes.

Using a hash map, the problem can be solved in:

```text
O(n) time
O(n) space
```

This is the approach used in this solution.

---

## 📚 Problem Link

🔗 [LeetCode — Two Sum](https://leetcode.com/problems/two-sum/)

---

## ⭐ Progress

**LeetCode Problems Solved:** `1`

**First Problem:** Two Sum

> One problem at a time. One optimization at a time. 🚀
