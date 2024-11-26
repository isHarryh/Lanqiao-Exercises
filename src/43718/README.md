# 43718 - 反倍数

![Year: 2020](https://img.shields.io/badge/Year-2020-white)
![Level: Provincial Mock](https://img.shields.io/badge/Level-Provincial%20Mock-blue)
![Python3](https://img.shields.io/badge/Python3-AC-green)

## 题目

### 题目描述

给定三个整数 $a, b, c$ ，如果一个整数既不是 $a$ 的整数倍也不是 $b$
的整数倍还不是 $c$ 的整数倍，则这个数称为反倍数。

请问在 1 至 $n$ 中有多少个反倍数。

### 输入描述

输入的第一行包含一个整数 $n$ 。

第二行包含三个整数 $a, b, c$ ，相邻两个数之间用一个空格分隔。

其中， $1 \leq n \leq 1000000，1 \leq a \leq n，1 \leq b \leq n，1 \leq c \leq n$ 。

### 输出描述

输出一行包含一个整数，表示答案。

### 输入输出样例

#### 示例

> 输入

```txt
30
2 3 6
```

> 输出

```txt
10
```

> 样例说明：

以下这些数满足要求：1, 5, 7, 11, 13, 17, 19, 23, 25, 29。

## 分析

本题非常简单，直接暴力枚举即可。
