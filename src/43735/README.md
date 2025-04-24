# 43735 - 人物相关性分析

![Year: 2019](https://img.shields.io/badge/Year-2019-white)
![Level: Provincial](https://img.shields.io/badge/Level-Provincial-blue)
![Python3](https://img.shields.io/badge/Python3-AC-green)

## 题目

### 题目描述

小明正在分析一本小说中的人物相关性。他想知道在小说中 Alice 和 Bob 有多少次同时出现。

更准确的说，小明定义 Alice 和 Bob “同时出现” 的意思是：在小说文本 中 Alice 和 Bob 之间不超过 $K$ 个字符。

例如以下文本：

This is a story about Alice and Bob.Alice wants to send a private message to Bob.

假设 $K$ = 20，则 Alice 和 Bob 同时出现了 2 次，分别是 "Alice and Bob" 和 "Bob. Alice"。前者 Alice 和 Bob 之间有 5 个字符，后者有 2 个字符。

注意：

1. Alice 和 Bob 是大小写敏感的，alice 或 bob 等并不计算在内。
2. Alice 和 Bob 应为单独的单词，前后可以有标点符号和空格，但是不能有字母。例如出现了 Bobbi 并不算出现了 Bob。

### 输入描述

第一行包含一个整数 $K（1  \leq  K  \leq  10^6） $ 。

第二行包含一行字符串，只包含大小写字母、标点符号和空格。长度不超过 $10^6$ 。

### 输出描述

输出一个整数，表示 Alice 和 Bob 同时出现的次数。

### 输入输出样例

#### 示例

> 输入

```txt
20
This is a story about Alice and Bob.Alice wants to send a private message to Bob.
```

> 输出

```txt
2
```

## 分析

本题直接对字符串进行遍历即可。

需要注意，如果 Alice 已经在前面出现了多次，现在出现一个 Bob，那么前面的这些 Alice 的出现都可能需要计入计数。如果题目所给的 $K$ 非常大的话，是可能导致超时的。为此，我们需要引入一个队列机制。

维护 `index_of_name1` 和 `index_of_name2` 两个 FIFO 队列。如果单词 Alice（或 Bob）出现了：

- 首先，将当前的位置索引加入到自己的队列的末尾。
- 然后，从头部开始遍历对方的队列，进行“清理”。每当遇到一个索引，如果这个索引距离不在容许范围内（距离太远），就将这个索引弹出队列。如果遇到的索引在容许范围内，则说明后续的索引都在容许范围内，结束遍历。
- 最后，将对方的队列的长度添加到计数器中。

这样就可以高效地进行统计了。需要特别注意处理字符串结尾的情况，建议将字符串末尾加上一个非字母的字符，来确保字符串结尾能够被正常地统计。
