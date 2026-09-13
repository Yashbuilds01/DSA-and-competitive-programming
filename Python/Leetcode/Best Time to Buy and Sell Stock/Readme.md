# 🧩 Best Time to Buy and Sell Stock (Problem-121)

> **LeetCode; #121 — Easy**

[![LeetCode](https://img.shields.io/badge/LeetCode-121-orange?style=for-the-badge\&logo=leetcode)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
[![Language](https://img.shields.io/badge/Language-Python%203-blue?style=for-the-badge\&logo=python)](https://www.python.org/)
[![Accepted](https://img.shields.io/badge/Status-Accepted-success?style=for-the-badge)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

---

## 📌 Problem

You are given an array `prices` where `prices[i]` represents the price of a stock on the `ith` day.

You want to maximize your profit by:

* Choosing **one day to buy** the stock.
* Choosing a **different day in the future to sell** the stock.

Return the **maximum profit** you can achieve from this transaction.

If no profitable transaction is possible, return `0`.

> **Important:** You must buy the stock **before** you sell it.

---

## 💡 Examples

### Example 1

**Input:**

```text
prices = [7,1,5,3,6,4]
```

**Output:**

```text
5
```

**Explanation:**

The best transaction is:

```text
Buy  → Day 2 → Price = 1
Sell → Day 5 → Price = 6
```

Profit:

```text
6 - 1 = 5
```

Therefore, the maximum profit is `5`.

---

### Example 2

**Input:**

```text
prices = [7,6,4,3,1]
```

**Output:**

```text
0
```

**Explanation:**

The stock price continuously decreases.

There is no possible transaction that produces a profit, so the maximum profit is `0`.

---

## 📋 Constraints

* `1 <= prices.length <= 10⁵`
* `0 <= prices[i] <= 10⁴`

---

## 🚀 Approach

The key idea is to keep track of the **lowest price seen so far**.

As we traverse the array:

1. Keep track of the minimum price at which we could have bought the stock.
2. For each current price, calculate the profit if we sell on that day.
3. Update the maximum profit whenever we find a better one.
4. Continue until the end of the array.

### 🔹 Key Idea

For every price:

```text
Potential Profit = Current Price - Minimum Price
```

We only consider prices that appeared **before** the current price, ensuring that the buying day always comes before the selling day.

---

## 🔄 Example

For:

```text
prices = [7,1,5,3,6,4]
```

We can track the minimum price and maximum profit:

| Day | Price | Minimum Price | Potential Profit | Maximum Profit |
| --: | ----: | ------------: | ---------------: | -------------: |
|   1 |     7 |             7 |                0 |              0 |
|   2 |     1 |             1 |                0 |              0 |
|   3 |     5 |             1 |                4 |              4 |
|   4 |     3 |             1 |                2 |              4 |
|   5 |     6 |             1 |                5 |              5 |
|   6 |     4 |             1 |                3 |              5 |

The maximum profit is:

```text
5
```

The transaction is:

```text
Buy at 1 → Sell at 6
Profit = 6 - 1 = 5
```


---

## 🔍 Code Explanation

### 1. Track the Minimum Price

```python
min_price = prices["inf"]
```

We initially take infinity as  min_price value .

---

### 2. Track Maximum Profit

```python
max_profit = 0
```

If no profitable transaction exists, the answer should remain `0`.

---

### 3. Traverse the Prices

```python
for i in prices:
```

We examine each day's stock price exactly once.

---

### 4. Update the Minimum Price

```python
if i < min_price:
    min_price = i
```

Whenever we find a lower price, we update our best possible buying price.

---

### 5. Calculate Potential Profit

```python
profit = i - min_price
```

This represents the profit we would make if we bought at the lowest price seen so far and sold today.

---

### 6. Update Maximum Profit

```python
if profit > max_profit:
    max_profit = profit
```

If the current transaction produces a better profit, we save it.

---

### 7. Return the Answer

```python
return max_profit
```

After checking every possible selling day, `max_profit` contains the best profit possible.

---

## ⏱️ Complexity Analysis

Let `n` be the number of days.

### Time Complexity

```text
O(n)
```

We traverse the array only once.

### Space Complexity

```text
O(1)
```

We use only two variables regardless of the input size.

| Complexity | Value    |
| ---------- | -------- |
| ⏱️ Time    | **O(n)** |
| 💾 Space   | **O(1)** |

---

## 🏆 My LeetCode Result

**Status:** ✅ Accepted

```text
213 / 213 test cases passed
```

### ⚡ Performance

```text
Runtime: 31 ms
Beats: 84.77%

Memory: 28.68 MB
Beats: 42.21%
```

| Metric             | Result           |
| ------------------ | ---------------- |
| 🟢 Status          | **Accepted**     |
| 🧪 Test Cases      | **213 / 213**    |
| ⚡ Runtime          | **31 ms**        |
| 🏆 Runtime Ranking | **Beats 84.77%** |
| 💾 Memory          | **28.68 MB**     |
| 📊 Memory Ranking  | **Beats 42.21%** |
| 🐍 Language        | **Python 3**     |

---

## 🧠 What I Learned

This problem demonstrates an important **one-pass optimization technique**.

Instead of checking every possible pair of buying and selling days, we keep track of the **minimum price seen so far** and calculate the best possible profit at every step.

The key idea is:

> **Buy at the lowest price seen so far and check the maximum profit possible at each future price.**

This reduces the brute-force approach from:

```text
O(n²) → O(n)
```

while using only constant extra space.

---

## 🔑 Concepts Used

* Arrays
* Greedy Approach
* One-pass Traversal
* Minimum Value Tracking
* Maximum Value Tracking
* Profit Calculation
* Time & Space Complexity
* Optimization

---

## 🎯 Follow-Up

### Can you solve this problem in `O(n)` time?

Yes.

The current solution already achieves:

```text
O(n) time
O(1) space
```

The important optimization is avoiding comparisons between every possible pair of days.

Instead, we only need to remember the **lowest buying price so far**.

---

## 📚 Problem Link

🔗 [LeetCode — Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

---




> One problem at a time. One optimization at a time. 🚀
