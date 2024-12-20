# 43699 - 四平方和

![Year: 2016](https://img.shields.io/badge/Year-2016-white)
![Level: Provincial](https://img.shields.io/badge/Level-Provincial-blue)
![Python3](https://img.shields.io/badge/Python3-AC-green)

## 题目

### 题目描述

四平方和定理，又称为拉格朗日定理：

每个正整数都可以表示为至多 4 个正整数的平方和。

如果把 0 包括进去，就正好可以表示为 4 个数的平方和。

比如：

$5 = 0^2 + 0^2 + 1^2 + 2^2$ ；

$7 = 1^2 + 1^2 + 1^2 + 2^2$ ；

对于一个给定的正整数，可能存在多种平方和的表示法。

要求你对 4 个数排序：

$0 \leq a \leq b \leq c \leq d$

并对所有的可能表示法按 $a,b,c,d$ 为联合主键升序排列，最后输出第一个表示法。

### 输入描述

程序输入为一个正整数 $N (N<5 \times 10^6)$ 。

### 输出描述

要求输出 4 个非负整数，按从小到大排序，中间用空格分开。

### 输入输出样例

#### 示例

> 输入

```txt
12
```

> 输出

```txt
0 2 2 2
```

## 分析

本题采用**枚举法**即可实现。

由于 $N = a^2 + b^2 + c^2 + d^2$ ，故必然满足 $a,b,c,d \leq \sqrt{N}$ 。根据题目对四个数大小的要求，可知 $a,b,c,d$ 的枚举范围是 $0 \leq a \leq b \leq c \leq d \leq \sqrt{N}$ 。然后，对 $a,b,c,d$ 依次从小到大枚举，即可得到第一组解。

在 $N$ 较小时，直接对四个数进行枚举是可控的。但是，当 $N$ 较大时，枚举可能需要极长时间。

对直接枚举法的时间复杂度进行分析：枚举阶段嵌套有 4 层上界为 $\sqrt{N}$ 的循环，时间消耗为 $T(N) = \sum^{\sqrt{N}}_{a=0}\sum^{\sqrt{N}}_{b=a}\sum^{\sqrt{N}}_{c=b}\sum^{\sqrt{N}}_{d=c}1$ ，故时间复杂度为 $O((\sqrt{N})^4) = O(N^2)$ 。

为了优化算法，我们可以将 $c,d$ 两个数的所有可能的平方和结果 $c^2 + d^2$ 作为键、最小顺序组合 $c,d$ 作为值存储到哈希表中。然后，枚举 $a,b$ 两个数的所有可能的平方和结果 $a^2 + b^2$ ，计算 $\Delta = N - (a^2 + b^2)$ 的值，在哈希表中尝试检索 $\Delta$ 对应的组合 $c,d$ 是否存在。如果存在，那么 $a,b,c,d$ 就是所求的第一组解。

对优化后的算法的时间复杂度进行分析：建表阶段有 2 层上界为 $\sqrt{N}$ 的循环，局部时间复杂度是 $O((\sqrt{N})^2) = O(N)$ 。枚举阶段也有 2 层上界为 $\sqrt{N}$ 的循环，局部时间复杂度也是 $O(N)$ 。因此，整体时间复杂度是 $O(N)$ 。
