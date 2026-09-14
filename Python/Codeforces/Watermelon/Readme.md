# 🍉 Watermelon (Problem-A)

> **Codeforces; 4A — Watermelon**
> **Difficulty: Way too easy**

![Codeforces](https://img.shields.io/badge/Codeforces-4A-1F8ACB?style=for-the-badge\&logo=codeforces\&logoColor=white)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)
![Language](https://img.shields.io/badge/Language-PyPy%203--64-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Accepted-success?style=for-the-badge)

---

## 📌 Problem

Pete and Billy bought a watermelon weighing **`w` kilograms**.

They want to divide it into **two parts** such that:

* Both parts have a **positive weight**.
* Both parts weigh an **even number of kilograms**.
* The two parts **do not have to be equal**.

Given `w`, determine whether such a division is possible.

Print:

* `YES` if the watermelon can be divided as required.
* `NO` otherwise.

---

## 💡 Examples

### Example 1

**Input:**

```text
8
```

**Output:**

```text
YES
```

**Explanation:**

The watermelon can be divided into:

```text
2 + 6 = 8
```

Both `2` and `6` are positive even numbers.

---

### Example 2

**Input:**

```text
5
```

**Output:**

```text
NO
```

It is impossible to divide `5` into two positive even numbers.

---

## 📋 Constraints

* `1 ≤ w ≤ 100`

---

## 🚀 Approach

The key observation is that the sum of **two even numbers is always even**.

Therefore:

* If `w` is **odd**, the answer is immediately `NO`.
* If `w` is **even**, we still need to make sure both parts are **positive**.

The smallest possible positive even number is `2`.

So we can divide the watermelon as:

```text
2 + (w - 2)
```

For this to work, `w - 2` must also be positive and even.

Therefore, the required condition is:

```text
w is even AND w > 2
```

### Condition

```python
if w > 2 and w % 2 == 0:
    print("YES")
else:
    print("NO")
```

---

## 🔄 Example Walkthrough

For:

```text
w = 8
```

Check whether `8` is greater than `2`:

```text
8 > 2  → True
```

Check whether `8` is even:

```text
8 % 2 == 0  → True
```

Both conditions are satisfied.

Therefore:

```text
YES
```

One valid division is:

```text
2 + 6 = 8
```

---

## 💻 Solution

```python
w = int(input())

if w > 2 and w % 2 == 0:
    print("YES")
else:
    print("NO")
```

---

## 🔍 Code Explanation

### 1. Read the weight

```python
w = int(input())
```

Reads the watermelon weight as an integer.

### 2. Check the conditions

```python
if w > 2 and w % 2 == 0:
```

There are two conditions:

* `w > 2` ensures that after giving one person `2` kg, the other part is still positive.
* `w % 2 == 0` checks whether `w` is even.

### 3. Print the answer

```python
print("YES")
```

If both conditions are true, the watermelon can be divided properly.

Otherwise:

```python
print("NO")
```

---

## ⏱️ Complexity Analysis

| Complexity           | Value  |
| -------------------- | ------ |
| **Time Complexity**  | `O(1)` |
| **Space Complexity** | `O(1)` |

Only a couple of arithmetic operations are performed, regardless of the value of `w`.

---

## 🏆 My Codeforces Result

| Platform   | Problem             | Status     | Language  |    Runtime |   Memory |
| ---------- | ------------------- | ---------- | --------- | ---------: | -------: |
| Codeforces | **4A — Watermelon** | ✅ Accepted | PyPy 3-64 | **186 ms** | **0 KB** |

**Submission:** September 14, 2026 — 22:46 (UTC+5:30)

---

## 🧠 What I Learned

* How to identify a solution from a simple mathematical condition.
* The importance of checking **positivity** in addition to parity.
* Using the modulo operator `%` to check whether a number is even.
* Recognizing when a problem can be solved in constant time.

---

## 🔑 Concepts Used

* 🔢 Even & Odd Numbers
* ➗ Modulo Operator `%`
* 🧠 Mathematical Observation
* 🔀 Conditional Statements
* ⏱️ Constant Time Complexity

---

## 🎯 Key Insight

The entire problem can be reduced to one simple condition:

```text
w > 2 AND w is even
```

Why?

Because every valid solution can be represented as:

```text
2 + (w - 2)
```

where both parts are positive even numbers.

---

## 📚 Problem Link

🔗 [Codeforces 4A — Watermelon](https://codeforces.com/contest/4/problem/A)

🔗 [My Submission](https://codeforces.com/contest/4/submission/390749744)

---



> One problem at a time. One optimization at a time. 🚀
