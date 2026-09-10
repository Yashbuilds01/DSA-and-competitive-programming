# 🧩 Valid Anagram (Problem-242)

> **LeetCode; #242 — Easy**

[![LeetCode](https://img.shields.io/badge/LeetCode-242-orange?style=for-the-badge\&logo=leetcode)](https://leetcode.com/problems/valid-anagram/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problems/valid-anagram/)
[![Language](https://img.shields.io/badge/Language-Python%203-blue?style=for-the-badge\&logo=python)](https://www.python.org/)
[![Accepted](https://img.shields.io/badge/Status-Accepted-success?style=for-the-badge)](https://leetcode.com/problems/valid-anagram/)

---

## 📌 Problem

Given two strings `s` and `t`, return **`true`** if `t` is an anagram of `s`, and **`false`** otherwise.

An **anagram** is a word or phrase formed by rearranging the letters of another word or phrase, using **all the original letters exactly once**.

---

## 💡 Examples

### Example 1

**Input:**

```text
s = "anagram"
t = "nagaram"
```

**Output:**

```text
true
```

**Explanation:**

Both strings contain exactly the same characters with the same frequencies.

```text
a → 3
n → 1
g → 1
r → 1
m → 1
```

Therefore, `t` is an anagram of `s`.

---

### Example 2

**Input:**

```text
s = "rat"
t = "car"
```

**Output:**

```text
false
```

**Explanation:**

The character frequencies are different.

```text
s → r:1, a:1, t:1
t → c:1, a:1, r:1
```

Since the characters do not match, `t` is not an anagram of `s`.

---

## 📋 Constraints

* `1 <= s.length, t.length <= 5 * 10⁴`
* `s` and `t` consist of lowercase English letters.

---

## 🚀 Approach

The first thing we need to check is whether both strings have the **same length**.

If their lengths are different, they cannot possibly be anagrams.

```python
if len(s) != len(t):
    return False
```

After that, we need to compare the **frequency of every character** in both strings.

### 🔹 Key Idea

We use:

```python
set(s)
```

to get all the **unique characters** present in `s`.

Then, for every unique character, we compare how many times it occurs in both strings:

```python
s.count(i) != t.count(i)
```

If any character has a different frequency, the strings are not anagrams.

If every character has the same frequency, the strings are anagrams.

### 🔄 Example

For:

```text
s = "anagram"
t = "nagaram"
```

The unique characters in `s` are:

```text
{a, n, g, r, m}
```

We compare their frequencies:

| Character | `s.count()` | `t.count()` | Match |
| --------: | ----------: | ----------: | :---- |
|       `a` |           3 |           3 | ✅     |
|       `n` |           1 |           1 | ✅     |
|       `g` |           1 |           1 | ✅     |
|       `r` |           1 |           1 | ✅     |
|       `m` |           1 |           1 | ✅     |

All frequencies match, so we return:

```text
true
```


---

## 🔍 Code Explanation

### 1. Check String Length

```python
if len(s) != len(t):
    return False
```

Anagrams must contain exactly the same number of characters.

Therefore, different lengths immediately mean the strings cannot be anagrams.

---

### 2. Get Unique Characters

```python
set(s)
```

A set removes duplicate characters.

For example:

```text
s = "banana"
```

then:

```python
set(s)
```

gives:

```text
{'b', 'a', 'n'}
```

We only need to check each character once.

---

### 3. Compare Character Frequencies

```python
if s.count(i) != t.count(i):
    return False
```

`count()` tells us how many times a character appears in a string.

If the frequency differs in either string, they cannot be anagrams.

---

### 4. Return True

```python
return True
```

If every character has the same frequency, the strings are valid anagrams.

---

## ⏱️ Complexity Analysis

Let `n` be the length of the strings.

The solution uses `set(s)` and calls `count()` for each unique character.

Since the strings contain lowercase English letters, there can be at most **26 unique characters**.

Therefore, the practical complexity is:

```text
Time:  O(26 × n)
```

which can be treated as:

```text
O(n)
```

for lowercase English letters.

### Space Complexity

The set stores at most 26 characters:

```text
O(26) → O(1)
```

| Complexity | Value    |
| ---------- | -------- |
| ⏱️ Time    | **O(n)** |
| 💾 Space   | **O(1)** |

---

## 🏆 My LeetCode Result

**Status:** ✅ Accepted

```text
55 / 55 test cases passed
```

### ⚡ Performance

```text
Runtime: 3 ms
Beats: 98.43%

Memory: 19.32 MB
Beats: 75.96%
```

| Metric             | Result           |
| ------------------ | ---------------- |
| 🟢 Status          | **Accepted**     |
| 🧪 Test Cases      | **55 / 55**      |
| ⚡ Runtime          | **3 ms**         |
| 🏆 Runtime Ranking | **Beats 98.43%** |
| 💾 Memory          | **19.32 MB**     |
| 📊 Memory Ranking  | **Beats 75.96%** |
| 🐍 Language        | **Python 3**     |

---

## 🧠 What I Learned

This problem demonstrates how **character frequency** can be used to determine whether two strings are anagrams.

The important idea is:

> **Two strings are anagrams if every character appears the same number of times in both strings.**

This solution uses Python's built-in:

```python
set()
```

to identify unique characters and:

```python
count()
```

to compare their frequencies.

---

## 🔑 Concepts Used

* Strings
* Sets
* Character Frequency
* `set()`
* `count()`
* String Length
* Early Return
* Time & Space Complexity

---

## 🎯 Follow-Up

### Can you solve this problem using a Hash Map?

Yes.

Instead of repeatedly using `count()`, we can store the frequency of every character in a dictionary.

That approach can achieve:

```text
O(n) time
O(n) space
```

A frequency-array solution can also achieve:

```text
O(n) time
O(1) space
```

when the input is restricted to lowercase English letters.

---

## 📚 Problem Link

🔗 [LeetCode — Valid Anagram](https://leetcode.com/problems/valid-anagram/)

---

## ⭐ Progress

**LeetCode Problems Solved:** `3`

**Previous Problems:**

* Two Sum
* Contains Duplicate

**Current Problem:** Valid Anagram

> One problem at a time. One optimization at a time. 🚀
