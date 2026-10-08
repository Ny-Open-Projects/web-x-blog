# 810 GC 触发时机与降频深挖

> 分类：Go 运行时 / GC | 难度：L3 | 题型：深挖 | 频率：中 | 关键词：**触发四分类** / **pacer** / **手动 STW** / **GOGC** / **sync.Pool**
> 原文锚点：第 1~45 段「触发四因素(堆/CPU/定时/手动,Go1.5 pacer)；手动runtime.GC/FreeOSMemory(同步STW,后者还OS不保证)；降频:参数(GOGC/SetGCPercent)+代码(避defer/短对象/值类型/sync.Pool)」

## 思路与架构
GC 触发是"目标堆增长率驱动的动态调整"而非固定阈值：pacer（Go 1.5 起）综合堆增长、CPU 占比与定时（约 2 分钟）算出下次时机；手动入口（`runtime.GC`/`debug.FreeOSMemory`）是同步 STW 的例外。降频则分参数层（GOGC/SetGCPercent 调大目标增长率）与代码层（减分配、复用对象）。回答时把"触发"与"降频"作为因果两端串起。

## 方案取舍
```text
GC 触发与降频矩阵：
──────────────────────────────────────────────────────────────
维度          手段                 效果                  代价/前提
触发-堆增长   pacer 动态算         达标即回收            目标增长率驱动
触发-定时     forcegcperiod≈2min   保底回收             兜底防漏
触发-手动     runtime.GC          同步 STW             不常用
触发-手动+还  FreeOSMemory         额外还 OS(不保证)    大量释放/测试
降频-参数     GOGC/SetGCPercent↑   频率↓                堆占用↑、单次工作量↑
降频-代码     避循环defer/短对象    分配↓                需改写法
降频-代码     sync.Pool 复用        分配/回收↓          对象生命周期管理

设计法则：
- 先理解 pacer：触发是目标堆增长率驱动的，不是"满才回收"
- 手动触发是 STW，只在释放大量内存/测试时用
- 调大 GOGC 降频但增堆，需按内存预算权衡
- 代码法优先：复用(sync.Pool)比调参更稳
```

## 答题技巧
```text
面试话术（先触发后降频，再权衡）：
1. 触发四分类：堆增长(pacer)/CPU 权衡/定时≈2min/手动
2. 手动：runtime.GC 同步 STW；FreeOSMemory 额外还 OS 不保证
3. 降频-参数：GOGC 默认100、SetGCPercent 等价返回旧值，调大降频增堆
4. 降频-代码：避循环 defer、避热点短对象、值类型缩追踪、sync.Pool 复用
5. 收尾：触发与降频是因果两端，代码法优先于调参
```

> 边界：三色标记与 STW 演进见 807/808/809；分配器与追踪见 811-go-runtime-allocator；软内存限制与 GOGC 见 1006-setmemorylimit。本卡只深挖"GC 触发时机与降频"不重述标记算法。
