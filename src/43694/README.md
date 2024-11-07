# 43694 - 正则问题

![Year: 2017](https://img.shields.io/badge/Year-2017-white)
![Level: Provincial](https://img.shields.io/badge/Level-Provincial-blue)
![Python3](https://img.shields.io/badge/Python3-AC-green)

## 题目

### 题目描述

考虑一种简单的正则表达式：

只由 `x()|` 组成的正则表达式。

小明想求出这个正则表达式能接受的最长字符串的长度。

例如 `((xx|xxx)x|(x|xx))xx` 能接受的最长字符串是：`xxxxxx`，长度是 6。

### 输入描述

一个由 `x()|` 组成的正则表达式。输入长度不超过 100，保证合法。

### 输出描述

这个正则表达式能接受的最长字符串的长度。

### 输入输出样例

#### 示例

> 输入

```txt
((xx|xxx)x|(x|xx))xx
```

> 输出

```txt
6
```

## 分析

本题可以使用**栈**来区分括号的嵌套层次，并使用**递归**进行求解。此外，也可以考虑使用**DFS**求解。代码中提供的解法是前者。
