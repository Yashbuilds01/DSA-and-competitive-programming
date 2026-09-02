# 📱 Sara's Phone

## 📝 Problem

Sara's phone has `N` apps, and each app takes `K` units of memory.

Sara wants to release `M` units of memory. Your task is to determine the **minimum number of apps** Sara needs to delete.

If it is not possible to release `M` units of memory by deleting the available apps, return `-1`.

## 📥 Input

### User Task

Since this is a **functional problem**, you do not have to take input.

You only need to complete the function `Phone()` that takes three integers `N`, `K`, and `M` as arguments.

- `N` — Number of apps on the phone.
- `K` — Memory used by each app.
- `M` — Memory Sara wants to release.

## 📌 Constraints

- `1 <= N <= 1000`
- `1 <= K <= 100`
- `0 <= M <= 10000`

## 📤 Output

Return the **minimum number of apps** Sara needs to delete.

If it is not possible to release `M` units of memory, return `-1`.

## 💡 Examples

### Sample 1

**Input:**
```text
10 3 10
```

**Output:**
```text
4
```