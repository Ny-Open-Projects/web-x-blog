---
title: [Q2636] Path.is_relative_to 与 commonpath:路径包含判定
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2636 · Path.is_relative_to 与 commonpath:路径包含判定

> 难度:★★★☆☆ | 标签:pathlib, 路径安全, 3.9 新特性

**问**:判断「某路径在不在指定目录之下」,为什么不能用 startswith?

**答**:字符串 `startswith` 会把 `/var/log/app2` 误判为 `/var/log/app` 的子路径——组件边界没对齐。3.9 的 `Path.is_relative_to` 按路径组件做前缀判定,语义正确且不用 `os.path.commonpath` 那样先统一绝对化;老式写法 `os.path.commonpath([base, p]) == base` 仍然可用,但要求两个都是绝对路径或都是相对路径,混用抛 ValueError。这个判定的安全用途是「路径逃逸校验」:处理用户上传的文件名、解压 zip 条目前,先归一化再校验是否仍在目标目录内,挡住 `../` 穿越。注意 `resolve()` 归一化符号链接后再判定才是真正防穿越的姿势。

```python
# file: code/01_语言核心与底层/q2636_path_is_relative.py
"""路径包含判定:is_relative_to、commonpath 与穿越校验。"""
import os
from pathlib import Path

if __name__ == "__main__":
    base = Path("/var/log/app")
    print("组件级包含:", base.joinpath("a.log").is_relative_to(base))
    print("字符串前缀误判:", "/var/log/app2".startswith("/var/log/app"))

    print("commonpath:", os.path.commonpath(["/var/log/app", "/var/log/app/x"]))
    try:
        os.path.commonpath(["/var/log/app", "relative/thing"])
    except ValueError as exc:
        print("混用绝对相对:", exc)

    # 穿越 校验:归一化后再判定
    suspicious = Path("/var/log/app/../..").resolve()
    print("归一化后仍在基目录内:", suspicious.is_relative_to(base))
```

**追问**:1) is_relative_to 需要两个路径都存在吗?——不需要,纯字符串/组件级运算,不碰文件系统,存在性是调用方的另一层检查。2) 与 commonpath 的分工?——is_relative_to 判定「A 在 B 之下」(3.9+ Path 方法,链式友好);os.path.commonpath 求公共祖先(可抛 ValueError 混盘);安全路径校验(防 ../ 逃逸)两者皆可用但要 resolve 后再判(Q2098)。3) 与 resolve 的配合?——比较前 resolve 消解 .. 与 symlink;否则攻击者用 .. 绕过判定;严格安全场景再 realpath。4) 生产陷阱?——未 resolve 就判包含(路径逃逸);跨盘混用 commonpath 崩;把相对路径直接判包含。
