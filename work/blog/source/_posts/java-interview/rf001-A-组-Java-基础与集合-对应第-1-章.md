---
title: "A 组：Java 基础与集合（对应第 1 章）"
date: 2026-11-18
categories: [Java面试, 快问快答]
tags: [Java面试, 快问快答, 33]
type: 快问快答
disableNunjucks: true
---

# 第 15 册 快问快答冲刺卡 —— 60 道高频题闪卡（考前最后 3 天）

> 用法：遮住答案自测，答不出的回炉对应章节。每题答案压缩到 3 句以内——
> 这不是完整答案，是"神经通路"，面试时以它为骨架展开。
> 按章节分组，每 10 题一组，配合各章"一页速记卡"滚动复习。

---


## A 组：Java 基础与集合（对应第 1 章）

1. **String 不可变的四条理由？** 池化复用、hashCode 可缓存、线程安全、防篡改安全。
2. **重写 equals 为什么必须重写 hashCode？** HashMap 先 hash 定桶再 equals 精确匹配；只重写 equals 会 get 不到、去重失效。
3. **Integer == 的坑？** 缓存 -128~127，128 起是新对象；包装类一律 equals。
4. **ArrayList 扩容？** 懒初始化 10，扩 1.5 倍（old >> 1），Arrays.copyOf 复制。
5. **为什么工程上不用 LinkedList？** 随机访问 O(n)、每节点两指针内存放大、缓存不友好；数组局部性原理碾压。
6. **HashMap put 流程四步？** 扰动 hash → 初始化 → (n-1)&hash 定桶 → 覆盖/尾插/树化 → 超阈值扩容。
7. **树化阈值 8 与退化 6 的由来？** 阈 8 = bin 已有 8 个节点时下一次插入触发（实测 8 键仍链表）；泊松分布下 bin 长 8 概率千万分之一；退化 6 留缓冲防抖动。
8. **CHM 的 size 怎么统计？** baseCount + CounterCell[] 分段（LongAdder 思想），返回近似值。
9. **CHM 为什么 key/value 不许 null？** get 返回 null 有二义性，并发容器必须一次确定。
10. **泛型擦除的四个限制？** 不能 new T()/T[]/instanceof T、不支持基本类型、静态成员不能用类泛型、重载签名冲突。
