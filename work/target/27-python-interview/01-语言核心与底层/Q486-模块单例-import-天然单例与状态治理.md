---
title: [Q486] 模块单例:import 天然单例与状态治理
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q486 · 模块单例:import 天然单例与状态治理

> 难度:★★★☆ | 标签:模块, 单例

**问**:为什么说「模块就是单例」?模块级可变全局状态在生产里会引发什么问题?

**答**:每个模块只在首次 import 时执行一次,之后所有 importer 从 sys.modules 拿同一个对象——所以模块级变量天然是全局单例,双检锁单例很多时候只是把这件事显式化。代价:全局可变状态让调用顺序影响行为、测试之间互相污染、多进程 fork 后各自副本不一致、隐藏了「谁在读写它」。治理原则:模块级只放不可变常量与纯函数;必须可变的状态收敛到一个显式的 context/config 对象;需要跨请求隔离的(web 场景)用 contextvars。

```python
# file: code/01_语言核心与底层/q486_module_singleton.py
import sys

import collections
import collections as collections_alias

if __name__ == "__main__":
    print("module identity stable:", collections is collections_alias)
    print("cached in sys.modules:", sys.modules["collections"] is collections)
    print("same module object for every importer — this is the singleton")

    state = {"calls": 0}              # 演示:模块级可变状态的全局性

    def get_state():
        state["calls"] += 1
        return dict(state)

    print(get_state(), get_state())
```

**追问**:1) 多进程部署时模块单例还成立吗?——每个进程独立初始化一份,「单例」只在进程内成立;跨进程共享要靠外部存储,这也解释了 fork 后内存状态各不相干。2) 为什么 import 缓存是「天然单例」?——sys.modules 是进程级登记表,首次 import 初始化一次,后续全部命中缓存;单例语义免费,但代价是与导入系统耦合(循环导入、测试隔离都变难)。3) fork 与模块状态的关系?——子进程继承父进程的 sys.modules 快照与全部模块状态,fork 后各自演化;fork 前的未 flush 连接、未完成任务都被复制,所以 pre-fork 模型要 gc.freeze + 关闭共享资源。4) 生产陷阱?——测试并行读写模块级可变状态互相污染;正确姿势是显式单例类 + 初始化入口,或依赖注入替代隐式全局。
