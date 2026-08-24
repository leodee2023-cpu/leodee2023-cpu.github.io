---
layout: post
title: "动态规划 Dynamic Programming2"
date: 2026-08-24 14:40:00 +0800
categories: [刷题]
tags: [LeetCode hot-100, 卡码训练营]
---
## 题目
### 46. 携带研究材料（卡码）
小明是一位科学家，他需要参加一场重要的国际科学大会，以展示自己的最新研究成果。他需要带一些研究材料，但是他的行李箱空间有限。这些研究材料包括实验设备、文献资料和实验样本等等，它们各自占据不同的空间，并且具有不同的价值。 

小明的行李空间为 N，问小明应该如何抉择，才能携带最大价值的研究材料，每种研究材料只能选择一次，并且只有选与不选两种选择，不能进行切割。

输入描述:

```
第一行包含两个正整数，第一个整数 M 代表研究材料的种类，第二个正整数 N，代表小明的行李空间。

第二行包含 M 个正整数，代表每种研究材料的所占空间。 

第三行包含 M 个正整数，代表每种研究材料的价值。
```

输出描述：

```
输出一个整数，代表小明能够携带的研究材料的最大价值
```

**示例1：**

输入：
```
6 1
2 2 3 1 5 2
2 3 1 5 4 3
```

输出：
```
5
```
#### 二维数组

**题目分析：** 这是很经典的01背包问题，按照动态规划做题的五部曲，
```
1. dp数组及其下标的含义：这里我们定义二维的dp数组dp[i][j]， 将它定义为从0-i的物品中选取，放入容量为j的背包，所得到的最大价值
2. dp数组的递推公式：
对于dp[i][j],
假设第i个物品的重量weight[i]超过了j 那显然我们有dp[i][j] = dp[i - 1][j]
假设第i个物品的重量小于等于j, 我们就需要考虑两种情况取最大值, 第一种情况是将物品i放入背包中，此时的dp[i][j] = dp[i - 1][j - weight[i]] + value[i]。
第二种情况是将物品i不放入背包中，此时的dp[i][j] = dp[i - 1][j]。
综合一下，我们得到递推公式：

if j < weight[i]:
    dp[i][j] = dp[i - 1][j]
else:
    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])

3. 如何初始化： 这里显然我们知道当j等于0时，dp[i][0]必然全为0，因为无法放入任何物品。
当i等于0时，如果j < weight[0]，那dp[0][j]也全为0 如果j >= weight[0], 那dp[0][j] = value[0]。
另外我们需要知道物品有m个的话 我们i的下标范围应该是0 ~ m - 1, 背包容量为n的话 我们的j的下标范围应该是0 ~ n，所以dp数组的大小为m × (n + 1)
初始化如下：

dp = [[0] * (n + 1) for _ in range(m)]
for j in range(weight[0], n + 1):
    dp[0][j] = value[0]

4. 如何开始遍历： 从i = 1, j = 0开始遍历
5. 举例推导dp数组，dp[0][0] = 0,...
```
**代码如下：**
```python
import sys
def solve(m, n, weight, value):
    #初始化dp数组
    dp = [[0] * (n + 1) for _ in range(m)]
    for j in range(weight[0], n + 1):
        dp[0][j] = value[0]
    for i in range(1, m):
        for j in range(n + 1):
            if j < weight[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])
    return dp[m - 1][n]

if __name__ == "__main__":
    data = list(map(int, sys.stdin.readline().strip().split()))
    weight = list(map(int, sys.stdin.readline().strip().split()))
    value = list(map(int, sys.stdin.readline().strip().split()))
    print(solve(data[0], data[1], weight, value))


```

#### 一维数组

**题目分析：** 在上文二维数组的基础上，我们可以改用一维数组来进行，
```
1. dp数组及其下标的含义：在二维数组时，dp数组dp[i][j]， 将它定义为从0-i的物品中选取，放入容量为j的背包，所得到的最大价值。那么改为一维数组后，dp[j]的定义就是容量为j的背包所得到的最大价值
2. dp数组的递推公式：
对于dp[i][j],
递推公式：

if j < weight[i]:
    dp[i][j] = dp[i - 1][j]
else:
    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])

那么如果我们在初始化的时候先做一个赋值操作，把dp[i - 1]那一层拷贝到dp[i]上, 再让dp[i][j] = max(dp[i][j], dp[i][j - weight[i]] + value[i]) 我们发现，此时我们是没有用到i的，所以可以直接将dp数组从2维降到1维，即dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
所以此时的递推公式是：
dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

3. 如何初始化： 
初始化如下：

dp = [0] * (n + 1)


4. 如何开始遍历： 为了防止重复问题，所以我们对于背包的遍历要采用倒序遍历。为什么二维数组的时候不需要倒序遍历呢，因为二维数组的时候，对于dp[i]这一层的计算都是通过dp[i - 1]来进行的。
遍历如下：
for i in range(m):
    for j in range(n, weight[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
5. 举例推导dp数组，dp[0][0] = 0,...
```

**代码如下：**

```python
import sys
def solve(m, n, weight, value):
    dp = [0] * (n + 1)
    for i in range(m):
        for j in range(n, weight[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
    return dp[n]
if __name__ == "__main__":
    data = list(map(int, sys.stdin.readline().strip().split()))
    weight = list(map(int, sys.stdin.readline().strip().split()))
    value = list(map(int, sys.stdin.readline().strip().split()))
    print(solve(data[0], data[1], weight, value))
```

### 416. 分割等和子集
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

**示例1：**

输入：
```
nums = [1,5,11,5]
```

输出：
```
true
```

**示例2：**

输入：
```
nums = [1,2,3,5]
```

输出：
```
false
```

**题目分析：** 这是一个01背包问题的实际应用，我们假设target就是我们背包的总容量，weight数组与value数组都赋值为nums，这样我们就可以做到，通过dp数组的最大值是否等于target来判断结果是否存在，所以话不多说，直接套用模板即可

**二维数组代码如下：**
```python
import sys
def solve(m, n, weight, value):
    #初始化dp数组
    dp = [[0] * (n + 1) for _ in range(m)]
    for j in range(weight[0], n + 1):
        dp[0][j] = value[0]
    for i in range(1, m):
        for j in range(n + 1):
            if j < weight[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])
    return dp[m - 1][n]

if __name__ == "__main__":
    data = list(map(int, sys.stdin.readline().strip().split()))
    m = len(data)
    if not data or m < 2:
        return False
    target = sum(data)
    if target % 2 != 0:
        return False
    target = target // 2
    n = target
    if solve(m, n, data, data) != target:
        return False
    else:
        return True


```