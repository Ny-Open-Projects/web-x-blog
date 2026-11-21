---
title: [Q1828] textwrap:帮助文本的换行、缩进与截断
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1828 · textwrap:帮助文本的换行、缩进与截断

> 难度:★★☆☆☆ | 标签:textwrap, CLI, 文案

**问**:CLI 帮助文本的自动换行、缩进与超长截断,textwrap 一次能给出什么?

**答**:三件套:① fill/dedent——fill 按 width 折行并给首行与续行不同缩进(initial_indent/subsequent_indent),dedent 剥离三引号字符串的公共前导空白,让文案源码里好读、输出时对齐;② shorten——按 width 截断加省略号、词边界优先,适合列表里的单行摘要;③ TextWrapper 实例可配 break_long_words、break_on_hyphens、max_lines,定制一次复用。工程习惯:帮助文案写进模块常量,出口统一走 textwrap,终端宽度用 shutil.get_terminal_size 动态取;中英混排注意 width 按字符数而非显示宽度,等宽对齐需求走 Q1540 的 format 对齐而不是 textwrap。

```python
# file: code/01_语言核心与底层/q1828_textwrap_help.py
"""textwrap:帮助文本的换行、缩进与截断。"""
import textwrap

BRIEF = ("本工具将大 CSV 文件按行数拆分为多个分片,"
         "支持自定义分隔符与编码,用于把大文件切成可并行处理的小块。")


def wrap_help(width=40):
    return textwrap.fill(BRIEF, width=width,
                         initial_indent="  ", subsequent_indent="  ")


def dedent_compare():
    raw = """\
        用三引号写的文档
        带着源码缩进粘进来。
    """
    return textwrap.dedent(raw)


def short_usage(width=30):
    return textwrap.shorten(BRIEF, width=width, placeholder="……")


if __name__ == "__main__":
    print(wrap_help())
    print("--- dedent ---")
    print(dedent_compare())
    print("--- shorten ---")
    print(short_usage())
```

**追问**:1) dedent 为什么有时剥不干净?——公共前缀按「非空白行」的最小缩进计算,首尾纯空白行忽略;某行缩进多一格或少一格,公共前缀变小,输出就会错位。2) wrap/fill 的关键参数?——width 行宽、subsequent_indent 续行缩进、break_long_words 超长词处理、drop_whitespace 空白折叠;CLI 帮助文本按终端宽减 margin 计算宽度。3) 与三引号文本的配合?——dedent 后再 strip 首尾;tab 与空格混用会让前缀判断失败(统一 expandtabs);段落内空行参与前缀计算吗——非空白行才参与。4) 生产陷阱?——缩进里混 tab(直接失效);把 wrap 当 re.sub 用(语义完全不同);截断显示要自己接省略号(textwrap.shorten 可做)。
