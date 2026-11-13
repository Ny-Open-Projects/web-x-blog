# LeetCode 295. 数据流的中位数 (java)

> 来源：[Wang's Blog](https://blog.csdn.net/tyro_java/article/details/145344649)
> 语言：**java**（由 TypeScript 等价转写）

## 题目描述

- - 
- 中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。
- - 例如 arr = [2,3,4] 的中位数是 3
- - 例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 
- - 
- 实现 MedianFinder 类:
- - MedianFinder() 初始化 MedianFinder 对象
- - void addNum(int num) 将数据流中的整数 num 添加到数据结构中
- - double findMedian()返回到目前为止所有元素的中位数
- - 与实际答案相差 
-  1
-  0
-  −
-  5
-  10^{-5}
-  10−5 以内的答案将被接受

## 示例

```
输入
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
输出
[null, null, null, 1.5, null, 2.0]

输入
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
输出
[null, null, null, 1.5, null, 2.0]
解释
 MedianFinder medianFinder = new MedianFinder();
 medianFinder.addNum(1); // arr = [1]
 medianFinder.addNum(2); // arr = [1, 2]
 medianFinder.findMedian(); // 返回 1.5 ((1 + 2) / 2)
 medianFinder.addNum(3); // arr[1, 2, 3]
 medianFinder.findMedian(); // return 2.0
```

## 提示

- -
 1
 0
 5
 10^5
 105 <= num <= 
 1
 0
 5
 10^5
 105
- 在调用 findMedian 之前，数据结构中至少有一个元素
 最多 5 * 
 1
 0
 4
 10^4
 104 次调用 addNum 和 findMedian

## 进阶

(无)

## 解法列表

| 方案 | 文件 | 来源语言 |
| --- | --- | --- |
| 1 ) 方案1：优先队列 | `solution_1_1_)_方案1_优先队列.java` | ts |
| 2 ) 方案2：优先队列-优化版 | `solution_2_2_)_方案2_优先队列-优化版.java` | ts |
| 3 ) 方案3：有序集合 + 双指针 | `solution_3_3_)_方案3_有序集合_+_双指针.java` | ts |
