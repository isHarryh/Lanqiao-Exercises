# 43724 - 摆动序列

![Year: 2020](https://img.shields.io/badge/Year-2020-white)
![Level: Provincial Mock](https://img.shields.io/badge/Level-Provincial%20Mock-blue)
![Python3](https://img.shields.io/badge/Python3-AC-green)

## 题目

### 题目描述

如果一个序列的奇数项都比前一项大，偶数项都比前一项小，则称为一个摆动序列。即 $a_{2i} < a_{2i-1}$ ， $a_{2i+1}\ > a_{2i}$ 。

小明想知道，长度为 $m$ ，每个数都是 $1$ 到 $n$ 之间的正整数的摆动序列一共有多少个。

### 输入描述

输入一行包含两个整数 $m, n\ (1 \leq n, m \leq 1000)$ 。

### 输出描述

输出一个整数，表示答案。答案可能很大，请输出答案除以 $10000$ 的余数。

### 输入输出样例

#### 示例

> 输入

```txt
3 4
```

> 输出

```txt
14
```

## 分析

本题可以通过**递推**的方式解决。

先观察在 $n$ 的值固定的情况下，随着长度 $m$ 的增长，答案值 $A_{nm}$ 如何变化。以 $n=4$ 为例：

- $m=1$ ：一个单独的数无法称为一个序列， $A_{nm}=0$ 。
- $m=2$ ：可以产生如下序列：
  ```txt
  (x1) 4, 3
  (x1) 4, 2
  (x1) 4, 1
  (x1) 3, 2
  (x1) 3, 1
  (x1) 2, 1
  total=6
  ```
  可以发现，当 $m=2$ 时，末尾数字为 $x$ 的序列有 $n-x$ 种。
- $m=3$ ：不难发现，序列的最后一个数字，只取决于先前一个数字，于是可以忽略更早的数字（用 `?` 代替）。可以产生如下序列：
  ```txt
  (x3) ?, 1, 2
  (x3) ?, 1, 3
  (x3) ?, 1, 4
  (x2) ?, 2, 3
  (x2) ?, 2, 4
  (x1) ?, 3, 4
  total=14
  ```

总的来看。在 $m$ 为奇数时，末尾数字为 $x$ 的序列的数量是长度为 $m-1$ 的序列中，末尾数字小于 $x$ 的序列数量；在 $m$ 为偶数时，末尾数字为 $x$ 的序列的数量是长度为 $m-1$ 的序列中，末尾数字大于 $x$ 的序列数量。

于是，只要维护“序列末尾各个数字出现的次数”这个数组，即可进行递推。

> 参考表： $m < 5, n < 5$ 的各种 $m,n$ 组合情况下，序列的总数：
> 
> ```txt
> n\m 1  2  3  4  5  
> 1   0  0  0  0  0  
> 2   0  1  1  1  1  
> 3   0  3  5  8  13 
> 4   0  6  14 31 70 
> 5   0  10 30 85 246
> '''
