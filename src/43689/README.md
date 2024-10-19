# 43689 - 包子凑数

![Java11](https://img.shields.io/badge/Java11-AC-green)
![Python3](https://img.shields.io/badge/Python3-AC-green)
![PyPy7](https://img.shields.io/badge/PyPy7-AC-green)

## 题目

### 题目描述

小明几乎每天早晨都会在一家包子铺吃早餐。他发现这家包子铺有 $N$ 种蒸笼，其中第 $i$ 种蒸笼恰好能放 $A_i$ 个包子。每种蒸笼都有非常多笼，可以认为是无限笼。

每当有顾客想买 $X$ 个包子，卖包子的大叔就会迅速选出若干笼包子来，使得这若干笼中恰好一共有 $X$ 个包子。比如一共有 3 种蒸笼，分别能放 3、4 和 5 个包子。当顾客想买 11 个包子时，大叔就会选 2 笼 3 个的再加 1 笼 5 个的（也可能选出 1 笼 3 个的再加 2 笼 4 个的）。

当然有时包子大叔无论如何也凑不出顾客想买的数量。比如一共有 3 种蒸笼，分别能放 4、5 和 6 个包子。而顾客想买 7 个包子时，大叔就凑不出来了。

小明想知道一共有**多少种数目**是包子大叔凑不出来的。

### 输入描述

第一行包含一个整数 $N$ ($1 \leq N \leq 100$)。

以下 $N$ 行每行包含一个整数 $A_i$ ($1 \leq A_i \leq 100$)。

### 输出描述

一个整数代表答案。如果凑不出的数目有无限多个，输出 `INF`。

### 输入输出样例

#### 示例 1

> 输入

```txt
2
4
5
```

> 输出

```txt
6
```

> 样例说明

凑不出的数目包括：1, 2, 3, 6, 7, 11。

#### 示例 2

> 输入

```txt
2
4
6
```

> 输出

```txt
INF
```

> 样例说明

所有奇数都凑不出来，所以有无限多个。

## 分析

本题研究的是某个正整数 $n$ 是否能用一组正整数 $A_i$ 的非负整数**线性组合**来表示，可以用**动态规划**求解。

设布尔数组 $dp$ 在当正整数 $n$ 能被 $A_i$ 线性表示时，元素 $dp_n$ 为真。易知，元素 $dp_0$ 初始为真，因为零总是可以被线性表示（$0=\sum{0A_i}$）。

接下来考虑 $i=1,2,\cdots,n$ 的情况（其中 $n$ 是一个足够大的整数）。如果现在可以在 $dp$ 中找到一个元素 $dp_j$，在 $A$ 中找到一个元素 $A_k$，满足 $dp_j$ 为真且 $dp_j + A_k = i$，那么 $i$ 就可以被 $A_i$ 的某种线性组合表示（此时将 $dp_i$ 赋值为真）。

结束遍历后，输出 $dp$ 数组内的非真值的数量。

> 也可以不使用布尔数组，而是用集合来实现：集合中存储可以被线性表示的数，此时“$dp_j$ 为真”的判据改成“数 $j$ 是否在集合内”的判据即可。

另外，容易发现，当这组正整数 $A_i$ 的最大公约数（GCD）不为 $1$ 时，不能被 $A_i$ 线性表示的正整数的数量是无限的。