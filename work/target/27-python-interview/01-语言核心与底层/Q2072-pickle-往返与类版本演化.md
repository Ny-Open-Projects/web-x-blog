---
title: [Q2072] pickle 往返与类版本演化
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2072 · pickle 往返与类版本演化

> 难度:★★★★☆ | 标签:pickle, 版本演化, __setstate__

**问**:用 pickle 存的对象,在类定义改过之后还能反序列化回来吗?怎么平滑迁移?

**答**:pickle 序列化实例时不带类代码,只记录「module.qualname 类引用 + 实例状态」,加载时按名字找到**当前**的类定义——所以类加字段、改方法没问题,旧字节会配新类走。真正的坑是旧数据缺新字段:load 出来的实例不会调用 __init__,状态就是旧字典原样灌回。规范做法是实现 __setstate__:它接收旧状态字典,在这里做字段改名、补默认值、丢弃废弃字段的迁移逻辑,让每个历史版本的字节都能归一到当前模型。demo 演示了「V1 打包 → 类定义演进 → 旧字节加载 → __setstate__ 补齐新字段」的完整闭环。另外记住 pickle 的两条红线:类改名会直接打破引用;加载不可信字节等于执行任意代码,只用于可信数据。

```python
# file: code/01_语言核心与底层/q2072_pickle_evolution.py
"""pickle 往返与类版本演化:老字节遇到新类定义。"""
import pickle


class ProfileV1:
    def __init__(self, name):
        self.name = name


blob_v1 = pickle.dumps(ProfileV1("alice"))    # 用 V1 定义打包


class ProfileV1:                              # 同名类演进:新增字段
    default_level = 1

    def __init__(self, name, level=1):
        self.name = name
        self.level = level

    def __setstate__(self, state):
        state.setdefault("level", self.default_level)   # 旧数据补默认值
        self.__dict__.update(state)


if __name__ == "__main__":
    old = pickle.loads(blob_v1)      # 反序列化用的是「当前」的 ProfileV1
    print("老字节加载后:", old.__dict__, "| 迁移出的 level:", old.level)

    fresh = ProfileV1("bob", 3)
    back = pickle.loads(pickle.dumps(fresh))
    print("新数据往返:", back.__dict__)
    print("往返保真:", back.name == fresh.name and back.level == fresh.level)
```

**追问**:1) 类改名后旧 pickle 还能用吗?——不能,引用按 module.qualname 解析,只能留旧名别名或写迁移脚本;与 JSON 的取舍?——pickle 能往返对象与类型,JSON 只能表达基础结构,但前者加载不可信数据是任意代码执行风险。2) 类版本演化的工程手法?——字段增删配 __reduce__/__setstate__ 自定义还原;加版本标记;新字段给默认值;协议版本(pickle_protocol)跨版本要锁定。3) 安全边界?——unpickle 等于执行构造代码,只对自家可信数据使用;对外交换一律 JSON/结构化格式;签名/加密 pickle 不解决「构造任意对象」问题。4) 生产陷阱?——重构改类名/搬模块导致旧数据全死;缓存系统用 pickle 存对象跨版本读;把 pickle 当「更快的 JSON」。
