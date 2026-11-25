---
title: "[Q6201] Django 信号重复注册：dispatch_uid 是唯一的稳定钥匙"
date: 2026-11-24
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6201 · Django 信号重复注册：dispatch_uid 是唯一的稳定钥匙

难度：P6 ｜ 标签：Django、signals、dispatch_uid、重复注册、去重、副作用

**问**：`post_save` 注册了一个回调，线上同一个请求触发两次保存时回调执行了两次——排查发现 `connect` 在两处代码都被调用。Django 的 `connect` 不是会去重吗？为什么同一函数注册两次只算一次、两次匿名 lambda 却触发两次？`dispatch_uid` 的去重键和默认键有什么区别？信号重复注册除了"执行两次"还有什么更隐蔽的后果？

**答**：
结论：Django 信号的去重键默认是 `(receiver 的引用, sender)`——**同一个函数对象**重复 connect 会被识别为已注册，返回静默跳过；但每次执行 `signals.post_save.connect(lambda: ...)` 或在函数体内 `def handler(): ...` 再注册，都会生成**新对象**，引用不同，去重失效，同一业务事件触发多次。`dispatch_uid` 把去重键换成你给的稳定标识（字符串/元组，如 `"billing.order.notify"`），无论注册代码执行多少次、receiver 是不是新对象，同 uid 只注册一次。这是唯一能对抗"注册代码被重复执行"（热加载、测试夹具重复 setup、import 路径不同）的机制。

取舍：a) 模块顶层 connect + 命名函数：默认去重基本够用，但依赖"模块只 import 一次"，测试里反复 reload 会破；b) 注册逻辑写在 `AppConfig.ready()`：保证单应用只执行一次，是官方推荐位置；c) 任何在**函数体内/类方法内/可能被多次执行的路径**上 connect 的代码，必须带 dispatch_uid；d) uid 要按业务语义命名（`"app.event.action"`），跨应用冲突比重复注册更难查；e) 重复注册的隐蔽后果不止双倍副作用——事件重复入库让幂等消费失效、审计日志翻倍、`transaction.on_commit` 里发的任务重复投递，往往比崩溃更难发现。

实战：事故形态是"订单审核回调在 `views.py` 的模块级和 `apps.py` 的 ready 里各注册一次，因为一次用了 lambda 包装（新对象）没被去重，审核通过后积分发了两遍；给唯一活跃的注册点加 `dispatch_uid="credit.grant.on_approve"`，并把注册收口到 ready"。下面模拟 Django 的两种去重键。

```python
class Signal:
    def __init__(self):
        self.receivers = []

    def connect(self, receiver, sender=None, dispatch_uid=None):
        if dispatch_uid is not None:
            key = ("uid", dispatch_uid, id(sender))
        else:
            key = ("recv", id(receiver), id(sender))
        if any(k == key for k, _ in self.receivers):
            return False
        self.receivers.append((key, receiver))
        return True

    def send(self, sender):
        return [r(sender) for _, r in self.receivers]


sig = Signal()

print("[1] 同一函数对象注册两次（Django 按引用去重）:",
      sig.connect(on_save := (lambda s: "A"), dispatch_uid=None),
      sig.connect(on_save, dispatch_uid=None),
      "触发次数:", len(sig.send("order")))

sig2 = Signal()
print("[2] 两次独立的 lambda（新对象，去重失效）:",
      sig2.connect(lambda s: "L1"), sig2.connect(lambda s: "L2"),
      "触发次数:", len(sig2.send("order")))

sig3 = Signal()
def handler(sender):
    return "H"
sig3.connect(handler, dispatch_uid="app.order.notify")
dup = sig3.connect(handler, dispatch_uid="app.order.notify")
print("[3] dispatch_uid 相同再注册:", dup, "触发次数:", len(sig3.send("order")))
```

**追问一**：为什么推荐把 connect 全部收口到 `AppConfig.ready()`，而不是分散在模块顶层？—— 模块顶层的注册依赖 import 时机与次数：被两个不同路径 import（包名别名）、测试中 `importlib.reload`、延迟导入都会让注册代码再次执行。`ready()` 由 Django 启动序列保证**每个已安装应用恰好执行一次**，注册次数天然可控；同时 ready 时 apps registry 已就绪，connect 里引用 `get_model` 不会踩 `AppRegistryNotReady`。收口后还有个工程红利：全局搜 `connect(` 能一眼审计"谁在监听什么"。

**追问二**：既然有去重键，为什么 Django 不干脆按函数名去重？—— 函数名不唯一也不稳定：不同模块同名函数会互相吞掉注册（比重复执行更糟）；装饰器生成的闭包没有可靠名字；同一函数为不同 sender 注册是合法且常见的需求（函数名去重会误杀）。所以默认键用 `id(receiver)` 精确到对象，`dispatch_uid` 交给开发者按业务语义显式声明稳定标识。这是"框架给机制、语义由业务定"的典型分工。

## 背诵要点
- 默认去重键是 receiver 对象引用：同一函数重复 connect 被跳过；lambda/函数体内 def 每次都是新对象，去重失效。
- `dispatch_uid` 用业务语义的稳定标识换掉引用键，是对抗"注册代码重复执行"的唯一可靠机制。
- 注册收口到 `AppConfig.ready()`；重复注册的后果是副作用翻倍（双发积分/重复任务），比崩溃更隐蔽。

## 复盘追问
- 同一个 post_save 回调执行了两次，注册点只有模块级一处，最可能的原因？（lambda 包装或函数体内 def 生成了新 receiver）
- 为什么函数名不能当去重键？（跨模块同名互吞、闭包无名、同函数多 sender 是合法需求）
