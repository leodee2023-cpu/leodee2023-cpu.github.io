---
layout: post
title: "动态规划 Dynamic Programming4---打家劫舍问题"
date: 2026-09-02 00:40:00 +0800
categories: [刷题]
tags: [LeetCode hot-100, 卡码训练营]
---

## 树形DP

本节重点要讲的是树形DP，树形DP要记住的就是必须要使用**后序遍历**

### 打家劫舍

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

 

**示例 1：**

输入：

```
1,2,3,1
```

输出：

```
4
```

解释：

```
偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
```

**示例 2：**

输入：

```
2,7,9,3,1
```

输出：

```
12
```

解释：

```
偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
```

**解析：**

这道题很简单，简单分析一下就能做出来了。

1. 确定DP数组的下标及其含义： 小偷到达第i个房子，能得到的最大价值。

2. 确定递推公式：我们来思考，如果小偷选择偷第i个房子里的钱，那么此时dp[i] = dp[i - 2] + nums[i]

如果他不偷第i个房子里的钱，那么此时dp[i] = dp[i - 1]

综上，dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

3. dp数组初始化：因为，存在dp[i - 1]和dp[i - 2],所以我们要初始化dp[0] = nums[0]和dp[1] = max(nums[0], nums[1])

**代码如下：**

```python

import sys

def solve(nums):
     if not nums:
          return 0
     n = len(nums)
     if n < 2:
          return nums[-1]
     dp = [0] * n
     dp[0] = nums[0]
     dp[1] = max(nums[0], nums[1])
     for i in range(2, n):
          dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
     return dp[-1]

if __name__ == "__main__":
     nums = list(map(int, sys.stdin.readline().strip().split()))
     print(solve(nums))

```

### 打家劫舍2

你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。

给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。

 

**示例 1：**

输入：

```
2,3,2
```

输出：

```
3
```

解释：

```
你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
```

**示例 2：**

输入：

```
1,2,3,1

```
输出：

```
4
```

解释：

```
你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
```

**示例 3:**

输入：

```
1,2,3
```

输出：

```
3
```

**解析：**
这个和上一道题相比只是从线形变成了环形，下面我们进行分析：

最后一个房屋和第一个房屋是相连的，那么假如我们去掉最后一个房屋，那就和上题线性求解一样了。

同理，假如我们去掉第一个房屋，那也就和上题的线性求解一样了，我们做两次dp，并求这两个dp数组的最大值即可

1. dp数组下标及其含义： 我们定义两个dp数组dp1和dp2，dp[i]的定义都为到达第i个房间时，能够获得的最大价值

2. 递推公式：

对于dp1， 我们有dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i]) 0 <= i <= n - 2

对于dp2， 我们有dp2[j] = max(dp2[j - 1], dp2[j - 2] + nums[j]) 1 <= j <= n - 1

3. 初始化：

对于dp1, 我们初始化dp1[0] = nums[0], dp1[1] = max(nums[0], nums[1])

对于dp2, 我们初始化dp2[0] = nums[1], dp2[1] = max(nums[1], nums[2])

**代码：**

```python
import sys

def solve(nums):
     if not nums:
          return 0
     n = len(nums)
     if n < 2:
          return nums[0]
     if n < 3:
          return max(nums[0], nums[1])
     dp1 = [0] * (n - 1)
     dp2 = [0] * (n - 1)

     dp1[0], dp1[1] = nums[0], max(nums[0], nums[1]) 
     dp2[0], dp2[1] = nums[1], max(nums[1], nums[2]) 

     for i in range(2, n - 1):
          dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i])
          dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i + 1])
     return max(dp1[-1], dp2[-1])

if __name__ == "__main__":
     nums = list(map(int, sys.stdin.readline().strip().split()))
     print(solve(nums))
```
### 打家劫舍3

小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root 。

除了 root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。

给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。

**示例 1:**



输入: 

```
[3,2,3,null,3,null,1]
```

输出: 

```
7 
```

解释:

```
小偷一晚能够盗取的最高金额 3 + 3 + 1 = 7
```

**示例 2:**



输入: 

```
[3,4,5,1,3,null,1]
```

输出:

```
9
```

解释: 

```
小偷一晚能够盗取的最高金额 4 + 5 = 9
```

**解析：**

这就是一道树形dp问题了，开头我们讲了，树形dp必须使用后序遍历，下面我们来进行分析为什么。

对于一个树而言，相连的节点必然是父节点与子节点，因此，要决定父节点偷与不偷，就要先知道子节点的状态，因此我们要采用后序遍历

1. dp数组的下标及含义 dp[i] = (val1, val2) 我们定义dp[i]的val1是到达第i个节点后，不偷这个节点得到的最大价值，val2是偷这个节点得到的最大价值

2. dp数组递推公式：对于每一个节点来讲，假设他的子节点的值分别是left和right，

那么如果不偷这个节点，我们就可以得到这个节点的val1应该是他左子节点的最大值+右子节点的最大值

如果偷这个节点，我们就可以得到这个节点的val2应该是他左子节点的val1加上右子节点的val1再加上它自身的值

综上，val1 = max(left) + max(right);val2 = left[0] + right[0] + root.val

3. dp数组的初始化，这里我们只需要令子节点为None时，返回的dp为(0, 0)即可

4. 遍历顺序，后序遍历

**代码：**

```python

import sys
from collections import deque
class TreeNode:
     def __init__(self, val = 0, left = None, right = None):
          self.val = val
          self.left = left
          self.right = right

def solve(root):
     if not root:
          return (0, 0)
     left = solve(root.left)
     right = solve(root.right)
     val1 = max(left) + max(right)
     val2 = left[0] + right[0] + root.val
     return (val1, val2)

def build_tree(vals):
     if not vals or vals[0] is None:
          return None
     q = deque()
     root = TreeNode(val = vals[0])
     q.append(root)
     i = 1
     while q and i < len(vals):
          p = q.popleft()
          if i < len(vals) and vals[i] is not None:
               left = TreeNode(vals[i])
               p.left = left
               q.append(left)
          i += 1
          if i < len(vals) and vals[i] is not None:
               right = TreeNode(vals[i])
               p.right = right
               q.append(right) 
          i += 1
     return root
if __name__ == "__main__":
     vals = eval(input())
     root = build_tree(vals)
     print(max(solve(root)))

```
     
