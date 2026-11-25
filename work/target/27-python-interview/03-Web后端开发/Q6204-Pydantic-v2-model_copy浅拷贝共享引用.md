---
title: "[Q6204] Pydantic v2 model_copy：浅拷贝的引用共享暗雷"
date: 2026-11-24
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6204 · Pydantic v2 model_copy：浅拷贝的引用共享暗雷

难度：P6 ｜ 标签：Pydantic v2、model_copy、deep、浅拷贝、引用共享、对象池

**问**：为了省校验开销，把一个"模板"Pydantic 模型 `model_copy()` 出来按请求微调——结果改了请求 A 的 `tags` 字段，请求 B 的数据也跟着变。`model_copy()` 不就是复制吗？为什么嵌套字段会串？`deep=True` 什么代价？什么时候该用 copy、什么时候该重新构造（validate）？

**答**：
结论：Pydantic v2 的 `model_copy(deep=False)` 是**浅拷贝**：顶层字段逐个复制引用，嵌套的 list/dict/子模型与原对象**共享同一实例**；对嵌套可变对象的修改会穿透到"所有副本和原件"。`deep=True` 才对嵌套对象做 deepcopy，语义隔离。这和 Python `copy.copy` 的语义一致——Pydantic v2 为了让 copy 极快（跳过校验、跳过嵌套复制），默认就是浅的。串数据的场景通常是：对象池/模块级模板 + 多请求复用 + 修改嵌套字段，三个条件凑齐就炸。

取舍：a) 只改**标量顶层字段**（name/price 这类不可变值）：`model_copy(update={...})` 安全且快，这是它设计的本意；b) 要改嵌套结构：`model_copy(deep=True)`，代价是 deepcopy 的 CPU 与内存成本，数据大时抵消了"省校验"的收益；c) 数据来自**不可信输入**（用户请求体）：永远重新构造走完整校验，copy 只适合"从可信模板派生"的场景——浅拷贝跳过校验意味着模板是脏的副本也是脏的；d) 缓存响应对象要谨慎：缓存的模型被 copy 后若调用方修改嵌套字段，缓存本体被污染，下一次请求拿到脏数据——要么 copy(deep=True)，要么在缓存边界做序列化隔离；e) 团队规范上，把"model_copy 只允许 update 标量 + 带注释"写进 review checklist。

实战：事故形态是"推荐接口把热门商品模型缓存在模块级变量，每请求 `model_copy(update={'view': n})` 微调浏览数（标量，安全），后来需求加了 `tags` 批量改写，直接 `copy.tags.append(...)`，所有商品模板的 tags 越积越多，A 商品挂上了 B 商品的标签；修复是 tags 变更走 `deep=True`，并在缓存出口做只读约束"。下面复现共享与隔离。

```python
import copy


class Tag:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Tag({self.name!r})"


class Model:
    def __init__(self, name, tags):
        self.name = name
        self.tags = tags

    def model_copy(self, deep=False):
        return Model(self.name, copy.deepcopy(self.tags) if deep else self.tags)


a = Model("a", [Tag("x")])
shallow = a.model_copy()
deep = a.model_copy(deep=True)

a.tags[0].name = "hacked"

print("[1] 浅拷贝视角:", shallow.tags, "——嵌套引用共享，被源头污染")
print("[2] 深拷贝视角:", deep.tags, "——deep=True 隔离")
print("[3] 身份一致性: shallow.tags is a.tags =", shallow.tags is a.tags)
print("[4] 取舍: 浅拷贝快（不复制嵌套对象），跨请求复用必须 deep=True 或重建")
```

**追问一**：`model_copy(update={...})` 为什么不做校验？这是特性还是风险？—— 特性与风险一体：v2 的设计意图是"已验证实例派生变体"跳过重复校验的开销（校验是 Pydantic 最贵的环节），update 只是替换 `__dict__` 里的值。风险在于 update 的值完全不受约束：类型错了、嵌套脏了都不报错，错误延迟到序列化或下游使用时爆。所以规则是：update 只放标量与不可变值；任何"从用户输入构造"的对象必须走 `Model(**data)` 完整校验，copy/update 只用于服务端可信数据的派生。

**追问二**：和 `copy.deepcopy` 相比，`model_copy(deep=True)` 有没有额外语义？什么时候反而该手写构造？—— `deep=True` 本质就是对字段值做 `copy.deepcopy`，没有额外魔法；区别在成本结构：deepcopy 对复杂嵌套（大列表、深子模型）是线性昂贵的，且 deepcopy 不重建校验器状态。当"变体"与模板差异大（改了类型、删了字段、来自外部数据）时，deepcopy 只是复制脏结构，正确做法是 `Model(**template.model_dump())` 重新走校验——dump+重建 比 deepcopy 多花校验时间但换来结构正确。判断标准：派生对象的字段值是否全部可信且合法，是 → copy，否 → 重建。

## 背诵要点
- `model_copy(deep=False)` 浅拷贝：顶层复制引用，嵌套 list/dict/子模型共享实例，修改互相穿透。
- 安全区：`update` 标量字段；危险区：改嵌套结构（必须 deep=True）或用不可信输入派生（必须重新校验）。
- 缓存 + copy 组合要防缓存本体被污染；差异大的派生用 `model_dump()` + 重建走完整校验。

## 复盘追问
- 请求 A 改了 tags 请求 B 也变了，三个凑齐的条件是什么？（模块级模板 + 多请求复用 + 修改嵌套可变字段）
- model_copy(deep=True) 和 model_dump 重建怎么选？（值全可信合法用 copy；来源不可信或差异大用 dump+重建走校验）
