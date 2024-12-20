# 43717 - 晚会节目单

![Year: 2020](https://img.shields.io/badge/Year-2020-white)
![Level: Provincial Mock](https://img.shields.io/badge/Level-Provincial%20Mock-blue)
![Python3](https://img.shields.io/badge/Python3-AC-green)

## 题目

### 题目描述

小明要组织一台晚会，总共准备了 $n$ 个节目。然后晚会的时间有限，他只能最终选择其中的 $m$ 个节目。

这 $n$ 个节目是按照小明设想的顺序给定的，顺序不能改变。

小明发现，观众对于晚上的喜欢程度与前几个节目的好看程度有非常大的关系，他希望选出的第一个节目尽可能好看，在此前提下希望第二个节目尽可能好看，依次类推。

小明给每个节目定义了一个好看值，请你帮助小明选择出 $m$ 个节目，满足他的要求。

### 输入描述

输入的第一行包含两个整数 $n, m$ ，表示节目的数量和要选择的数量。

第二行包含 $n$ 个整数，依次为每个节目的好看值。

其中， $1 \leq n \leq 10^5$ ， $0 \leq 节目的好看值 \leq 10^5$ 。

### 输出描述

输出一行包含 $m$ 个整数，为选出的节目的好看值。

### 输入输出样例

#### 示例

> 输入

```txt
5 3
3 1 2 5 4
```

> 输出

```txt
3 5 4
```

> 样例说明

选择了第 1, 4, 5 个节目。

## 分析

本题需要求解具有最大字典序的子序列。下面提供两种方法。

### 简历都看一遍（选择法）

我们想求解具有最大字典序的子序列 $\{S_m\}$ ，最直接的思路就是从主序列 $\{A_n\}$ 中选取元素依次得到 $\{S_m\}$ $S_1,S_2,\cdots,S_m$ 。步骤如下：

1. 先对 $\{A_n\}$ 内的元素进行降序（从大到小）排列，得到 $\{A'_n\}$ 。
2. 遍历 $\{A'_n\}$ 中的元素 $A'_j$ ，记其在主序列中的原始索引是 $i$ 。确保 $i$ 严格大于目前子序列的末尾元素的原始索引。这样一来，可以保证选取的元素遵循主序列的原始顺序，并且选取的元素的价值是目前最大的（因为 $\{A'_n\}$ 已经降序排列）。
3. 尝试把 $A'_j$ 放进子序列 $\{S_m\}$ 末尾，如果此时主序列尾部剩余的元素数量不足以让 $\{S_m\}$ 填满（即不满足 $n - i \geq m - S_m 的当前长度 $ ），则说明该元素暂时无法放进子序列中（即使该元素的价值很大，但是该元素的原始索引太靠后了），此时回到第 2 步选取下一个 $\{A'_n\}$ 中的元素。
4. 成功放进子序列的末尾后，将该元素从 $\{A'_n\}$ 中移除，并回到第 2 步，继续选取元素来填充子序列。

上述算法的时间复杂度是 $O(n+(n+1)+\cdots+(n-m+1))=O(mn)$ 。

### 干不了就滚蛋（淘汰法）

第一种方法每一次选取元素时还需要对 $\{A'_n\}$ 进行遍历，虽然能够一次性地确定子序列中的每个元素，但非常繁琐。不妨利用堆栈思想，进化式地生成子序列。步骤如下：

1. 直接遍历 $\{A_n\}$ 中的每一个元素 $A_i$ 。这样一来，天然地满足选取的元素遵循主序列的原始顺序。
2. 如果子序列 $\{S_m\}$ 的末尾元素 $S_k$ 的价值小于 $A_i$ ，并且抛弃 $S_k$ 的话 $\{S_m\}$ 仍能填满（满足 $n - i \geq m - S_m 的当前长度 - 1$ ，或者说 $n - i > m - S_m 的当前长度 $ ），那么将 $S_k$ 抛弃（从而让后面价值更高的元素来代替它）。
3. 将 $A_i$ 加入到子序列 $\{S_m\}$ 的末尾。重复上述过程，直到填满整个子序列。

上述算法的时间复杂度是 $O(n)$ 。和第一种方法相比，它的时间消耗与 $m$ 解耦了，因此性能上显著更优。
