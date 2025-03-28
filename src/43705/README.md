# 43705 - 垒骰子

![Year: 2015](https://img.shields.io/badge/Year-2015-white)
![Level: Provincial](https://img.shields.io/badge/Level-Provincial-blue)
![C++](https://img.shields.io/badge/C++-AC-green)
![Python3](https://img.shields.io/badge/Python3-AC-green)

## 题目

### 题目描述

赌圣 atm 晚年迷恋上了垒骰子，就是把骰子一个垒在另一个上边，不能歪歪扭扭，要垒成方柱体。

经过长期观察，atm 发现了稳定骰子的奥秘：有些数字的面贴着会互相排斥！

我们先来规范一下骰子：1 的对面是 4，2 的对面是 5，3 的对面是 6。

假设有 $m$ 组互斥现象，每组中的那两个数字的面紧贴在一起，骰子就不能稳定的垒起来。

atm 想计算一下有多少种不同的可能的垒骰子方式。

两种垒骰子方式相同，当且仅当这两种方式中对应高度的骰子的对应数字的朝向都相同。

由于方案数可能过多，请输出模 $10^9 + 7$ 的结果。

不要小看了 atm 的骰子数量哦～

### 输入描述

输入第一行两个整数 $n,m$ ， $n$ 表示骰子数目；

接下来 $m$ 行，每行两个整数 $a,b$ ，表示 $a$ 和 $b$ 数字不能紧贴在一起。

其中， $0 < n   \leq   10^9, m   \leq   36$ 。

### 输出描述

输出一行一个数，表示答案模 $10^9+7$ 的结果。

### 输入输出样例

#### 示例

> 输入

```txt
2 1
1 2
```

> 输出

```txt
544
```

## 分析

本题是有约束的排列组合问题。一般地，可以使用**动态规划**解决。如果运用一些线性代数的知识，那么可以使用**矩阵快速幂**来极大幅度地提升速度。

先看看题目的输出示例的 $544$ 是怎么得来的吧： $n=2$ ，限制 1 和 2 不能相对。我们可以先确定第一层的顶面情况，一共有 6 种。再考虑第二层的底面情况，当第一层顶面不是 1 或 2 时，可以有 6 种，反之只有 5 种。因此，第一层和第二层衔接处的情况数是 $4 \times 6 + 2 \times 5 = 34$ 种，我们叫它“顶面总可能数”。又因为骰子可以在水平面上 $90 \degree$ 地旋转 4 次，使之侧面发生变化，所以在 $n=2$ 的情况下，侧面的情况数是 $4^2=16$ 种，我们叫它“侧面总可能数”。最后， $34 \times 16 = 544$ 种。

看起来有点复杂，实际上也确实有点复杂，我们一步步来。

首先，将骰面 1\~6 重新编号为 0\~5，建立一个合法转移表 `transit`。如果顶面是 a 的骰子可以堆叠顶面是 b 的骰子，那么 `transit[a][b]` 的值为真，否则为假。

### 动态规划方法

可以考虑建立一个有 6 个元素的数组 `dp`，其初始元素均为 1。`dp[i]` 表示当前楼层的顶面是 `i` 号骰面时，可以产生的顶面总可能数。

记合法转移表 `transit` 为矩阵 $T$ ，那么 `transit[i][j]` 指的就是矩阵的元素 $t_{ji}$ 。假设楼上的顶面总可能数的数组为 `dp'`，那么状态转移方程是：

```math
dp'_i = \sum_{j=0}^5 dp_j t_{ji}
```

最后，生成第 $n$ 楼的顶面总可能数，并将其求和，再乘以 $4^n$ 即可得到最终答案。

上述算法的时间复杂度是 $O(n)$ 。实验证明，当 $n \approx 10^9$ 时，Python 需要数分钟得出结果，C++ 也需要近十秒才能得出结果，性能不是很理想。

此外，在运算过程中，要记得将结果取模。在做幂运算的时候，要采用快速幂算法。

> **快速幂：**
>
> 要想求解某个整数的整数次幂的某个模 $a^b \mod c$ 时，如果直接将 $a$ 连续乘以 $b$ 次，那么消耗的时间与 $b$ 成线性函数。此时可以采用快速幂算法。
>
> 注意到整数 $b$ 可以写成如下二进制形式：
> ```math
> b = b_0 2^0 + b_1 2^1 + \cdots + b_{k-1} 2^{k-1} + b_k 2^k
> ```
>
> 根据幂运算的性质，可以对 $a^b$ 作如下拆分：
> ```math
> a^b = a^{b_0 2^0 + b_1 2^1 + \cdots + b_{k-1} 2^{k-1} + b_k 2^k} = a^{b_0 2^0} \times a^{b_1 2^1} \times \cdots \times a^{b_{k-1} 2^{k-1}} \times a^{b_k 2^k}
> ```
>
> 因此可以这样计算 $a^b \mod c$ ：
>
> 1. 初始令结果变量 $r=1$ 。
> 2. 如果 $b$ 的末位二进制位是 1，那么令 $r = (r \times a) \mod c$ 。同时，令 $a = a^2$ ，令 $b = [\frac{b}{2}]$ （右移一位）。
> 3. 如果到最后，满足 $b = 0$ ，则表明计算完毕， $r$ 的值就是最终结果，否则回到第 2 步继续计算。

### 矩阵快速幂方法

我们可以研究一下前文的状态转移方程。假设 `dp` 是行向量，那么原式可以写成矩阵乘法的形式：

```math
dp'_i = \sum_{j=0}^5 dp_j t_{ji} = dpT^T
```

当状态转移结束时，不难发现，最终的结果是 $dp(T^T)^{n-1} = dp(T^{n-1})^T$ 。此时，我们就可以使用矩阵快速幂算法，快速地求解出 $T^{n-1}$ ，然后再将其转置，并左乘 `dp`。

上述算法的时间复杂度是 $O(logn)$ 。实验证明，这时 Python 都能够在 20ms 内给出解答了。

> **矩阵快速幂：**
>
> 类似于整数的快速幂算法，我们可以这样计算 $A^b \mod c$ ：
>
> 1. 初始令结果矩阵 $R=I$ ，其中 $I$ 是单位矩阵。
> 2. 如果 $b$ 的末位二进制位是 1，那么令 $R = (RA) \mod c$ 即 $r_{ij} = \sum (r_{ik}a_{kj} \mod c)$ 。同时，令 $A = A^2$ ，令 $b = [\frac{b}{2}]$ （右移一位）。
> 3. 如果到最后，满足 $b = 0$ ，则表明计算完毕， $R$ 的值就是最终结果，否则回到第 2 步继续计算。
