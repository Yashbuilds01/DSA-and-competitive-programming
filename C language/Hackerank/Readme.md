# 🔄 For Loop in C

> **HackerRank — C Language**
> **Topic: For Loop**

[![HackerRank](https://img.shields.io/badge/HackerRank-For%20Loop%20in%20C-2EC866?style=for-the-badge\&logo=hackerrank\&logoColor=white)](https://www.hackerrank.com/challenges/for-loop-in-c/problem)
[![Language](https://img.shields.io/badge/Language-C-blue?style=for-the-badge\&logo=c)](https://www.hackerrank.com/domains/c)
[![Status](https://img.shields.io/badge/Status-Solved-success?style=for-the-badge)](https://www.hackerrank.com/challenges/for-loop-in-c/submissions)

---

## 📌 Problem

This problem introduces the **`for` loop** in C.

Given two integers `a` and `b`, print the appropriate output for every integer in the inclusive range:

```text
[a, b]
```

For each number:

* If the number is between **1 and 9**, print its English representation in lowercase.
* If the number is greater than `9` and even, print **`even`**.
* If the number is greater than `9` and odd, print **`odd`**.

---

## 🎯 Objective

The main objective of this challenge is to understand how a **`for` loop** works in C.

The general syntax of a `for` loop is:

```text
for (initialization; condition; update)
    statement;
```

The three parts are:

| Part               | Purpose                                        |
| ------------------ | ---------------------------------------------- |
| **Initialization** | Sets the starting value                        |
| **Condition**      | Determines whether the loop continues          |
| **Update**         | Changes the loop variable after each iteration |

For example, a loop that executes 10 times can be represented as:

```text
for (int i = 0; i < 10; i++)
```

---

## 💡 Task

For every integer in the given range:

### If the number is between 1 and 9

Print its English representation:

| Number | Output  |
| -----: | ------- |
|      1 | `one`   |
|      2 | `two`   |
|      3 | `three` |
|      4 | `four`  |
|      5 | `five`  |
|      6 | `six`   |
|      7 | `seven` |
|      8 | `eight` |
|      9 | `nine`  |

### If the number is greater than 9

* Even number → `even`
* Odd number → `odd`

---

## 📥 Input Format

The input contains two integers:

```text
a
b
```

The range includes both `a` and `b`.

---

## 📤 Output Format

For every integer from `a` to `b`, print:

* Its English representation if it is between `1` and `9`.
* `even` if it is greater than `9` and even.
* `odd` if it is greater than `9` and odd.

Each result should be printed on a separate line.

---

## 🧪 Example

### Sample Input

```text
8
11
```

### Sample Output

```text
eight
nine
even
odd
```

### Explanation

The numbers in the range are:

```text
8  → eight
9  → nine
10 → even
11 → odd
```

---

## 🚀 Approach

The solution uses a **`for` loop** to iterate from the first input number to the second input number.

For every number:

1. Check whether it is between `1` and `9`.
2. If so, use a `switch` statement to print its English representation.
3. Otherwise, determine whether the number is even or odd using the modulo operator `%`.
4. Print the corresponding result.

### 🔹 Important Concepts

**For Loop**

Used to process every number in the given range.

**Switch Statement**

Used to map numbers `1` through `9` to their English representations.

**Modulo Operator**

The expression:

```text
number % 2
```

is used to determine whether a number is even or odd.

* Remainder `0` → Even
* Remainder `1` or `-1` → Odd

---

## ⏱️ Complexity Analysis

Let `n` represent the number of integers in the given range.

### Time Complexity

```text
O(n)
```

Each number in the range is processed exactly once.

### Space Complexity

```text
O(1)
```

Only a constant amount of extra memory is used.

| Complexity | Value    |
| ---------- | -------- |
| ⏱️ Time    | **O(n)** |
| 💾 Space   | **O(1)** |

---

## 🧠 What I Learned

This problem helped reinforce the fundamentals of **loops and conditional logic in C**.

Key takeaways:

* How to use a `for` loop.
* How to control the starting and ending conditions of a loop.
* How to use a `switch` statement.
* How to use `%` to check whether a number is even or odd.
* How to combine loops with conditional statements.
* How to process a range of integers.

---

## 🔑 Concepts Used

* `for` Loop
* `switch` Statement
* `if / else if`
* Modulo Operator `%`
* Integer Input
* Range Iteration
* Conditional Logic
* C Programming Fundamentals

---

## 🏆 HackerRank Progress

**Platform:** HackerRank

**Language:** C

**Problem:** For Loop in C

**Status:** ✅ Solved

**Current Rank:** `1,023,840`

**Points:** `10 / 15`

**Progress to First Star:** `5 more points`

---

## 📚 Problem Links

🔗 [HackerRank — For Loop in C](https://www.hackerrank.com/challenges/for-loop-in-c/problem)

🔗 [My Submissions](https://www.hackerrank.com/challenges/for-loop-in-c/submissions)

🔗 [Leaderboard](https://www.hackerrank.com/challenges/for-loop-in-c/leaderboard)

🔗 [Discussions](https://www.hackerrank.com/challenges/for-loop-in-c/forum)

🔗 [Editorial](https://www.hackerrank.com/challenges/for-loop-in-c/editorial)

---

## ⭐ Progress

**HackerRank C Problems Solved:** `1`

**Current Topic:** `For Loop`

> Learn the fundamentals. Solve the problems. Build the logic. 🚀
