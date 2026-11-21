# 全卷断言实证套件 —— "保证完全准确"的证据层

> 把面试内容中**可实证的 Java 断言**变成可重复运行的测试。2026-11-14 首次全量运行：
> **PASS=32 / FAIL=0 / INFO=2**（完整结果见 `suite-result.txt`）。

## 覆盖范围（34 项）

| 组 | 验证内容（对应章节） |
|----|----------------------|
| 核心语言 | Integer/Long 缓存 -128~127、String.hashCode 31 乘子、Compact Strings、intern JDK7+ 行为、ArrayList 1.5 倍扩容（第 1 章） |
| Map 家族 | HashMap 默认容量 16、翻倍扩容、同桶 8 个+容量 64 → 树化（反射查表）、hash 扰动 h^(h>>>16)、fail-fast、LinkedHashMap LRU（第 1 章） |
| 并发 | CHM null 拒绝 + 并发计数、ThreadLocal 弱引用回收、volatile 可见性、**非 volatile 循环真挂起（一手证据）**、线程池 core→queue→max→reject 顺序实测、submit 吞异常 / execute 走 UEH、AtomicLong 并发、Semaphore/Latch/Barrier、线程状态、StampedLock 乐观读、可重入（第 2 章） |
| JDK21 | 虚拟线程 1 万并发（第 2 章） |
| JVM | GC 日志 GC(序号) Pause Young 格式（第 3/15 册）、堆 OOM 消息、容器参数识别（第 3 章） |

## 运行方式

```bash
javac -encoding UTF-8 JavaVerificationSuite.java GcProbe.java OomProbe.java
java --add-opens java.base/java.util=ALL-UNNAMED \
     --add-opens java.base/java.lang=ALL-UNNAMED \
     JavaVerificationSuite
```

> `--add-opens` 是反射读 HashMap 内部 table 的前提——这个参数本身就是面试谈资。

## 运行中的三个真实发现（已回写进对应章节）

1. **非 volatile 可见性挂起实锤**：对照线程自旋 9 分钟未看见主线程写入（CPU 325 秒），JVM 都无法退出——JMM 可见性问题的活体证据（已写入第 2 章）。
2. **JIT 逃逸分析消除分配实锤**：循环内 `new byte[64]` 3000 万次在 `-Xmx64m` 下零 GC——分配被标量替换全部消除（已写入第 3 章）。
3. **"java" 字面量预入池**：`"ja"+"va"` 的 intern 不返回自身（`"java"` 在 System 初始化时已入池）——经典陷阱确认（INFO，第 1 章）。

## 源码核对结论（对照 JDK 21.0.2 src.zip）

- HashMap.putVal / ConcurrentHashMap.transfer / CHM null 拒绝：**逐行一致** ✅
- AQS：**JDK15+ 已重构**（`acquire` 统一私有方法，旧方法名消失）——原理不变、实现形态变（已在第 20 册加版本核对注）✅
