---
title: [Q2628] getopt vs argparse 的取舍:小脚本与正式 CLI 的分界
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2628 · getopt vs argparse 的取舍:小脚本与正式 CLI 的分界

> 难度:★★★☆☆ | 标签:getopt, argparse, CLI 设计

**问**:标准库里 getopt 和 argparse 都能解析参数,选型标准是什么?

**答**:`getopt` 是 C `getopt` 的直译,只做「切分选项与值」这一件事,返回 `(opts, args)` 后全靠手写处理——没有帮助文本、没有类型转换、没有错误提示,解析失败还要自己捕获 `getopt.GetoptError`。`argparse` 则是声明式:加参数即自动生成 `-h` 帮助、类型校验、默认值、缺参报错(自带 SystemExit 和 usage 信息),还支持子命令与互斥组。选型一句话:一次性内部脚本、选项不超过两三个且格式简单,`getopt` 十几行搞定;任何要活过一个月、给别人用的 CLI,直接 `argparse`,它省下的错误处理代码远超声明的几行。两者混用的唯一理由是移植遗留代码。

```python
# file: code/01_语言核心与底层/q2628_getopt_vs_argparse.py
"""getopt 与 argparse 的同一需求两种写法对照。"""
import argparse
import getopt
import sys


def run_getopt(argv):
    """getopt:手动切分,手写错误。"""
    try:
        opts, args = getopt.getopt(argv, "vo:", ["verbose", "output="])
    except getopt.GetoptError as exc:
        return f"解析失败: {exc}"
    out = {"verbose": False, "output": None}
    for opt, val in opts:
        if opt in ("-v", "--verbose"):
            out["verbose"] = True
        elif opt in ("-o", "--output"):
            out["output"] = val
    return out, args


def build_argparse():
    """argparse:声明即文档。"""
    p = argparse.ArgumentParser(description="演示")
    p.add_argument("-v", "--verbose", action="store_true")
    p.add_argument("-o", "--output")
    p.add_argument("files", nargs="*")
    return p


if __name__ == "__main__":
    argv = ["-v", "--output=out.txt", "f1", "f2"]
    print("getopt:", run_getopt(argv))

    ns = build_argparse().parse_args(argv)
    print("argparse:", ns.verbose, ns.output, ns.files)
```

**追问**:1) argparse 遇到非法参数会直接退出吗?——会打印 usage 与错误信息后抛 SystemExit(退出码 2),适合 CLI 顶层;库代码里要可编程式处理时应先 parse_known_args 或自建 parser 捕获。2) 取舍的分界?——getopt:C 风格、极简、几行脚本;argparse:子命令/类型校验/help 自动生成;click/typer:组合式与类型注解风格;正式 CLI 不手写 usage 文本。3) 退出码协议?——argparse 错误 exit 2;业务错误自定 1;0 成功(Q1560);SystemExit 在测试中要 pytest.raises。4) 生产陷阱?——库代码 import argparse 直接退出(把 CLI 行为带进库);getopt 手写 usage 维护烂;--version/help 没有接 dest/退出语义。
