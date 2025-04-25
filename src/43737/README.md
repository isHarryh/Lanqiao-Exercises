# Fibonacci 数列与黄金分割

![Year: Unknown](https://img.shields.io/badge/Year-2019-white)
![Level: Provincial](https://img.shields.io/badge/Level-Provincial-blue)
![Python3](https://img.shields.io/badge/Python3-AC-green)

## 题目

### 题目描述

Fibonacci 数列是非常著名的数列：

$F[1] = 1$,

$F[2] = 1$,

对于 $i > 3，F[i] = F[i−1] + F[i−2]$ 。

Fibonacci 数列有一个特殊的性质，前一项与后一项的比值， $F[N]/F[N + 1]$ ，会趋近于黄金分割。

为了验证这一性质，给定正整数 N，请你计算 $F[N]/F[N + 1]$ ，并保留 8 位小数。

### 输入描述

输入一个正整数 $N\ (1 \leq  N  \leq 2 \times 10^9)$ 。

### 输出描述

输出 $F[N]/F[N + 1]$ 。答案保留 8 位小数。

### 输入输出样例

#### 示例

> 输入

```txt
2
```

> 输出

```txt
0.50000000
```

## 分析

本题直接计算斐波那契数列即可。

本题的输入范围 $2 \times 10^9$ 看似非常巨大，实际上，稍微测试一下就会发现，从 $N = 20$ 开始，答案就固定在了 `0.61803399`。也就是说，在 $N$ 较小的时候精度就已经足够了，不管 $N$ 多么地大，保留 8 位小数的答案始终都是这个数字了。
