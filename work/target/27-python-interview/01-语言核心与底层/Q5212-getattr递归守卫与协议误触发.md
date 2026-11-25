---
title: "[Q5212] __getattr__ 的递归守卫：self.name 自坑与协议误触发"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5212 · __getattr__ 的递归守卫：self.name 自坑与协议误触发

难度：P6 ｜ 标签：__getattr__、无限递归、AttributeError、描述符、hasattr、pickle

**问**：写了个配置代理类，`__getattr__` 里写 `return self.name`，一访问就 `RecursionError`，为什么？`__getattr__` 抛错以外的方式（返回 None、吞异常）会引发什么连锁反应？`hasattr`、`copy.deepcopy`、`pickle` 这些协议为什么会"莫名其妙"触发 `__getattr__`？

**答**：
结论：`__getattr__` 只在**常规查找失败后**才被调用。如果 `__getattr__` 内部又访问一个不存在的实例属性（比如 `self.name` 而实例没有 `name`），会再次进入 `__getattr__`，无限递归直到栈爆。守卫纪律只有一条：`__getattr__` 内部访问自身状态必须走**不可能再触发 `__getattr__` 的路径**——`object.__getattribute__(self, "_data")`、直接读 `self.__dict__`、或访问类上真实存在的属性。失败路径必须抛 `AttributeError`（这是协议契约）：`hasattr` 靠捕获它判定 False，`copy`/`pickle` 等协议靠它探测可选钩子（`__getstate__`、`__reduce__` 等）是否存在——`__getattr__` 吞掉异常或返回 None，会让协议误以为钩子存在（拿到一个错误的返回值）或探测行为失控。

取舍：a) 代理/懒加载类先想清楚 `__getattr__` 与 `__getattribute__` 的分工：只需要拦截缺失属性用 `__getattr__`，要拦截全部访问才用 `__getattribute__`（后者更容易自坑，见 Q028）；b) `__getattr__` 内部只允许出现 `object.__getattribute__` 或 `self.__dict__` 两种自访问方式，其余一律先取到本地变量再操作；c) 失败一律 `raise AttributeError(...) from None`，不要返回 None 哨兵——那会把"没有这个属性"伪装成"属性值是 None"；d) 调试期先加计数器验证触发频率：`__getattr__` 被协议探测打爆是代理类性能劣化的常见暗源；e) 与 `__slots__` 组合时更脆：槽位外的属性全部落到 `__getattr__`，探测量翻倍。

实战：事故形态是"配置代理类在 `__getattr__` 里写 `self._data.get(name)`，某次 `_data` 初始化失败留下半构造对象，访问任意属性直接 RecursionError 把 worker 打死；修复改为构造函数里用 `object.__setattr__` 落 `_data`，`__getattr__` 里先 `object.__getattribute__(self, '_data')` 拿引用，失败路径显式抛 AttributeError"。下面验证递归、协议触发与守卫写法。

```python
import copy


class Config:
    """守卫版: 自访问只走 object.__getattribute__"""

    def __init__(self, data):
        object.__setattr__(self, "_data", data)

    def __getattr__(self, name):
        try:
            data = object.__getattribute__(self, "_data")
        except AttributeError:
            raise AttributeError(name) from None
        if name in data:
            return data[name]
        raise AttributeError(name) from None


class Broken:
    """反面教材: self.name 递归"""

    def __getattr__(self, name):
        return getattr(self, name)


print("[1] 守卫版正常取值:", Config({"env": "prod"}).env)

try:
    Broken()._anything
except RecursionError:
    print("[2] 反面教材触发无限递归: RecursionError")

c = Config({"a": 1})
print("[3] hasattr 协议探测:", hasattr(c, "a"), hasattr(c, "missing"))

try:
    copy.copy(c)
    print("[4] copy.copy 正常走完")
except Exception as e:
    print("[4] copy 协议被 __getattr__ 干扰:", type(e).__name__, e)

try:
    c.missing
except AttributeError as e:
    print("[5] 失败契约:", type(e).__name__, "—— hasattr/协议依赖它判 False")
```

**追问一**：`copy.deepcopy` 和 `pickle` 为什么常被 `__getattr__` 误伤？—— 协议探测靠"试着拿属性 + 捕获 AttributeError"：deepcopy 会探测 `__deepcopy__`/`__getstate__`/`__reduce_ex__`，pickle 会探测 `__getinitargs__`、`__setstate__` 等。如果 `__getattr__` 对这些名字**不抛 AttributeError 而是返回了别的值**，协议会以为钩子存在，把返回值当 callable/元组用，立刻炸出难懂的 TypeError；如果 `__getattr__` 自己抛了其他异常类型，探测路径直接中断。所以代理类的 `__getattr__` 必须**只对业务键放行、对一切双下划线开头或探测名快速抛 AttributeError**（黑名单前缀 `__` 是最省事的守卫）。

**追问二**：`__getattr__` 里 `self._data` 与 `object.__getattribute__(self, "_data")` 什么时候等价、什么时候不等价？—— 当 `_data` 确实存在于实例 dict 且没有同名数据描述符时，两者等价；但半构造对象（`__init__` 异常中断）、`__slots__` 类、或 `_data` 本身还没赋值的场景里，`self._data` 会再次进 `__getattr__`——递归就发生在这里。`object.__getattribute__` 也一样会触发吗？会——它就是常规查找本身，找不到一样调用 `__getattr__`。真正的安全网是构造期保证 `_data` 一定先落地（`object.__setattr__`），`__getattr__` 里对拿不到 `_data` 的情况**直接抛 AttributeError**，而不是再访问别的属性。

## 背诵要点
- `__getattr__` 只兜底常规查找失败；内部自访问必须走 `object.__getattribute__`/`__dict__`，否则递归。
- 失败必须抛 AttributeError：hasattr、copy、pickle 全靠它做协议探测；吞异常=协议误判。
- 探测名（`__` 开头/`__getstate__` 等）在 `__getattr__` 里直接快速拒绝，避免协议误伤。

## 复盘追问
- 配置代理一访问就 RecursionError，根因？（__getattr__ 内 self.xxx 再触发自身）
- 为什么 deepcopy 后代理对象行为诡异？（协议探测拿到错误钩子返回值）
