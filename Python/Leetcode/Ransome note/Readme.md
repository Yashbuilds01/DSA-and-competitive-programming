# 📝 Ransom Note

> **LeetCode #383 — Easy**

[![LeetCode](https://img.shields.io/badge/LeetCode-383-orange?style=for-the-badge\&logo=leetcode)](https://leetcode.com/problems/ransom-note/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problems/ransom-note/)
[![Language](https://img.shields.io/badge/Language-Python%203-blue?style=for-the-badge\&logo=python)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Accepted-success?style=for-the-badge)](https://leetcode.com/problems/ransom-note/)

---

## 📌 Problem

Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed using the letters from `magazine`, and `false` otherwise.

Each letter in `magazine` can only be used **once** in `ransomNote`.

---

## 💡 Examples

### Example 1

**Input:**

```text
ransomNote = "a"
magazine = "b"
```

**Output:**

```text
false
```

---

### Example 2

**Input:**

```text
ransomNote = "aa"
magazine = "ab"
```

**Output:**

```text
false
```

---

### Example 3

**Input:**

```text
ransomNote = "aa"
magazine = "aab"
```

**Output:**

```text
true
```

---

## 📋 Constraints

* `1 <= ransomNote.length, magazine.length <= 10⁵`
* `ransomNote` and `magazine` consist of lowercase English letters.

---

## 🚀 Approach

The main idea is to keep track of how many times each character appears in `magazine`.

For every character in `ransomNote`, we need to check whether the required character is available.

### 🔹 Steps

1. Count the frequency of every character in `magazine`.
2. Traverse through `ransomNote`.
3. For each character:

   * If it is not available, return `False`.
   * Otherwise, use one occurrence by decreasing its count.
4. If every character can be constructed, return `True`.

Since there are only **26 lowercase English letters**, a frequency array/dictionary can efficiently track the available characters.

---


## ⏱️ Complexity Analysis

Let:

* `n` = length of `ransomNote`
* `m` = length of `magazine`

### Time Complexity

```text
O(n + m)
```

Both strings are traversed once.

### Space Complexity

```text
O(1)
```

Since the input contains only lowercase English letters, at most 26 different characters need to be stored.

| Complexity | Value        |
| ---------- | ------------ |
| ⏱️ Time    | **O(n + m)** |
| 💾 Space   | **O(1)**     |

---

## 🏆 LeetCode Result

**Status:** ✅ Accepted

```text
130 / 130 test cases passed
```

### ⚡ Performance

```text
Runtime: 26 ms
Beats: 37.57%

Memory: 19.60 MB
Beats: 74.27%
```

| Metric             | Result                 |
| ------------------ | ---------------------- |
| 🟢 Status          | **Accepted**           |
| 🧪 Test Cases      | **130 / 130**          |
| ⚡ Runtime          | **26 ms**              |
| 📊 Runtime Ranking | **Beats 37.57%**       |
| 💾 Memory          | **19.60 MB**           |
| 📊 Memory Ranking  | **Beats 74.27%**       |
| 🐍 Language        | **Python 3**           |
| 📅 Submitted       | **September 23, 2026** |

---

## 🧠 Key Concept

This problem is a good example of **frequency counting**.

Instead of repeatedly searching for characters in `magazine`, we keep track of how many times each character is available.

For example:

```text
magazine = "aab"
```

Frequency:

```text
a → 2
b → 1
```

For:

```text
ransomNote = "aa"
```

We consume two `a`s:

```text
a → 2 → 1 → 0
```

Since both required characters were available, the answer is `true`.

---

## 🔑 Concepts Used

* Strings
* Hash Maps / Dictionaries
* Frequency Counting
* Character Traversal
* Greedy Consumption
* Time & Space Complexity

---

## 📚 Problem Link

🔗 [LeetCode — Ransom Note](https://leetcode.com/problems/ransom-note/)

---

## 📈 LeetCode Progress

**Problems Solved:** `2+`

> Building the fundamentals one problem at a time. 🚀
