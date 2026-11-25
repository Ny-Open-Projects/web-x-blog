---
title: "[Q5228] startswith/endswith 的元组参数与多后缀判定"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5228 · startswith/endswith 的元组参数与多后缀判定

难度：P5 ｜ 标签：startswith、endswith、元组参数、多扩展名、前缀分支、边界参数

**问**：`endswith` 接受多个候选后缀怎么写？`os.path.splitext` 处理不了 `a.tar.gz` 怎么办？`startswith` 的 `start` 窗口参数有什么用？往元组里塞空字符串会发生什么？

**答**：
结论：`str.startswith`/`str.endswith` 的第一个参数可以是**字符串或字符串元组**——`name.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))` 一行等价于 any 循环，且匹配按元组顺序短路。这是替代"长 or 链"和"正则"的最轻方案，C 层实现，快且零依赖。三个边界要点：①**大小写**——`endswith` 大小写敏感，文件名判定先 `lower()` 再比（但 lower 后与真实文件名无关，只用于类型判定）；②**复合扩展**——`os.path.splitext` 只切最后一个点（`a.tar.gz` 得 `.gz`），判定 `tar` 系必须 `endswith((".tar.gz", ".tar.bz2"))` 显式列全；③**start/end 窗口**——`startswith(元组, start)` 只看从 start 起的子串，配合 `len(s) - len(s.lstrip())` 可以跳过前导空白做"首词命令识别"，不用真的构造新字符串。致命边界：元组里混入**空字符串**会让判定恒 True——`"".endswith(("",))` 也是 True，因为任何串都以空串结尾；候选表来自配置时必须过滤空项。

取舍：a) 候选少（<10）且都是字面量：元组参数最优；b) 候选来自用户配置/动态集合：先 `tuple(x for x in cfg if x)` 消空项、统一 lower，再传入；c) 候选需要通配（`*.tar.*`）：升级到 `fnmatch`（Q1832 的 shell 通配语义），不要硬造 endswith 变体；d) 协议首词分支（HTTP 方法识别）：`startswith(元组)` 比 split 更省——不需要真的构造子串对象；e) 路径判定注意 `Path.suffix` 与 splitext 同样只取最后一段（Q2098 的 pathlib 解析陷阱），复合扩展场景都要显式。

实战：事故形态是"上传校验的扩展名白名单来自运营配置，某次配置多了一个空行产生的空串，白名单变成'全部放行'，任意可执行文件直传成功；修复为配置加载端过滤空项 + 单元测试覆盖空串边界"。下面演示元组判定、复合扩展、窗口参数与空串陷阱。

```python
# startswith/endswith 的元组参数与多后缀判定
print("[1] endswith/startswith 直接接元组, 等价于 any(s.endswith(x) for x in tup)")
suffixes = (".jpg", ".jpeg", ".png", ".webp")
for name in ("photo.JPG", "photo.png", "photo.gif"):
    print(f"    {name}: is_image={name.lower().endswith(suffixes)}")

print("[2] 多重压缩扩展: splitext 只切最后一个点, 双扩展要显式处理")
import os
for name in ("backup.tar.gz", "data.tar.bz2", "plain.txt"):
    print(f"    {name}: splitext={os.path.splitext(name)[1]!r}, tar 系={name.endswith(('.tar.gz', '.tar.bz2'))}")

print("[3] startswith 元组用于命令/协议前缀分支, 替代长 or 链")
prefixes = ("GET ", "HEAD ", "OPTIONS ")
for line in ("GET /a HTTP/1.1", "POST /b HTTP/1.1", "HEAD /c HTTP/1.1"):
    kind = next((p.strip() for p in prefixes if line.startswith(p)), "OTHER")
    print(f"    {line!r} -> {kind}")

print("[4] startswith(元组, start) 的窗口参数: 只看从 start 起的子串")
line = "  GET /x HTTP/1.1"
print("    lstrip 后匹配:", line.lstrip().startswith(prefixes))
print("    start 窗口:", line.startswith(prefixes, len(line) - len(line.lstrip())))

print("[5] 空字符串边界: ''.endswith(('.gz',)) 是 False, 元组里含 '' 则恒 True")
print("    ''.endswith(('',)) =", "".endswith(("",)), " (慎用空串入元组)")
```

**追问一**：为什么元组里混入空串会让 endswith 恒为 True？—— 数学语义：`s.endswith("")` 恒为 True（任何串都以空串结尾，匹配点是任意位置），元组匹配是 any，只要有一个空串成员整个判定就短路为 True。这解释了为什么"配置驱动的白名单"必须把空项、纯空白项在加载层过滤掉，而不是指望调用处的判定兜底。同类陷阱也存在于 `startswith(("",))`。白名单类逻辑的通用验收标准：给它一个空输入和一个全空白配置，结果必须是"拒绝"而不是"放行"。

**追问二**：前缀分支用 startswith 元组，和 `line.split()` 后比较，怎么选？—— startswith 窗口方案不构造子串对象、O(最长前缀) 即短路，适合热路径（协议解析、路由首段识别）；split 方案可读性好但会切出整行 token 数组，大流量下 GC 压力可观（Q2615 的调用开销构成）。工程上还有第三档：超高频协议解析直接按字节偏移比较（长度前缀帧，Q2907），startswith 属于"中等频度 + 可读性优先"的甜点位。判定失败时的降级分支记得显式写（next 的 default / else OTHER），隐式漏网比慢一点更危险。

## 背诵要点
- startswith/endswith 接元组 = any 短路匹配，C 层实现；先 lower 再比做类型判定。
- splitext 只切最后一个点，复合扩展（tar.gz）要显式 endswith 元组；空串入元组 → 恒 True。
- start 窗口参数避免构造子串；配置驱动的白名单必须过滤空项并测试空输入边界。

## 复盘追问
- 上传白名单因配置空串全部放行，怎么在两层修？（加载端过滤空项+测试空边界；判定端元组来自过滤后的 tuple）
- 协议首词识别为什么选 startswith(元组, start) 而不是 split？（不构造 token 对象、短路快；热路径省 GC）
