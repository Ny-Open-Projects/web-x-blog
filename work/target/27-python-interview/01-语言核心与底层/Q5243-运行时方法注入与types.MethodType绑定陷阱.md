---
title: "[Q5243] 运行时方法注入：实例挂函数的绑定陷阱与 types.MethodType"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5243 · 运行时方法注入：实例挂函数的绑定陷阱与 types.MethodType

难度：P6 ｜ 标签：types.MethodType、绑定方法、实例属性、描述符、monkeypatch、partial 预绑定、测试替身

**问**：给实例动态挂一个函数 `c.patched = lambda ...` 为什么调用时不会自动绑定 self？`types.MethodType` 与"挂到类上"分别是什么语义？monkeypatch 替换类方法做测试替身时要注意什么？`functools.partial` 预绑定 self 与绑定方法是什么关系？

**答**：
结论：方法绑定的本质是**描述符协议发生在"类"这一层**（Q2618/Q1813）：函数对象实现 `__get__`，属性访问 `c.get` 走 type(c).__mro__ 找到类里的函数描述符，`__get__(None→instance)` 返回绑定方法——而**实例的 `__dict__` 命中会短路类查找吗？不会**：非数据描述符的优先级是"实例 dict 优先"（函数是非数据描述符），所以 `c.patched = lambda ...` 存进实例 dict 后，`c.patched` 直接返回**裸函数**，根本不经过 `__get__`，也就没有绑定——调用时缺 self 参数直接 TypeError。三条注入路径的语义矩阵：①**实例挂裸函数**——不绑定，self 要手动闭包捕获或忽略；②**types.MethodType(fn, obj)**——显式构造绑定方法对象（等价于 fn.__get__(obj, type(obj))），`self` 参数自动就位，适合运行时给单实例注入带 self 语义的行为；③**挂到类上（`Client.get = fn`）**——写入类的 dict，走描述符协议，**所有实例共享且自动绑定**，这是 monkeypatch 的标准形态。`functools.partial(Class.method, instance)`（Q519）预绑定 self，得到的是可调用对象而非 MethodType——没有 `__self__` 属性、不能做描述符，但作为回调/线程注册（Q1597 系）足够，且可以继续固定更多参数。测试纪律：monkeypatch 替换类方法必须**保存原引用并在 teardown 还原**（pytest 的 monkeypatch fixture 自动做），替换期间其他线程/异步任务可能读到替身——集成测试要串行化；替身要保留签名语义（参数校验、异常类型），否则测试通过≠真实链路可用。

取舍：a) 单实例定制 vs 全类替换：单实例行为差异（如某个 client 关闭重试）优先闭包/MethodType 注入，避免类级 patch 的全局影响面；b) 注入 vs 构造参数：能用依赖注入（构造时传入 collaborator）就不用运行时 patch——patch 是测试与遗产代码的润滑剂，不是架构；c) MethodType vs lambda 闭包捕获：`c.get2 = lambda key: orig(c, key)` 语义等价且更直白，MethodType 的价值是"被注入对象真的以方法身份出现"（有 `__self__`、`__func__`，调试与框架内省友好）；d) 性能：实例 dict 命中比类描述符快一点（少了 `__get__` 调用），但为省一次调用而绕开绑定机制是负优化；e) __slots__ 类不能随便挂实例属性——注入路径要先确认 `__dict__` 存在。

实战：事故形态是"测试里 `Client.fetch = mock_fn` 替换类方法，mock 忘记还原，另一个测试文件 import 同类继续跑——半条流水线用了 mock 数据入库；修复为 conftest 统一 monkeypatch fixture（自动还原）+ CI 加 ResourceWarning 类巡检（测试结束断言 Client.fetch.__name__ 不变）。另一处生产代码给长连接对象用 MethodType 注入 per-connection 编码器，连接关闭后 MethodType 持有 conn 引用造成泄漏——注入表随连接生命周期登记/注销"。下面实测三条注入路径与绑定语义。

```python
# 运行时方法注入: 实例挂函数、MethodType 与类级替换的绑定语义
import types
from functools import partial

class Client:
    def __init__(self, host: str) -> None:
        self.host = host

    def get(self, key: str) -> str:
        return f"{self.host}:{key}"

c = Client("db")

print("[1] 实例挂裸函数: 不经过描述符 __get__, 无自动绑定")
c.patched = lambda key: f"NO-SELF:{key}"
print("    c.patched('k') =", c.patched("k"), "(lambda 无 self 参数, 直接可用)")
def want_self(self, key: str) -> str:
    return f"{self.host}:{key}(instance-fn)"
c.patched2 = want_self
try:
    c.patched2("k")
except TypeError as e:
    print("    传 self 的函数挂实例属性 -> TypeError:", e, "(self 没有被绑定)")

print("[2] types.MethodType: 显式构造绑定方法, self 自动就位")
c.patched3 = types.MethodType(want_self, c)
print("    c.patched3('k') =", c.patched3("k"))
print("    __self__ 是 c:", c.patched3.__self__ is c, "| __func__ 是原函数:", c.patched3.__func__ is want_self)

print("[3] 挂到类上: 走描述符协议, 所有实例共享且自动绑定")
Client.get_quiet = lambda self, key: f"{self.host}:{key}(quiet)"
print("    c.get_quiet('k') =", c.get_quiet("k"), "| 新实例同样可用:", Client("cache").get_quiet("k"))

print("[4] partial 预绑定 self: 可调用对象而非 MethodType")
bound = partial(Client.get, c)
print("    bound('k') =", bound("k"), "| 有 __self__ 吗:", hasattr(bound, "__self__"))
extra = partial(Client.get, c, "fixed-key")     # 继续固化第一个参数
print("    固化参数后:", extra())

print("[5] 类级 monkeypatch: 保存原引用, teardown 还原")
orig = Client.get
Client.get = lambda self, key: "MOCK"
print("    替换期 c.get('k') =", c.get("k"))
Client.get = orig
print("    还原后 c.get('k') =", c.get("k"), "(还原必须写进 finally/teardown)")
print("[rule ] 实例挂函数=不绑定; MethodType=显式绑定; 挂类=共享绑定; patch 必须可还原")
```

**追问一**：为什么实例 dict 里的函数"短路"了绑定，而类里的不会？非数据描述符的查找优先级展开讲讲。—— 属性查找规则：`obj.attr` 先看 `type(obj).__mro__` 上有没有**数据描述符**（定义了 `__set__`/`__delete__`，如 property）；有则数据描述符优先级最高，实例 dict 根本轮不到；没有则先查实例 dict——命中直接返回（**不调用任何 `__get__`**，这就是裸函数不绑定的根源）；未命中再沿 MRO 找非数据描述符（函数）并调用 `__get__(obj, type(obj))` 完成绑定，最后才是类属性普通值。函数是"定义了 `__get__` 没有 `__set__`"的非数据描述符，所以：类里的函数 + 实例查找 = 绑定方法；实例 dict 里的函数 = 原始函数对象。推导两个推论：①实例 dict 挂 property 同名属性会**遮蔽** property 吗——不会，property 是数据描述符，优先级高于实例 dict（这就是"实例属性不能覆盖 property"的经典坑）；②想让实例挂的函数也绑定，必须自己包装 `types.MethodType` 或让函数对象进类 dict。这套优先级同时解释了 Q1813（classmethod/staticmethod 的绑定差异）与 `__slots__` 类无实例 dict 的注入限制。

**追问二**：MethodType 注入的对象被第三方框架序列化/pickle 时会怎样？运行时注入对可观测性（日志、profiling）有什么隐性成本？—— pickle 语义：绑定方法 pickle 时按"实例 + 函数的限定名"还原（`pickle.MethodType` 的 reduce 走 `__qualname__` 查找），注入的函数若是模块级 def 可以还原，若是 lambda/闭包则 pickle 直接失败——注入行为与序列化通道的兼容性要在设计时核对（Q428 的对象图约束同族）。可观测性成本：①**profiling 名字漂移**——MethodType 包装的函数在采样器里显示的还是 `__func__` 的名字，但部分链路追踪按方法对象身份去重，注入导致同一逻辑被记成不同调用点；②**日志归因**——动态注入让"这个类的行为"不再由类定义唯一决定，读代码的人看不到全貌，工程纪律是注入点集中在一处（如连接工厂），并在日志里打上注入标记；③**静态分析与类型检查失明**——mypy 看不到运行时注入，若注入改变了签名契约，要靠运行时断言兜底。原则：注入是"逃生舱"，用得越少越隐形越好；批量行为差异应该走子类或策略对象，而不是 patch。

## 背诵要点
- 绑定发生在类层描述符协议：实例 dict 命中短路 __get__（裸函数不绑定 self），类 dict 命中才绑定；数据描述符（property）优先级高于实例 dict。
- 三条注入路径：实例挂函数（不绑定）、types.MethodType（显式绑定，有 __self__/__func__）、挂类（全实例共享绑定）；partial 预绑定 self 是可调用对象非 MethodType。
- monkeypatch 纪律：保存原引用+teardown 还原、替身保签名语义、注入点集中登记防泄漏；注入是逃生舱，架构层用依赖注入/策略对象。

## 复盘追问
- 为什么 c.fn = func 挂实例属性调用不自动传 self？（属性查找中实例 dict 优先且不触发函数 __get__；绑定只发生在类层非数据描述符路径）
- 替换类方法做测试替身的风险面？（全局影响、并发读到替身、忘还原污染后续用例、pickle/内省兼容性；用 monkeypatch fixture 自动还原）
