---
title: "A 卷 Java 基础与集合"
date: 2026-11-18
categories: [Java面试, 笔试]
tags: [Java面试, 笔试题, 33]
type: 笔试题
disableNunjucks: true
---

# 第 24 册 笔试题库 —— 七卷全领域闭卷笔试（含答案与解析）

> 用法：**闭卷作答**，对照答案自评。评分：选择 2 分/题，判断 1 分/题，简答 5 分/题，编程 15 分/题；每卷满分 100。
> 覆盖：A Java 基础与集合 / B 并发与线程 / C JVM / D MySQL / E Redis / F **MongoDB**（新增领域）/ G 算法编程。
> **所有算法编程题的参考实现已在本机 JDK 21.0.2 实测，输出为真实运行结果**（代码见 notes/verify/ExamSolutions.java）。

---


## A 卷 Java 基础与集合

**A-1（选择）** `Integer a = 127, b = 127; Integer c = 128, d = 128;` 则 `a == b` 与 `c == d` 的结果？
A. true / true　B. true / false　C. false / false　D. true / 抛异常
**答案：B。** 包装类缓存 -128~127（`IntegerCache.high` 默认 127），128 超出缓存走 new。

**A-2（选择）** 下列哪项**不是** HashMap 树化的触发条件？
A. bin 中已有 8 个节点时发生下一次插入　B. 表长度 ≥ 64　C. 插入第 8 个节点　D. putAll/resize 后的再平衡
**答案：C。** 精确语义（JDK21 实测）：bin 已有 8 个节点时，**下一次插入（第 9 个）**才调用 treeifyBin；容量 <64 则改为扩容不树化。8 个节点时仍是链表。

**A-3（选择）** `new String("ja") + "va"` 后调用 `intern()`，与自身引用比较的结果？
A. 一定 true　B. 一定 false　C. 视字符串内容而定　D. 编译错误
**答案：C（本考点实测）**：内容为 "polyx2026" 这类**未入池**的新串 → true（JDK7+ 保留堆引用）；内容恰好是 **"java"** → false（它在 System 初始化时已被预入池）。经典的"背答案翻车题"。

**A-4（选择）** `new ArrayList<>()` 首次 add 后内部数组容量？此后加到第 11 个元素时容量？
A. 0→10→15　B. 10→15→22　C. 0→16→24　D. 10→20→30
**答案：A（实测）**。懒初始化；1.5 倍增长（10+10>>1=15；15+7=22）。

**A-5（选择）** 反射拿 `List<String>` 字段声明的泛型参数，靠的是什么？
A. 运行时泛型信息完整保留　B. class 文件的 Signature 属性　C. 注解处理器　D. 不可能拿到
**答案：B。** 擦除后泛型信息以 Signature 形式保留在 class 文件中，`getGenericType()` 可读——Jackson 反序列化的基础。

**A-6（判断）** "String 不可变，所以任何 String 做 HashMap key 后都绝对安全。"
**答案：错。** String 本身不可变且 hash 缓存安全，但若业务持有的是**可变对象**（如自定义 key）字段变化，hash 就失效。判断题考的是表述漏洞：不可变的是 String 对象本身，不是"所有 key"。

**A-7（判断）** "javac 会把 `"a" + b` 编译期直接合并成一个常量。"
**答案：错。** 仅**编译期常量**（两个字面量/常量）才会折叠；含变量的拼接 javac 改写为 StringBuilder（JDK8）或 invokedynamic StringConcatFactory（JDK9+，运行时按形态 specialize）。

**A-8（简答）** 重写 equals 必须满足哪五条性质？违反的后果各举一例。

**【思路】** 这题考的不是"背五条"，是**用反例证明你理解契约为什么存在**——每条违例都要能落到一个真实故障场景（最好的素材就是 HashMap/HashSet 出错）。

**【标准答案】**（先给五条，再给违例后果，一气呵成）
- **自反性**：x.equals(x) 为 true——违反则该对象在集合中"自己找不到自己"；
- **对称性**：x.equals(y) == y.equals(x)——违例：自定义类 equals 里用 instanceof 反向兼容 String，`myObj.equals("str")` 与 `"str".equals(myObj)` 结果不一致，放入 HashSet 后 contains 行为诡异；
- **传递性**：x=y 且 y=z → x=z——违例：继承场景父类 equals 用 instanceof 判断（Point 与 ColorPoint 互比），经典案例见《Effective Java》Item 10；
- **一致性**：多次调用结果相同（对象未修改）——违例：equals 依赖可变字段，对象入 HashMap 后修改字段 → get 返回 null（key"丢失"）；
- **非空性**：x.equals(null) 返回 false——违例：equals 里不判 null 直接强转 → NPE。

**【标准实现】**（背这个模板）
```java
@Override
public boolean equals(Object o) {
    if (this == o) return true;                    // 自反 + 性能短路
    if (!(o instanceof Point)) return false;       // 非空 + 类型（getClass 与 instanceof 的取舍要能讲）
    Point p = (Point) o;
    return x == p.x && y == p.y;
}
@Override
public int hashCode() { return 31 * x + y; }       // 与 equals 字段完全一致
```

**【常见错误】** ① 只重写 equals 不重写 hashCode（HashMap key 丢失）；② equals 里用 `==` 比较（除了枚举/包装类缓存场景全是错）；③ 在 equals 中使用可变字段；④ 用 Arrays.equals 比较对象数组而元素未重写 equals。

**A-9（编程）** 实现一个 `LinkedHashMap` 子类的 LRU，要求 accessOrder 语义正确。
**答案**：见第 13 册题 2（30 秒版）；核心：`super(16, 0.75f, true)` + 重写 `removeEldestEntry`。

---
