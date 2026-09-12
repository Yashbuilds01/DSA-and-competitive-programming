# 🧩 Valid Palindrome (Problem-125)

> **LeetCode; #125 — Easy**

[![LeetCode](https://img.shields.io/badge/LeetCode-125-orange?style=for-the-badge\&logo=leetcode)](https://leetcode.com/problems/valid-palindrome/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problems/valid-palindrome/)
[![Language](https://img.shields.io/badge/Language-Python%203-blue?style=for-the-badge\&logo=python)](https://www.python.org/)
[![Accepted](https://img.shields.io/badge/Status-Accepted-success?style=for-the-badge)](https://leetcode.com/problems/valid-palindrome/)

---

## 📌 Problem

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all **non-alphanumeric characters**, it reads the same forward and backward.

Alphanumeric characters include **letters and numbers**.

Given a string `s`, return `true` if it is a **palindrome**, or `false` otherwise.

---

## 💡 Examples

### Example 1

**Input:**

```text
s = "A man, a plan, a canal: Panama"
```

**Output:**

```text
true
```

**Explanation:**

After converting to lowercase and removing non-alphanumeric characters:

```text
"amanaplanacanalpanama"
```

The string reads the same forward and backward.

Therefore, it is a palindrome.

---

### Example 2

**Input:**

```text
s = "race a car"
```

**Output:**

```text
false
```

**Explanation:**

After removing spaces:

```text
"raceacar"
```

This does not read the same forward and backward.

Therefore, it is not a palindrome.

---

### Example 3

**Input:**

```text
s = " "
```

**Output:**

```text
true
```

**Explanation:**

After removing non-alphanumeric characters, the string becomes:

```text
""
```

An empty string reads the same forward and backward, so it is considered a palindrome.

---

## 📋 Constraints

* `1 <= s.length <= 2 * 10⁵`
* `s` consists only of printable ASCII characters.

---

## 🚀 Approach

The main challenge is that we need to:

1. Ignore spaces and punctuation.
2. Treat uppercase and lowercase letters as the same.
3. Check whether the resulting string is the same forward and backward.

A simple approach is to create a cleaned string containing only lowercase alphanumeric characters and then compare it with its reverse.

### 🔹 Key Idea

For every character in the string:

* Check whether it is alphanumeric.
* Convert it to lowercase.
* Add it to a new string.

For example:

```text
"A man, a plan, a canal: Panama"
```

becomes:

```text
"amanaplanacanalpanama"
```

Then compare the string with its reverse.

If both are equal:

```text
cleaned == cleaned[::-1]
```

the string is a palindrome.

---

## 🔄 Example

For:

```text
s = "A man, a plan, a canal: Panama"
```

After processing:

```text
Original:
A man, a plan, a canal: Panama

Cleaned:
amanaplanacanalpanama
```

Reverse:

```text
amanaplanacanalpanama
```

Since:

```text
cleaned == reversed
```

the result is:

```text
true
```

---


## 🔍 Code Explanation

### 1. Create a Clean String

```python
new_s = ""
```

This will store only the characters that matter for the palindrome check.

---

### 2. Traverse the String

```python
for i in s:
```

We examine every character in the input string.

---

### 3. Keep Only Alphanumeric Characters

```python
if i.isalnum():
```

`isalnum()` returns `True` for letters and numbers.

Characters such as:

```text
space
,
.
!
:
```

are ignored.

---

### 4. Convert to Lowercase

```python
new_s += i.lower()
```

This ensures that uppercase and lowercase letters are treated equally.

For example:

```text
A → a
P → p
```

---

### 5. Compare With the Reverse

```python
return new_s == new_s[::-1]
```

`[::-1]` reverses the string.

If the original cleaned string and its reverse are identical, the string is a palindrome.

---

## ⏱️ Complexity Analysis

Let `n` be the length of the input string.

### Time Complexity

```text
O(n)
```

We traverse the string once and then reverse the cleaned string.

### Space Complexity

```text
O(n)
```

We create a new string containing the alphanumeric characters.

| Complexity | Value    |
| ---------- | -------- |
| ⏱️ Time    | **O(n)** |
| 💾 Space   | **O(n)** |

---

## 🏆 My LeetCode Result

**Status:** ✅ Accepted

```text
Accepted
```

### ⚡ Performance

```text
Runtime: 7 ms
Beats: 80.78%

Memory: 19.66 MB
Beats: 53.98%
```

| Metric             | Result           |
| ------------------ | ---------------- |
| 🟢 Status          | **Accepted**     |
| ⚡ Runtime          | **7 ms**         |
| 🏆 Runtime Ranking | **Beats 80.78%** |
| 💾 Memory          | **19.66 MB**     |
| 📊 Memory Ranking  | **Beats 53.98%** |
| 🐍 Language        | **Python 3**     |

---

## 🧠 What I Learned

This problem demonstrates how **string preprocessing** can simplify a palindrome problem.

Before checking the palindrome, we normalize the input by:

* Removing irrelevant characters.
* Converting letters to lowercase.
* Comparing the cleaned string with its reverse.

The key idea is:

> **Normalize the string first, then perform the palindrome check.**

Python's built-in methods such as:

```python
isalnum()
lower()
```

make this preprocessing concise and readable.

---

## 🔑 Concepts Used

* Strings
* String Traversal
* String Slicing
* Palindromes
* `isalnum()`
* `lower()`
* String Reversal
* String Preprocessing
* Time & Space Complexity

---

## 🎯 Follow-Up

### Can you solve this problem using `O(1)` extra space?

Yes.

Instead of creating a new cleaned string, we can use **two pointers**:

```text
left  → beginning of string
right → end of string
```

We can move the pointers inward while skipping non-alphanumeric characters and compare the characters directly.

This allows the problem to be solved in:

```text
O(n) time
O(1) extra space
```

The current solution prioritizes **simplicity and readability**.

---

## 📚 Problem Link

🔗 [LeetCode — Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

---


> One problem at a time. One optimization at a time. 🚀
