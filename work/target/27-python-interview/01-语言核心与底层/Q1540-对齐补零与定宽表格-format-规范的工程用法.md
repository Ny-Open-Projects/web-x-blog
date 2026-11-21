---
title: [Q1540] 对齐补零与定宽表格:format 规范的工程用法
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1540 · 对齐补零与定宽表格:format 规范的工程用法

> 难度:★★☆☆☆ | 标签:格式化, 对齐, 输出

**问**:输出对齐报表时,ljust/rjust/center/zfill 与 format 规范怎么选?补零为什么要小心负数?

**答**:两套工具,推荐统一走 format 规范:[[fill]align][sign][#][0][width][,][.precision][type],一次表达对齐+填充+精度+类型;方法族 ljust/rjust/center/zfill 适合单步快速操作,与 format 一一对应(f"{s:<6}" 等价 s.ljust(6))。补零要点:① 数字用 0>width 或 08.2f,符号感知——零插在符号与数字之间;② 字符串 zfill 也处理 +/- 前缀,但非数字串补零要显式 fill 加对齐方向;③ 补零的经典用途是「位数对齐的排序键」(part-0001 < part-0023),不补零字典序会乱。中文全角混排表格:Python 按码点计数而终端按显示宽度渲染,需要按 unicodedata.east_asian_width 自算宽度,标准库没有现成方案。

```python
# file: code/01_语言核心与底层/q1540_align_and_pad.py

ROWS = [
    ("q1526", 3, 0.874),
    ("q1528", 4, 23.5),
    ("q1540", 2, 6.125),
]


def render_table(rows):
    header = f"{'id':<8}{'level':>7}{'score':>10}"
    lines = [header, "-" * len(header)]
    for qid, level, score in rows:
        lines.append(f"{qid:<8}{level:>7}{score:>10.3f}")
    return "\n".join(lines)


if __name__ == "__main__":
    print(render_table(ROWS))

    # 补零:位数对齐的排序键(不补零字典序会乱)
    parts = [("part", 1), ("part", 23), ("part", 4)]
    keys = [f"{name}-{num:04d}" for name, num in parts]
    print("sorted keys:", sorted(keys))

    # 方法族与 format 的等价关系
    s = "py"
    print(s.ljust(6, "."), "|", f"{s:.<6}")
    print(s.rjust(6, "_"), "|", f"{s:_>6}")
    print(s.center(7, "*"), "|", f"{s:*^7}")

    # 数字补零符号感知 vs 字符串 zfill
    print("format zero:", f"{-3.5:08.2f}")
    print("zfill      :", "-3.5".zfill(8), "|", "42".zfill(5))
```

**追问**:1) 中英文混排的表格为什么总对不齐?——Python 按码点计数,全角字符显示宽度是 2;要按 unicodedata.east_asian_width 自算显示宽度或引入 wcwidth。2) format 规范的工程要点?——数值 :>10.2f/:,分组、文本 :<10、居中 :^、补零 :06d;动态宽度 f"{x:{w}}" 嵌套规格;对齐是「存储格式化」的职责,显示宽度另算。3) 宽度计算模型?——east_asian_width 的 W/F 算 2、Na/N/H 算 1;组合字符零宽;终端等宽假设仅在等宽字体+无组合字符时成立。4) 生产陷阱?——CJK 对齐问题在报表/CLI 输出普遍存在,用 wcwidth 或表格库(tabulate);把「len」当显示宽度;emoji/组合字符让宽度计算再次失准。
