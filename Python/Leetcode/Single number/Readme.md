# 🧩 Single Number (Problem-136)

> **LeetCode; #136 — Easy**

[![LeetCode](https://img.shields.io/badge/LeetCode-136-orange?style=for-the-badge\&logo=leetcode)](https://leetcode.com/problems/single-number/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problems/single-number/)
[![Language](https://img.shields.io/badge/Language-Python%203-blue?style=for-the-badge\&logo=python)](https://www.python.org/)
[![Accepted](https://img.shields.io/badge/Status-Accepted-success?style=for-the-badge)](https://leetcode.com/problems/single-number/)

---

## 📌 Problem

Given a **non-empty array of integers** `nums`, every element appears **twice** except for one element.

Find and return the element that appears only once.

The solution must have:

* **Linear runtime complexity:** `O(n)`
* **Constant extra space:** `O(1)`

---

## 💡 Examples

### Example 1

**Input:**

```text
nums = [2,2,1]
```

**Output:**

```text
1
```

**Explanation:**

`2` appears twice, while `1` appears only once.

Therefore, the answer is `1`.

---

### Example 2

**Input:**

```text
nums = [4,1,2,1,2]
```

**Output:**

```text
4
```

**Explanation:**

`1` and `2` appear twice, while `4` appears only once.

Therefore, the answer is `4`.

---

### Example 3

**Input:**

```text
nums = [1]
```

**Output:**

```text
1
```

**Explanation:**

The only element in the array appears once.

---

## 📋 Constraints

* `1 <= nums.length <= 3 * 10⁴`
* `-3 * 10⁴ <= nums[i] <= 3 * 10⁴`
* Every element appears twice except for one element which appears only once.

---

## 🚀 Approach

The most efficient way to solve this problem is using the **XOR (`^`) operator**.

### 🔹 Key Idea

The XOR operator has two important properties:

```text
a ^ a = 0
```

A number XORed with itself becomes `0`.

And:

```text
a ^ 0 = a
```

A number XORed with `0` remains unchanged.

Therefore, when every number appears twice except one:

```text
a ^ b ^ a ^ b ^ unique
```

the duplicate numbers cancel each other out:

```text
(a ^ a) ^ (b ^ b) ^ unique
```

which becomes:

```text
0 ^ 0 ^ unique
```

and finally:

```text
unique
```

This allows us to find the single number in **one traversal** without using any extra data structure.

---

## 🔄 Example

For:

```text
nums = [4,1,2,1,2]
```

We start with:

```text
unique = 0
```

Then XOR every element:

| Step | Number | XOR Operation | `unique` |
| ---: | -----: | :------------ | -------: |
|    1 |      4 | `0 ^ 4`       |      `4` |
|    2 |      1 | `4 ^ 1`       |      `5` |
|    3 |      2 | `5 ^ 2`       |      `7` |
|    4 |      1 | `7 ^ 1`       |      `6` |
|    5 |      2 | `6 ^ 2`       |      `4` |

The duplicate values cancel:

```text
4 ^ 1 ^ 2 ^ 1 ^ 2
```

becomes:

```text
4 ^ (1 ^ 1) ^ (2 ^ 2)
```

```text
4 ^ 0 ^ 0
```

Therefore:

```text
4
```

is the single number.

---



## 🔍 Code Explanation

### 1. Initialize `unique`

```python
unique = 0
```

We start with `0` because:

```text
0 ^ x = x
```

---

### 2. XOR Every Element

```python
for i in nums:
    unique ^= i
```

This is equivalent to:

```python
unique = unique ^ i
```

Every duplicate number cancels itself out because:

```text
x ^ x = 0
```

---

### 3. Return the Remaining Number

```python
return unique
```

After all elements have been processed, every duplicated number has cancelled out, leaving only the number that appears once.

---

## ⏱️ Complexity Analysis

Let `n` be the length of `nums`.

### Time Complexity

```text
O(n)
```

We traverse the array exactly once.

### Space Complexity

```text
O(1)
```

Only one variable, `unique`, is used regardless of the input size.

| Complexity | Value    |
| ---------- | -------- |
| ⏱️ Time    | **O(n)** |
| 💾 Space   | **O(1)** |

---

## 🏆 My LeetCode Result

**Status:** ✅ Accepted

```text
61 / 61 test cases passed
```

### ⚡ Performance

```text
Runtime: 0 ms
Beats: 100.00%

Memory: 21.06 MB
Beats: 70.05%
```

| Metric             | Result            |
| ------------------ | ----------------- |
| 🟢 Status          | **Accepted**      |
| 🧪 Test Cases      | **61 / 61**       |
| ⚡ Runtime          | **0 ms**          |
| 🏆 Runtime Ranking | **Beats 100.00%** |
| 💾 Memory          | **21.06 MB**      |
| 📊 Memory Ranking  | **Beats 70.05%**  |
| 🐍 Language        | **Python 3**      |

---

## 🧠 What I Learned

This problem demonstrates one of the most useful properties of the **XOR operator**.

The key observations are:

```text
x ^ x = 0
x ^ 0 = x
```

Because every number except one appears exactly twice, all duplicate numbers cancel each other out.

> **XOR allows us to find the unique element in `O(n)` time using `O(1)` extra space.**

This perfectly satisfies the requirements of the problem without using a set, dictionary, or sorting.

---

## 🔑 Concepts Used

* Arrays
* Bit Manipulation
* XOR Operator
* One-pass Traversal
* Duplicate Cancellation
* Constant Space
* Time & Space Complexity

---

## 🎯 Follow-Up

### Can you solve this problem without using extra space?

Yes.

The XOR approach solves it using:

```text
O(n) time
O(1) space
```

No additional array, set, dictionary, or sorting is required.

---

## 📚 Problem Link

🔗 [LeetCode — Single Number](https://leetcode.com/problems/single-number/)

---

## ⭐ Progress

**LeetCode Problems Solved:** `6`


> One problem at a time. One optimization at a time. 🚀
