---
title: [Q5132] assert 在 -O 下的剥离语义与成本
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5132 · assert 在 -O 下的剥离语义与成本

难度：P6 | 标签：assert、-O 字节码、成本工程、契约校验

**问**：面试官问：为什么说"用 assert 做入参校验是成本与正确性双输"？请从 `-O`/`-OO` 的字节码语义、运行成本两个层面解释，并给出生产代码里校验的正确写法。

**答**：

**结论**：`assert cond, msg` 在编译期受 `__debug__` 开关控制：`python -O` 时 `__debug__` 为 False，整个 assert 语句（含副作用表达式和 msg 的求值）被编译器直接丢弃，不产生任何字节码。因此 (1) 用 assert 做业务校验，在优化模式下校验凭空消失，非法输入静默通过；(2) assert 失败抛的是 `AssertionError` 且可被 `python -OO` 连 docstring 一起剥掉，不适合作为 API 契约。

**取舍**：assert 的正确定位是"开发期内部不变量"，它省下的是生产环境的条件判断字节码——这是它唯一的成本优势。需要永远生效的校验用 `if not cond: raise ValueError/TypeError`；需要格式化消息又怕提前求值贵的，惰性拼接即可。另外注意 assert 里的副作用（如 `assert self._flush()`）在 -O 下连带不执行，是最隐蔽的一类 bug。

**实战**：成本角度，普通 `if cond` 每次调用都是一次 POP_JUMP_IF_FALSE，代价纳秒级；真正贵的场景是 assert msg 里做了 f-string 拼接或函数调用——不过 -O 下它反而免费了。工程结论：热路径上"必须成立"的条件用 assert 表达意图，"可能被外部违反"的条件用显式 raise，两者语义边界写进 code review 清单。

```python
import dis, subprocess, sys, tempfile, os

src = "x = 1\nassert x == 2, f'bad value {x!r}'\nprint('passed')\n"
d = tempfile.mkdtemp(); f = os.path.join(d, "a.py")
open(f, "w").write(src)

# 1) 默认模式：assert 生效
r0 = subprocess.run([sys.executable, "-I", f], capture_output=True, text=True)
print("normal   ->", r0.returncode, r0.stderr.strip().splitlines()[-1])

# 2) -O：assert 整句被剥离，程序正常跑完
r1 = subprocess.run([sys.executable, "-I", "-O", f], capture_output=True, text=True)
print("-O       ->", r1.returncode, r1.stdout.strip())

# 3) 字节码证据：__debug__ 是编译期常量
def check(x):
    assert x > 0, "must be positive"
    return x
dis.dis(check)
print("__debug__ =", __debug__)
```

**追问 1**：`-OO` 与 `-O` 的区别是什么？
答：`-OO` 在 `-O` 基础上再删除 docstring（`.pyc` 文件名带 `opt-2` 标记）。依赖 docstring 的框架特性（如某些 CLI 的帮助文本）会在 -OO 下失效，部署镜像如果统一加 `-OO` 要做全量回归。

**追问 2**：如何在运行时检测当前是否处于优化模式？
答：读 `__debug__` 常量即可（编译期确定）；更好的做法是不写依赖该值的分支逻辑，把"校验永远生效"的部分直接写成 raise，让两种模式行为一致。

**追问 3**：assert 的消息表达式在非优化模式下何时求值？
答：仅在条件为 False 时才求值 msg（字节码里 msg 在跳转目标分支上），所以 `assert cond, expensive()` 的昂贵消息在正常路径没有成本——但别在 cond 表达式本身里塞副作用。

## 背诵要点

- `python -O` 使 `__debug__=False`，assert 连同 msg 求值在编译期整体剥离，字节码里根本不存在。
- assert 只表达"内部不变量"，外部输入校验必须 `if not cond: raise`，否则 -O 下静默失效。
- `-OO` 额外删除 docstring，依赖 docstring 的功能在优化镜像里会二次翻车。

## 复盘追问

- 团队规范如何防止 assert 被滥用为校验？CI 里能加什么检查？(提示：grep assert 后跟 raise 语义 + 灰度用 -O 跑测试)
- 为什么说 assert 副作用 bug 在测试环境发现不了？(提示：pytest 默认不启用 -O)
