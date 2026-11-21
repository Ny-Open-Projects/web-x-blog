---
title: [Q490] MappingProxyType 与只读视图
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q490 · MappingProxyType 与只读视图

> 难度:★★★☆ | 标签:不可变, API 设计

**问**:把内部 dict 直接 return 给调用方有什么风险?types.MappingProxyType 与 copy 的区别?

**答**:直接暴露内部 dict 意味着任何人都能改它,而且改的是你的内部状态——防御性拷贝(list(d))防住了修改,但断开了实时性且每次拷贝有成本。MappingProxyType 是「活的只读视图」:任何写操作抛 TypeError,底层字典更新时视图实时反映,零拷贝。典型用法:类属性 __dict__ 本身就是它(所以类的命名空间只读)、对外暴露配置表/注册表。注意它只防写不防底层数据结构的「浅可变」:值是 list 时,拿到视图的人依然能改那个 list。

```python
# file: code/01_语言核心与底层/q490_mapping_proxy.py
import types

class Registry:
    _data = {"a": 1}
    PUBLIC = types.MappingProxyType(_data)   # 活的只读视图

if __name__ == "__main__":
    view = Registry.PUBLIC
    print(view["a"])
    try:
        view["b"] = 2
    except TypeError as e:
        print("read-only:", e)
    Registry._data["b"] = 2                  # 内部仍可写
    print("view follows updates:", view["b"])
    print("underlying type:", type(view).__name__)
    print("still shallow: values can be mutable containers")
```

**追问**:1) frozenset 和 MappingProxyType 的共同点?——都是「把可变结构的只读契约编码进类型」:frozenset 不可哈希化地冻结内容,proxy 冻结映射的写入口,二者都不做拷贝。2) 只读视图保护了什么、没保护什么?——挡住调用方的写操作(写抛 TypeError);但底层 dict 仍可被所有者修改,读者会看到变化——它是单向只读契约,不是深不可变。3) proxy 的底层机制?——MappingProxyType 包装 dict 引用转发读操作,写一律 TypeError;type.__dict__ 就是它,类命名空间因此对外只读。4) 生产陷阱?——把 proxy 当「内容不可变」传出去,所有者原地修改后下游行为漂移;序列化要先 dict(proxy) 转换;测试里通过 getattr 拿到底层 dict 原地改,污染其他用例。
