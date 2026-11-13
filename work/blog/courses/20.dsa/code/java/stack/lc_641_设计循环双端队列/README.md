# LeetCode 641. 设计循环双端队列 (java)

> 来源：[Wang's Blog](https://blog.csdn.net/tyro_java/article/details/145385578)
> 语言：**java**（由 TypeScript 等价转写）

## 题目描述

- - 
- 设计实现双端队列。
- - 
- 实现 MyCircularDeque 类:
- - MyCircularDeque(int k) ：构造函数,双端队列最大为 k 。
- - boolean insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true ，否则返回 false 。
- - boolean insertLast() ：将一个元素添加到双端队列尾部。如果操作成功返回 true ，否则返回 false 。
- - boolean deleteFront() ：从双端队列头部删除一个元素。 如果操作成功返回 true ，否则返回 false 。
- - boolean deleteLast() ：从双端队列尾部删除一个元素。如果操作成功返回 true ，否则返回 false 。
- - int getFront() )：从双端队列头部获得一个元素。如果双端队列为空，返回 -1 。
- - int getRear() ：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1 。
- - boolean isEmpty() ：若双端队列为空，则返回 true ，否则返回 false 。
- - boolean isFull() ：若双端队列满了，则返回 true ，否则返回 false 。

## 示例

```
输入
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
输出
[null, true, true, true, false, 2, true, true, true, 4]

输入
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
输出
[null, true, true, true, false, 2, true, true, true, 4]
解释

MyCircularDeque circularDeque = new MycircularDeque(3); // 设置容量大小为3
circularDeque.insertLast(1); // 返回 true
circularDeque.insertLast(2); // 返回 true
circularDeque.insertFront(3); // 返回 true
circularDeque.insertFront(4); // 已经满了，返回 false
circularDeque.getRear(); // 返回 2
circularDeque.isFull(); // 返回 true
circularDeque.deleteLast(); // 返回 true
circularDeque.insertFront(4); // 返回 true
circularDeque.getFront(); // 返回 4

输入
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
输出
[null, true, true, true, false, 2, true, true, true, 4]
解释
MyCircularDeque circularDeque = new MycircularDeque(3); // 设置容量大小为3
circularDeque.insertLast(1); // 返回 true
circularDeque.insertLast(2); // 返回 true
circularDeque.insertFront(3); // 返回 true
circularDeque.insertFront(4); // 已经满了，返回 false
circularDeque.getRear(); // 返回 2
circularDeque.isFull(); // 返回 true
circularDeque.deleteLast(); // 返回 true
circularDeque.insertFront(4); // 返回 true
circularDeque.getFront(); // 返回 4
提示：
- 1 <= k <= 1000
- 0 <= value <= 1000
- insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull 调用次数不大于 2000 次
```

## 提示

(无)

## 进阶

(无)

## 解法列表

| 方案 | 文件 | 来源语言 |
| --- | --- | --- |
| 1 ) 方案1：数组 | `solution_1_1_)_方案1_数组.java` | ts |
| 2 ) 方案2：链表 | `solution_2_2_)_方案2_链表.java` | ts |
