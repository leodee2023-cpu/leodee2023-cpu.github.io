---
layout: post
title: "动态规划 Dynamic Programming3"
date: 2026-08-26 14:40:00 +0800
categories: [刷题]
tags: [LeetCode hot-100, 卡码训练营]
---

## 题目
### 1049. 最后一块石头的重量
有一堆石头，用整数数组 stones 表示。其中 stones[i] 表示第 i 块石头的重量。

每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块 石头。返回此石头 最小的可能重量 。如果没有石头剩下，就返回 0。




**示例1：**

输入：
```
2,7,4,1,8,1
```

输出：
```
1
```

**题目分析：** 我们之前做过了一道416. 分割等和子集，这道题其实就是它的一个变种，我们可以将stones分成两个和尽量接近的子集stones1和stones2，

那么abs(sum(stones1) - sum(stones2))就是我们要求的结果。我比较习惯用二维dp数组来求解，比较容易理解，我们令背包的最大容量为target = sum(stones) // 2，

然后求sum(stones) - 2 * dp[len(stones) - 1][-1]即可.

**代码如下：**
```python
import sys
def solve(data):
    total = sum(data)
    target = total // 2
    m = len(data)
    n = target
    weight = data
    value = data
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
    return total - dp[m - 1][n] * 2

if __name__ == "__main__":
    data = list(map(int, sys.stdin.readline().strip().split()))
    print(solve(data))


```

### 494. 目标和

给你一个非负整数数组 nums 和一个整数 target 。

向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：

例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。

**示例1：**

输入：
```
1,1,1,1,1
3
```

输出：
```
5
```

解释：

```
一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
```

**题目分析：**

这道题和上一道题也是类似的解法，但是比较难想。
首先，如果存在某种方法让nums计算得到target的话，我们假设存在一个被减数数组a，一个减数数组b，那显然我们有：


sum(a) - sum(b) = target

sum(a) + sum(b) = sum(nums)


可以得到

 sum(a) = (target + sum(nums)) / 2

也就是说，如果存在一个

sum(a) = (target + sum(nums)) / 2 

这道题才能有解。

有了这个前提之后，这个问题就变成了有多少种a数组，它的和等于(target + sum(nums)) / 2，下面我们按照动态规划的五部曲进行分析
```
1. 确定dp数组的下标和含义： 这里我们定义dp[i][j]的含义为，从0 - i 中选择元素，填满容量为j的背包，有多少种填法

2. 确定递推公式： 显然，如果nums[i] > j的话，那么nums[i]就无法放入背包中，dp[i][j] = dp[i - 1][j]

如果nums[i] <= j的话，

nums[i]可以放入背包中，此时就面临着是否要放入背包中的选择，如果nums[i]不放入背包，那显然就有dp[i - 1][j]

种方法填满背包

如果nums[i]放入背包，那就有dp[i - 1][j - nums[i]]种

因此，当nums[i] <= j 的时候，一共有dp[i - 1][j] + dp[i - 1][j - nums[i]]种

3.初始化：当j = 0时比较特殊，不是像之前一样dp[i][0] = 0,因为如果nums中有0元素那还是可以填满的，而且什么都不放也可以视为填满，

假设0 - i 种有zeronums个0，那dp[i][0] = 2 ** zeronums

当i = 0时，如果j == nums[0]，dp[0][j] = 1， 否则dp[0][j]就等于0(j > 0)

```

代码如下：
```python
import sys

def solve(nums, target):
    m = len(nums)
    total = sum(nums)
    a = target + total
    if abs(target) > total:
        return 0 #如果target的绝对值大于total  那就说明也不存在
    if a % 2 != 0:
        return 0 #如果没有这样一个a 那就说明没有解

    a = a // 2
    n = a
    dp = [[0] * (n + 1) for _ in range(m)]
    if nums[0] <= n:
        dp[0][nums[0]] = 1
    zeronums = 0 
    for i in range(m):
        if nums[i] == 0:
            zeronums += 1
        dp[i][0] = 2 ** zeronums
    
    for i in range(1, m):
        for j in range(n + 1):
            if nums[i] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i]]
    return dp[-1][-1]
if __name__ == "__main__":
    nums = list(map(int,sys.stdin.readline().strip().split()))
    target = int(sys.stdin.readline().strip())
    print(solve(nums, target))
```

### 474. 一和零

给你一个二进制字符串数组 strs 和两个整数 m 和 n 。

请你找出并返回 strs 的最大子集的长度，该子集中 最多 有 m 个 0 和 n 个 1 。

如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。

**示例1：**

输入：
```
"10", "0001", "111001", "1", "0"
5, 3
```

输出：
```
4
```

解释：

```
最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。
```

**示例2：**

输入：
```
"10", "0", "1"
1, 1
```

输出：
```
2
```

解释：

```
最大的子集是 {"0", "1"} ，所以答案是 2 。
```
**题目分析：**

这道题也可以看作是一个01背包问题的变种，我们可以视为，将strs中的元素选取放入一个容量为m个0， n个1的背包中，我们能得到的元素的最大数量，特殊的是这是一个二维背包，为了方便理解我们可以使用三维dp数组来求解

```
1. dp数组的定义：dp[k][i][j] 从0 ~ k 个元素中选择元素放入容量为i个0，j个1的背包中，元素的最大数量 

2. 递推公式的推导： 

对于第k个元素，假设它的重量为zerosnum， onesnum，那么显然有：
        if zerosnum > i or onesnum > j :
            dp[k][i][j] = dp[k - 1][i][j]
        else:
            dp[k][i][j] = max(dp[k - 1][i][j], dp[k - 1][i - zerosnum][j - onesnum] + 1 )

3.dp数组的初始化；

dp = [[[0] * (n + 1)] for _ in range(m + 1)] for _ in range(len(strs))
当k为0时，第0个元素的重量为zerosnum, onesnum
那么我们有dp[0][i][j] = 1, if i >= zerosnum and j >= onesnum
```

代码如下：

```python
import sys
def solve( strs, m, n):

dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(len(strs))]
for i in range(strs[0].count('0'), m + 1):
    for j in range(strs[0].count('1'), n + 1):
        dp[0][i][j] = 1
for k in range(1, len(strs)):
    zerosnum = strs[k].count('0')
    onesnum = strs[k].count('1')
    for i in range(m + 1):
         for j in range(n + 1):
            if zerosnum > i or onesnum > j:
                dp[k][i][j] = dp[k - 1][i][j]
            else:
                dp[k][i][j] = max(dp[k - 1][i][j], dp[k - 1][i - zerosnum][j - onesnum] + 1 )
return dp[len(strs) - 1][m][n]

if __name__ == "__main__":
    strs = list(sys.stdin.readline().strip().split())
    data = list(map(int, sys.stdin.readline().strip().split()))
    m = data[0]
    n = data[1]
    print(solve(strs, m, n))
```