# 43723 最长递增

![Year: 2020](https://img.shields.io/badge/Year-2020-white)
![Level: Provincial Mock](https://img.shields.io/badge/Level-Provincial%20Mock-blue)
![Python3](https://img.shields.io/badge/Python3-AC-green)

## 题目

### 题目描述

在数列 $a_1, a_2, \cdots, a_n$ 中，如果 $a_i < a_{i+1} < a_{i+2} < \cdots < a_j$，则称 $a_i$ 至 $a_j$ 为一段递增序列，长度为
$j-i+1$。

给定一个数列，请问数列中最长的递增序列有多长。

### 输入描述

输入的第一行包含一个整数 $n$。

第二行包含 $n$ 个整数 $a_1, a_2, \cdots, a_n$，相邻的整数间用空格分隔，表示给定的数列。

其中， $2 \leq n \leq 1000$ ， $0 \leq 数列中的数 \leq 10^4$。

### 输出描述

输出一行包含一个整数，表示答案。

### 输入输出样例

#### 示例

> 输入

```txt
7
5 2 4 1 3 7 2
```

> 输出

```txt
3
```

## 分析

本题非常简单，可以使用**贪心算法**来跟踪当前递增子序列的长度，时间复杂度是 $o(n)$。
