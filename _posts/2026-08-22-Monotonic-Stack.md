---
layout: post
title: "单调栈Monotonic-Stack"
date: 2026-08-22 00:30:00 +0800
categories: [算法]
tags: [LeetCode, hot-100]
---

## 单调栈总结
单调栈是一种特殊的栈结构，它的核心特点是：栈内元素从栈底到栈顶始终保持单调递增或单调递减的顺序，栈内元素我们通常是存数组索引。
我们利用这个性质，可以在 O(n) 的时间复杂度内，**高效地解决一类“寻找数组中某个元素左/右侧第一个比它大（或小）的元素”的问题**。

**单调递增栈**通常用来解决寻找数组内某一元素的下一个比它小的元素，*单调递减栈*与之相反，通常用来寻找数组内某一元素下一个比它大的元素，单调栈的**核心操作时机**是在新元素入栈前，通过 while 循环弹出所有破坏单调性的栈顶元素。“被弹出的元素” 就在此刻找到了它的目标。
下面我们来做几道题加深一下理解
## 题目
### 739. 每日温度
给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。

**示例 1:**

输入:
```
temperatures = [73,74,75,71,69,72,76,73]
```
输出:
```
[1,1,4,2,1,1,0,0]
```
**示例 2:**

输入: 
```
temperatures = [30,40,50,60]
```
输出: 
```
[1,1,1,0]
```
**示例 3:**

输入: 
```
temperatures = [30,60,90]
```
输出: 
```
[1,1,0]
```

**题目分析：** 题目中明确提到了，要找到一个数组中下一个比它更大的元素，所以这是一个很典型的要用单调递减栈去求解的问题，只是这里应该做一个变种，原本的单调栈answer数组中存储的是新入栈的数组元素的索引，这里我们应该改成新入栈的数组元素的索引与出栈元素索引的差值。

**代码如下：**
```python
import sys
class Solution:
  def dailyTemperatures(self, temperatures):
    n = len(temperatures)
    stack = []
    ans = [0] * n
    for i in range(n):
      while stack and temperatures[stack[-1]] < temperatures[i]:
        ans[stack[-1]] = i - stack[-1]
        stack.pop()
      stack.append(i)
    return ans

if __name__ == "__main__":
  temperatures = sys.stdin.read().split()
  temperatures = list(map(int, temperatures))
  print(Solution().dailyTemperatures(temperatures))
```

### 42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
**示例1：**

<img width="412" height="161" alt="image" src="https://github.com/user-attachments/assets/dae08ca8-ea70-44c2-9022-11de8f1a2285" />

输入：
```
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
```

输出：
```
6
```

**示例2：**
输入：
```
height = [4, 2, 0, 3, 2, 5]
```
输出：
```
9
```
**题目分析：**
对于这个问题，我们用单调栈去解决的话，因为只有当一个元素去找到下一个大于它的元素的时候，才会有容积去接到雨水，所以我们这里要使用单调递减栈来寻找一个元素的下一个比它大的元素。

**代码如下：**

```python
import sys
def trap(height):
    stack = []
    res = 0
    n = len(height)
    for i in range(n):
        while stack and height[i] > height[stack[-1]]:
            bottom = stack.pop() #记录一下底层
            if not stack:
                continue  #如果弹出之后栈为空了那就直接进行下一轮
            res += (min(height[i], height[stack[-1]]) - height[bottom]) * (i - stack[-1] - 1) 这一层接的雨水是长乘宽
    return res
if __name__ == '__main__':
    height = sys.stdin.read().split()
    height = list(map(int, height))
    print(trap(height))
```


     
