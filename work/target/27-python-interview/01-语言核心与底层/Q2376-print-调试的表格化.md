---
title: [Q2376] print 调试的表格化
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2376 · print 调试的表格化

> 难度:★★☆☆☆ | 标签:print 调试, 可读性, debug

**问**:不用调试器,纯 print 调试怎么打出「能看」的信息?

**答**:print 调试的三个纪律:一是表格化——用 f-string 定宽对齐(`{name:<10}{value!r:>20}`)输出「阶段 + 变量名 + repr」的行,多轮循环的状态变化一眼可比,散乱的 print 只能逐行脑内对齐;二是节流——只在关键轮次或状态变化时打印(`if i % 2 == 0`),全量打印会淹没信号;三是可开关——用环境变量或模块常量控制调试输出,而不是删 print(下一轮还要用),`DEBUG=1 python x.py` 随开随关。配套细节:值一律用 repr(字符串显式带引号、能看出空格与制表符),str 会把不可见字符藏起来;调试行带阶段标记(step3)方便 grep。这套手法是调试器不可用(远程、容器、多进程)时的主力,也是读别人代码时插桩观察的最快路径。

```python
# file: code/01_语言核心与底层/q2376_print_debug_table.py
"""print 调试的表格化:对齐输出让多轮状态一目了然。"""
import os


def dump_vars(stage, **vars):
    """统一的调试快照:一行一个变量,定宽对齐。"""
    print(f"--- {stage} ---")
    for name, value in vars.items():
        print(f"  {name:<10} = {value!r:>28}")


def run_pipeline(nums):
    acc = 0
    out = []
    for i, v in enumerate(nums):
        acc += v
        out.append(acc * 2)
        if i % 2 == 0:            # 节流:只看偶数轮
            dump_vars(f"step{i}", i=i, v=v, acc=acc, out=out)
    return out


if __name__ == "__main__":
    result = run_pipeline([1, 2, 3, 4])
    print("最终:", result)

    DEBUG = os.environ.get("DEBUG")
    x = 42
    if DEBUG:
        print(f"[debug] x={x}")
    print("DEBUG 未设置时 [debug] 行不出现:", DEBUG is None)

    s = "a\tb"
    print("str :", s)
    print("repr:", repr(s))
```

**追问**:1) 为什么调试值要用 repr 而不是 str?——repr 显示类型边界与不可见字符(引号、\t、\n),str 会把它们渲染掉;调试信息的第一要求是「忠实」,repr 是默认选择。2) 表格化 print 的要点?——列宽按 repr 截断(reprlib,Q1835);对齐考虑显示宽(CJK/emoji,Q2351);字典/集合输出先 sorted 保证可复现(哈希序不稳)。3) 与结构化输出的关系?——临时插桩 print(..., file=sys.stderr)(Q2380);需要机器读时转 json.dumps(repr 不能 eval,Q1835);调试完删除或收敛到 logging.debug。4) 生产陷阱?——str 吃掉空格/换行让现场失真;调试输出进 stdout 破坏管道;repr 大对象卡死(没截断)。
