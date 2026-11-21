---
title: [Q5035] marshal 的定位与误用事故：pyc 专用不是通用序列化
date: 2026-11-20
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5035 · marshal 的定位与误用事故：pyc 专用不是通用序列化

> 难度:★★★ | 标签:marshal, pyc, 序列化, 版本演进

**问**：标准库里的 `marshal` 是干什么的？它和 pickle、json 的边界在哪？为什么有人拿 marshal 做序列化后在升级 Python 时数据全废？

**答**：marshal 是**为 .pyc 文件服务的内部格式**——读写 code 对象（字节码、常量表、名字表）比 pickle 更快更直接，这是它唯一的设计目标。三个致命边界：1) **跨版本不兼容**：字节码指令集随版本变化（3.10→3.11 加了异常表，3.12 重排指令），marshal 不保证向后兼容，pyc 里就带着 magic number 校验版本；2) **类型面窄**：只支持 None/数值/字符串/bytes/元组/列表/dict/set/code/frozenset 等"解释器原生"类型，自定义类实例直接不支持；3) **无独立演进**：官方文档明说"并非通用持久化模块"，格式随解释器实现自由变化。事故模式：有人因为 marshal 比 pickle 快就缓存 code 对象或数据到磁盘/Redis，Python 升级后 marshal.loads 报错或读出垃圾。正确分工：**code 对象且生命周期在当前解释器内 → marshal；一般对象持久化 → pickle（协议版本显式指定，Q5037 的兼容契约）；跨语言/跨信任边界 → JSON/schema 协议**。

```python
# file: code/01_语言核心与底层/q5035_marshal_scope.py
import marshal
import pickle

# 1) marshal 的主场: code 对象的往返
def target(n: int) -> int:
    return n * 2 + 1

co = target.__code__
blob = marshal.dumps(co)
co2 = marshal.loads(blob)
import types
assert isinstance(co2, types.CodeType)
print("code 对象 marshal 往返 OK, 字节数:", len(blob))
func = types.FunctionType(co2, {"__builtins__": __builtins__}, "target")
print("code 重绑为函数后运行: target(10) =", func(10))  # 21

# 2) 类型面窄: 自定义类实例直接失败
class Point:
    def __init__(self, x): self.x = x

try:
    marshal.dumps(Point(1))
except ValueError as e:
    print("marshal 不支持自定义类:", e)

# 3) 对普通数据, pickle 才是持久化工具(带协议版本契约)
data = {"k": [1, 2.5, "s"], "nested": {"a": (1, 2)}}
m = marshal.dumps(data)          # 当前版本能读
p = pickle.dumps(data, protocol=5)
print(f"marshal={len(m)}B pickle5={len(p)}B —— 大小接近, 但只有 pickle 承诺兼容")

# 4) 版本敏感性的证据: marshal 版本号随解释器变化
print("marshal version:", marshal.version, "(随解释器发布变化, 无跨版本承诺)")
```

**追问**：1) pyc 为什么不会因 marshal 不兼容而崩？——pyc 头部有 4 字节 magic number，导入系统先校验它与当前解释器匹配，不匹配就重编译（Q2611 的失效判定）。2) marshal 比 pickle 快多少、什么场景值得用？——通常 1.5-3 倍于 pickle 且支持 code 对象；值得用的场景基本只有"当前进程内传递 code 对象"（如动态加载器、打包工具），业务数据持久化永远轮不到它。3) 为什么说 marshal 无安全优势？——它和 pickle 一样是二进制还原语义，虽然不能执行任意构造器，但官方明确"不用于不可信数据"；安全边界不能当作选 marshal 的理由。

## 背诵要点
- marshal 是 .pyc 的内部格式：code 对象专用，跨版本不兼容、类型面窄、无兼容承诺。
- 业务持久化用 pickle（显式协议版本），跨信任边界用 JSON/schema 协议。
- pyc 靠 magic number 防版本错配，导入系统自动重编译。

## 复盘追问
- 线上发现 Redis 里存的 marshal 数据升级后读不出来，除了重写数据你还有什么应急读取手段？风险是什么？
- 为什么官方不给 marshal 兼容承诺？这种"内部格式当公共 API"的治理问题在你的仓库里还有哪些？
