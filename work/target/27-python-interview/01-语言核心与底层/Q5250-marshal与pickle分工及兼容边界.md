---
title: "[Q5250] marshal 与 pickle 的分工：pyc 内部格式、类型白名单与兼容边界"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5250 · marshal 与 pickle 的分工：pyc 内部格式、类型白名单与兼容边界

难度：P6 ｜ 标签：marshal、pickle、pyc、代码对象、类型白名单、版本兼容、序列化选型、.pyc 缓存

**问**：marshal 是什么——它与 pickle 同为"对象序列化"为什么并存？marshal 的类型白名单窄在哪、它能做而 pickle 不能做的是什么（code 对象）？"marshal 不承诺跨版本兼容"对 pyc 缓存意味着什么？什么场景该选 marshal、什么场景明确不该？

**答**：
结论：marshal 是 **Python 内部的"编译产物序列化器"**——`.pyc` 文件的字节码部分就是 `marshal.dumps(模块的 code 对象)`（Q415 的启动优化、Q1257 的 code 对象深水区都以它为底层），而 pickle 是**通用的对象持久化协议**。两者分工的四条分界线：①**类型白名单**——marshal 只认解释器原生类型（None/bool/int/float/complex/str/bytes/bytearray/tuple/list/set/frozenset/dict/code 对象），自定义类实例、函数、lambda 一律 ValueError；pickle 面向任意对象（`__reduce__` 机制，代价是 unpickle 即任意代码执行的安全面，Q428）；②**code 对象是 marshal 独占**——pickle 无法序列化 code 对象（TypeError），而 marshal 能，这是 pyc 必须用它的根本原因（编译产物 = code 对象树）；③**版本承诺**——pickle 有跨版本协议规范（0-5，新旧互相可读），marshal **明确不承诺跨 Python 版本兼容**（格式随解释器内部实现自由变化，文档原话"不是持久化格式"），pyc 的 magic number 就是版本闸门——3.12 的 pyc 给 3.11 读必炸；④**性能与体积**——marshal 是 C 实现的极简编解码，无协议协商、无版本谈判，比 pickle 快且产物小；对象图能力上 pickle 的 memo 是**文档承诺的契约**（同一对象共享/循环引用确定保真），marshal 内部虽用引用标记在单次 dumps 内也保真共享与递归（3.12 实测如此），但这是实现细节不在文档契约内——跨版本升级不能赌它。选型口径：**编译产物缓存（pyc 类需求）与"同版本解释器内部传输"用 marshal；跨进程持久化/缓存一律 pickle（可信环境）或 JSON（不可信）——绝不把 marshal 当通用序列化对外**。

取舍：a) pyc 失效边界：pyc 校验用 mtime+size 或 hash（PEP 552），marshal 格式变更靠 magic number 拦截——清理 __pycache__ 是无害操作，但**手工伪造 pyc 让旧版本解释器读**必报 bad marshal data；b) marshal 的合理外用：解释器级缓存（如自研编译缓存、AST/code 产物的临时落盘）在同版本环境内可用，但要带版本戳自校验；c) 与 pickle 的对象图差异：pickle 有 memo（同一对象序列化一次、引用还原，Q5077 的 deepcopy memo 同机制），marshal 展开共享——对象图大且共享多时 marshal 体积反而可能更大；d) 安全：marshal.loads 不执行代码（白名单外直接报错），比 pickle.loads 安全一个量级，但**解析不可信数据同样不该用 marshal**（资源耗尽类风险仍在）；e) 第三方替代：跨版本代码产物缓存用 pickle 存字节码？不行（code 对象 pickle 不支持）——要么 marshal+版本戳，要么源头保存源码文本每次重新 compile。

实战：事故形态是"自研模板引擎把 compile 出的 code 对象 marshal 落盘做编译缓存，升级 Python 3.11→3.12 后所有缓存命中处直接报 ValueError: bad marshal data——缓存层没做 magic number 校验，回退路径也没有（炸在请求路径上）。修复为：缓存文件头写 sys.version + marshal 格式戳，读时校验不匹配即丢弃重建；同时把'升级解释器必须清空编译缓存目录'写进升级 runbook"。下面实测类型白名单、code 对象独占与体积/速度差异。

```python
# marshal 与 pickle: 类型白名单、code 对象与兼容边界
import marshal
import pickle
import sys
import timeit

data = {"id": 7, "tags": ["a", "b"], "score": 0.5, "nested": {"ok": (1, 2)}}
mb = marshal.dumps(data)
pb = pickle.dumps(data)

print("[1] 原生类型往返: 两者都行, marshal 产物更小")
print("    marshal 字节数:", len(mb), "| pickle 字节数:", len(pb), "| 往返一致:", marshal.loads(mb) == data)

print("[2] 类型白名单: marshal 拒绝自定义类实例")
class P:
    def __init__(self) -> None:
        self.x = 1

try:
    marshal.dumps(P())
except ValueError as e:
    print("    marshal.dumps(P()) -> ValueError:", e)
print("    pickle 可以还原自定义类:", pickle.loads(pickle.dumps(P())).x == 1)

print("[3] code 对象: marshal 独占能力 (pyc 的根基)")
code = compile("value = 40 + 2", "<tpl>", "exec")
print("    marshal 存 code 对象:", type(marshal.loads(marshal.dumps(code))).__name__)
try:
    pickle.dumps(code)
except TypeError as e:
    print("    pickle.dumps(code) -> TypeError:", e)
ns = {}
exec(marshal.loads(marshal.dumps(code)), ns)     # 还原后可执行
print("    marshal 往返的 code 仍可 exec:", ns["value"] == 42)

print("[4] 引用共享与递归: 当前实现两者都保真, 契约强度不同")
shared = ["x"] * 3
holder = {"a": shared, "b": shared}
back = pickle.loads(pickle.dumps(holder))
print("    pickle memo 还原共享:", back["a"] is back["b"], "(memo 是协议文档承诺)")
mm = marshal.loads(marshal.dumps(holder))
print("    marshal 共享保真:", mm["a"] is mm["b"], "(内部引用标记是实现细节, 不在文档契约内)")
lst = []
lst.append(lst)
rec_m = marshal.loads(marshal.dumps(lst))
rec_p = pickle.loads(pickle.dumps(lst))
print("    递归往返: marshal", rec_m[0] is rec_m, "| pickle", rec_p[0] is rec_p)

print("[5] 兼容边界: marshal 不承诺跨版本, pyc 靠 magic number 闸门")
print("    当前解释器:", sys.version.split()[0], "| 缓存自校验应写版本戳:", sys.implementation.cache_tag)
n = 20000
t1 = timeit.timeit(lambda: marshal.dumps(data), number=n)
t2 = timeit.timeit(lambda: pickle.dumps(data), number=n)
print(f"[6] 速度: marshal {t1:.3f}s vs pickle {t2:.3f}s (同量级, 差异在协议复杂度)")
print("[rule ] marshal=编译产物缓存+版本戳自校验; pickle=可信环境通用; 对外协议一律 JSON")
```

**追问一**：pyc 的 magic number 与 PEP 552 的 hash 校验是怎么回事？为什么"同版本解释器但源码未变"也可能 pyc 失效重编译？—— pyc 文件头四字节是 **magic number**（随 Python 版本/实现变化，3.10 起每个版本还会因字节码语义微调而变），加载器先比对 magic 不匹配即丢弃——这是 marshal "不承诺跨版本"的闸门落点；PEP 552（3.7+）引入两种校验模式：**timestamp 模式**（默认，头里存源码 mtime+size，mtime 变化即失效）与 **hash-based 模式**（头存源码内容哈希，分 checked/unchecked：checked 每次加载验证哈希——mtime 不可靠的场景如构建产物分发，unchecked 只信任 pyc 不再校验）。"源码未变也重编译"的常见触发：①**mtime 精度/时钟问题**——构建系统拷贝文件把 mtime 扰动，timestamp 模式误判失效（切 hash-based checked 模式解决）；②**不同解释器构建产物**——venv 混用、Docker 层缓存里残留旧版本 pyc，magic 不匹配；③unchecked hash 模式下源码变了但没重新生成 pyc，**旧字节码被照常使用**——这是 unchecked 模式的固有风险，CI 里必须保证生成步骤与部署原子绑定。

**追问二**：marshal 能处理递归（自引用 list）吗？它内部有引用标记，与 pickle memo 的"引用共享契约"差异怎么评估？—— 递归支持：marshal 对**递归容器**（`lst.append(lst)`）有特判，能往返；实测 3.12 里**共享引用**（两个键指向同一个非循环对象）在单次 dumps 内也保真（`d["a"] is d["b"]` 为 True）——内部用 FLAG_REF 标记复用已序列化对象。但契约强度是本质差异：**pickle 的 memo 写在协议文档里**（版本协议保证共享/循环还原），marshal 的引用标记是"当前实现的行为"，marshal 文档自我定位是"内部格式、不承诺稳定"——升级 Python 后依赖它的身份语义可能静默改变。评估口径：①**体积**——两者共享保真后差异主要来自协议开销，marshal 通常更小更快（无备忘录协议协商）；②**语义**——依赖"同一对象只出现一份"（身份去重、原地修改可见性）的代码，marshal 场景要靠**单版本环境 + 升级时回归测试**兜住，pickle 场景协议兜底；③**工程决策**——marshal 只用于"编译产物"这类天然树形、无身份语义依赖的对象图；对象图复杂的持久化回 pickle，不可信环境回 JSON/MessagePack。三个工具三种契约：marshal 保"结构值"（实现级）、pickle 保"对象图"（协议级）、JSON 保"数据互操作"——错配即事故。

## 背诵要点
- marshal=解释器内部编译产物序列化器（pyc 的 code 对象），类型白名单窄（拒自定义类实例）、能存 code 对象（pickle 不行）、不承诺跨版本（pyc 靠 magic number 闸门）。
- 对象图差异：pickle memo 是协议级契约（共享/循环确定保真）；marshal 单次 dumps 内也实测保真但属实现细节，不赌跨版本；树形编译产物 marshal 更小更快。
- 选型三契约：marshal 保结构值（编译缓存+版本戳自校验）、pickle 保对象图（可信环境）、JSON 保互操作（不可信外部）；marshal.loads 不执行代码但也不该接不可信数据。

## 复盘追问
- 为什么 pyc 不能给旧版本解释器读、升级后要清缓存？（marshal 格式随实现自由变化，magic number 是唯一闸门；编译缓存必须带版本戳并在升级 runbook 清空）
- marshal 与 pickle 在"两个键共享同一个对象"上行为差在哪？（marshal 展开成两份丢 identity；pickle memo 还原同一对象；依赖身份的语义用 marshal 会隐性 bug）
