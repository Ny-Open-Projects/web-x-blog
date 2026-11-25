---
title: "[Q5211] exec/eval 的命名空间边界：globals 必须是真 dict，函数内 locals 不可达"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5211 · exec/eval 的命名空间边界：globals 必须是真 dict，函数内 locals 不可达

难度：P6 ｜ 标签：exec、eval、globals、locals、动态代码、作用域

**问**：在函数体内 `exec("z = local_x * 2")`，为什么拿不到局部变量 `local_x`？`exec` 的 `globals` 参数为什么必须是真正的 dict？`eval` 和 `exec` 在语句与表达式上怎么分工？动态代码的变量到底落在哪个命名空间？

**答**：
结论：`exec`/`eval` 编译时**只能看见两个命名空间**——globals 与 locals。在模块顶层两者相同；在函数体内，`locals()` 返回的是帧局部变量的**快照副本**，编译动态代码时 `local_x` 既不在 globals 也不在传入的 locals 里，直接 `NameError`。这是编译期名字解析模型决定的：普通函数的字节码用 `LOAD_FAST` 读槽位，而动态代码只有 `LOAD_NAME`/`LOAD_GLOBAL` 两条通用路径，永远够不到调用者帧的局部槽位。`globals` 参数必须是真 dict，因为解释器要把执行期写入的全局名字直接落到这个 dict 上（类型严格校验，传 list 会 TypeError）；`locals` 可以是任意映射，但只读使用。`eval` 只接受表达式（返回值即表达式值），`exec` 接受语句序列（返回 None，副作用全靠命名空间）。

取舍：a) 需要拿到局部数据进动态代码：显式构造 `exec(code, {"x": local_x})`，把值"装箱"进 globals，不要指望函数帧穿透；b) 动态代码产生的全局变量会污染传入的 globals dict——用一次性空 dict + `__builtins__` 限定，跑完即弃；c) 对性能敏感路径不要走 exec：每次调用都要重新编译，除非把 code 对象缓存起来；d) eval 处理表达式、exec 处理语句的分工要守住，不要用 `eval("func(" + arg + ")")` 拼语句级调用；e) 任何动态执行都是信任边界：模板来源不可信时换受限求值器（ast.literal_eval），这一卡只谈语义边界，安全面见 Q472/Q5149。

实战：事故形态是"插件系统在 handler 内 `exec(cfg_expr)` 引用局部上下文变量，本地一直好使（顶层 exec 侥幸同帧），迁到函数内后全部 NameError；修复改为显式传 `exec(expr, {"ctx": ctx_dict})`，同时给返回值加了 `exec` 产生的残留全局清理"。下面逐条验证。

```python
import builtins

code = "y = x * 2"

g = {"x": 21, "__builtins__": builtins}
exec(code, g)
print("[1] exec 的写入落在 globals:", "y" in g, "y =", g.get("y"))


def runner():
    local_x = 5
    try:
        exec("z = local_x * 2")  # 函数内: locals 不可达
    except NameError as e:
        print("[2] 函数内 exec 看不到局部变量:", e)


runner()

try:
    exec("a = 1", ["not", "a", "dict"])
except TypeError as e:
    print("[3] globals 必须是真 dict:", e)

ns = {"__builtins__": builtins}
print("[4] eval 只吃表达式:", eval("1 + 2 * 3", ns))
try:
    eval("a = 1")
except SyntaxError as e:
    print("[5] eval 拒绝语句:", type(e).__name__)
```

**追问一**：为什么函数内 `locals()` 返回的是快照，exec 写进去的名字却"消失"？—— 函数帧的局部变量存在于固定的槽位数组（`co_varnames`），CPython 出于性能不会实时同步到 dict；`locals()` 调用时把槽位**复制**成一份 dict 快照，之后你对这份快照的任何写入都不会回写槽位。所以 `exec("q = 1", globals(), locals())` 之后 `q` 只活在快照里，下一行 `q` 仍然 NameError。这也是 3.13 PEP 667 之前 Python 的著名语义暗坑（帧内省面见 Q5038）。

**追问二**：`exec(code, g)` 与 `exec(code)` 的 `__builtins__` 注入有什么差别？—— 不传 globals 时 exec 用**当前调用方的真 globals**，`__builtins__` 已在其中，动态代码可以直接用 `open`/`__import__` 等内建；显式传入自制 dict 时，解释器会自动补一个 `__builtins__` 键（默认完整内建模块），想收窄就得自己放一个"阉割版"模块或映射进去。注意这只是粗粒度收口，不是安全边界——内建里仍有 `getattr`/`__import__` 足以逃逸，真正的隔离只能靠子进程/受限环境，语义上分清"命名空间控制"与"沙箱"两层。

## 背诵要点
- 动态代码只见 globals+locals 两个空间，函数内 locals 是快照副本，局部槽位永远不可达 → 显式装箱传参。
- globals 必须真 dict（写入落点），eval 吃表达式、exec 吃语句，exec 返回 None。
- exec 的命名空间控制不是沙箱：内建逃逸面巨大，不可信输入走受限求值器或子进程。

## 复盘追问
- handler 内 exec 引用局部变量报 NameError，根因？（动态代码无 LOAD_FAST 路径，locals 快照不可回写）
- eval 和 exec 怎么选？（表达式返回值用 eval；语句/多行副作用用 exec，返回 None）
