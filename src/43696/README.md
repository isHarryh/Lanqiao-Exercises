# 43696 - 小数第n位

![Python3](https://img.shields.io/badge/Python3-AC-green)

## 题目

### 题目描述

我们知道，整数做除法时，有时得到有限小数，有时得到无限循环小数。

如果我们把有限小数的末尾加上无限多个 0，它们就有了统一的形式。

本题的任务是：在上面的约定下，求整数除法小数点后的第 $n$ 位开始的 3 位数。

### 输入描述

输入一行三个整数：$a\ b\ n$，用空格分开。$a$ 是被除数，$b$ 是除数，$n$ 是所求的小数后位置（$0<a,b,n<10^9$）

### 输出描述

输出一行 3 位数字，表示：$a$ 除以 $b$，小数后第 $n$ 位开始的 3 位数字。

### 输入输出样例

#### 示例

> 输入

```txt
1 8 1
```

> 输出

```txt
125
```

## 分析

本题需要处理**极大位数的除法**（有效位数达 $10^9$），显然不适合直接计算，使用**长除法**可以显著降低时间和空间的消耗。

长除法就是我们在小学学过的用来手算除法的计算工具，它通过不断对被除数做带余除法来逐位地计算商。

解决本题的算法逻辑如下：

1. 对于被除数 $a$ 和除数 $b$，首先令 $a_0 = a \% b$ 来抹除商的整数部分，此时 $a_0 \leq b$。
2. 接下来规定自然数 $k$ 表示“后续做了多少次除法”，当 $k < n - 1$ 时，循环执行：对于被除数 $a_k$，令 $a_{k+1} = (a_k \times 10) \% b$ 作为下一次除法的被除数。
3. 经过上述操作后，$k = n$ 成立。此时 $(a_k \times 10^3) \% b$ 就是所求的“小数第 $n$ 位开始的 3 位数字”的值。

为了加快 (2) 所描述的过程，我们可以不去“一位一位地”运算，而是用“很多位”一起**批量运算**。具体而言，改进如下：

- 先做批量的长除法：假设“很多位” $d = 10000$，那么当 $k < n - d$ 时，循环执行：对于被除数 $a_k$，令 $a_{k+1} = (a_k \times 10^d) \% b$ 作为下一次除法的被除数。
- 再做单步的长除法：经过上述操作后，$n - d \leq k < n$ 成立，此时再“一位一位地”运算，直到逼近 $k = n$。