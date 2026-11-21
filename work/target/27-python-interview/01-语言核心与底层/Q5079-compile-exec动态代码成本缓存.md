---
title: [Q5079] compile/exec 动态代码的成本与缓存
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5079 · compile/exec 动态代码的成本与缓存

> 难度:★★★☆ | 标签:成本工程, 动态执行, compile

**问**：规则引擎/模板系统用 `eval`/`exec` 按请求编译表达式，为什么 P99 会出现周期性毛刺？`compile()` 的产物怎么复用、编译缓存怎么自建？`eval` 与 `exec` 的沙箱边界是什么、为什么"限制 builtins"挡不住逃逸？

**答**：结论：每次 `eval(expr)` 的成本 = **词法/语法解析 + AST 构建 + 编译成 code object**，这一步远比执行贵（小表达式编译≈几十微秒，执行可能只有 1 微秒），按请求编译等于把最贵的部分放在了热路径；毛刺来自 dict 缓存满后重建/清空、或表达式基数失控导致缓存命中率抖动。正确姿势：a) `compile(expr, "<expr>", "eval")` 得到 code object，**进程内缓存 code object**（LRU 限定基数，expr→code），执行态 `eval(code, glob, loc)` 只剩执行成本，稳态提升一个数量级；b) `compile` 的 flags 可传 `ast.PyCF_ONLY_AST` 拿 AST 做静态校验/白名单检查（只允许 Call/Name/BinOp 等节点、禁 Attribute 到 dunder），这比字符串黑名单可靠；c) 沙箱边界：`eval("()().__class__...")` 经典逃逸链说明**禁 builtins + 传空 globals 远不是沙箱**——对象图可达性（`__class__`/`__subclasses__`/`__globals__`）总能拿到 os.system；真要安全用 AST 白名单 + 无 Attribute/无 subscript 的极小语法子集，或者干脆换受控 DSL（如 simpleeval 思路、jsonpath），红线是**用户输入永不进 exec 桌面级沙箱**；d) `exec` 的 globals 默认继承调用者帧，`exec(code, {})` 才会建独立命名空间，且 `__builtins__` 会被自动注入——想剥也剥不干净，再次说明它不是安全边界。实战：表达式基数要**预估上限并监控缓存命中率**，超限走降级（拒绝+告警）而不是无限缓存。

```python
# file: code/01_语言核心与底层/q5079_compile_exec.py
import ast, time, timeit, sys
from collections import OrderedDict

# 1) 成本对比: 每次字符串 eval vs 缓存 code object
expr = "price * qty * (1 - discount) if qty > 0 else 0"
env = {"price": 3.0, "qty": 12, "discount": 0.1}

def make_env():                     # eval/exec 的执行环境
    return dict(env), {}

t0 = timeit.timeit(lambda: eval(expr, *make_env()), number=50000)
code = compile(expr, "<expr>", "eval")
t1 = timeit.timeit(lambda: eval(code, dict(env)), number=50000)
print(f"字符串 eval: {t0*20:.0f}us/千次 | compile 后 eval(code): {t1*20:.0f}us/千次")

# 2) LRU code 缓存: 预估基数上限 + 命中率
class CodeCache(OrderedDict):
    def __init__(self, cap=1024):
        super().__init__(); self.cap = cap; self.hit = self.miss = 0
    def get_code(self, src):
        if src in self:
            self.hit += 1; self.move_to_end(src); return self[src]
        self.miss += 1
        c = compile(src, "<expr>", "eval")
        self[src] = c
        if len(self) > self.cap: self.popitem(last=False)
        return c

cache = CodeCache(cap=64)
for _ in range(100):
    for k in range(10):             # 10 个表达式反复跑 -> 全命中
        eval(cache.get_code(f"x * {k}"), {"x": 2})
print(f"缓存命中 {cache.hit} / 未命中 {cache.miss} (基数 10 << cap 64)")

# 3) AST 白名单: 编译前静态校验, 拒绝属性访问与双下划线
ALLOW = (ast.Expression, ast.BinOp, ast.Num, ast.Constant, ast.Name,
         ast.Load, ast.Add, ast.Mult, ast.Sub)
def safe(src):
    tree = compile(src, "<expr>", "eval", ast.PyCF_ONLY_AST)
    for node in ast.walk(tree):
        if not isinstance(node, ALLOW) or isinstance(node, ast.Attribute):
            raise ValueError("不在白名单: " + type(node).__name__)
    return tree

print("白名单通过:", ast.dump(safe("a + b * 2"), include_attributes=False)[:40], "...")
try:
    safe("().__class__.__base__")   # 经典逃逸链, AST 层直接拒
except ValueError as e:
    print("逃逸链被 AST 白名单拦截:", e)

# 4) exec 不是沙箱: __builtins__ 自动注入
g = {}
exec("assert __builtins__ is not None", g)
print("exec 注入 __builtins__:", "__builtins__" in g)

print("python:", sys.version.split()[0])
```

**追问**：1) 为什么不用 `lru_cache` 包一层 compile？——可以（`@lru_cache(compile...)` 思路），但需要可控点：cap 要按表达式基数预估，命中/未命中要可观测（lru_cache_info 可拿 stats）；更重要的是缓存键要包含编译 flags 与 filename，否则不同用途的 code object 会串。2) `compile` 编译出的 code object 能 pickle 吗？——不能直接（code object 不可 pickle，3.12 前 marshal 可以序列化但跨版本不保证兼容），跨进程共享编译产物的可行做法是子进程各自编译，或把表达式落到磁盘当模块 import 走 pyc 缓存机制。3) `ast.literal_eval` 能替代这套吗？——只覆盖字面量（list/dict/数字/字符串），不支持变量与运算符语义，适合"用户给常量结构"的场景；规则引擎要变量代入就必须 compile + 受控环境。

## 背诵要点
- eval/exec 每次调用都走解析+编译，成本远高于执行；热路径必须 `compile()` 一次缓存 code object，稳态提升一个数量级。
- 安全是 AST 白名单问题不是命名空间问题：禁 builtins 挡不住 `__class__` 逃逸链，exec 还会自动注入 `__builtins__`。
- 缓存要定 cap + 监控命中率，基数失控时降级拒绝；code object 不可 pickle，跨进程共享走 marshal（版本敏感）或各自编译。

## 复盘追问
- 你们的规则表达式基数有多少？缓存命中率有没有指标，毛刺时段命中率是多少？（提示：把 get_code 的 hit/miss 打成指标，毛刺与 miss 率对齐时间轴）
- 有没有安全评审过 eval 入口的表达式来源？如果规则由租户提交，你的拦截层在哪一层？（提示：AST 白名单 + 语法子集 + 超时中断（signal/settrace 限步数），三层都要）
