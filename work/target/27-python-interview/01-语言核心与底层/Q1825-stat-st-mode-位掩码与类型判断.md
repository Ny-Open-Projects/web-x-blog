---
title: [Q1825] stat:st_mode 位掩码与类型判断
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1825 · stat:st_mode 位掩码与类型判断

> 难度:★☆☆☆☆ | 标签:stat, 文件系统, 位运算

**问**:os.path.isdir 之外,stat 模块直接读 st_mode 有什么不可替代的能力?

**答**:os.path 系列是 stat 的便捷封装,但 st_mode 一个字段同时编码「文件类型位」与「权限位」:低 9 位是三组 rwx,0o170000 掩码后的类型段用 S_ISDIR/S_ISREG/S_ISLNK 判定,stat.filemode 直接给出 -rw-r----- 风格的十字符串。用 stat 的三个理由:① 一次 os.stat 拿全信息——类型、权限、大小、时间戳、inode 同一笔系统调用,os.path 多次判断是多次 stat;② lstat 与 stat 区分「符号链接本身」与「目标」,os.path.isfile 跟随链接而 S_ISLNK(lstat 结果)识别链接本身,安全检查(防符号链接逃逸)必须用后者;③ 权限位按位与判断,比字符串比对便宜且准确。

```python
# file: code/01_语言核心与底层/q1825_stat_mode.py
"""stat 模块:st_mode 位掩码与类型判断。"""
import os
import stat as st
import tempfile


def describe(path):
    s = os.stat(path)
    kinds = [(st.S_ISDIR, "目录"), (st.S_ISREG, "普通文件"),
             (st.S_ISLNK, "符号链接")]
    kind = next(label for test, label in kinds if test(s.st_mode))
    return kind, st.filemode(s.st_mode), s.st_size


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as root:
        f = os.path.join(root, "a.txt")
        d = os.path.join(root, "sub")
        os.mkdir(d)
        with open(f, "w") as fh:
            fh.write("hello")
        os.chmod(f, 0o640)
        print("文件:", describe(f))
        print("目录:", describe(d))
        print("权限位:", oct(os.stat(f).st_mode & 0o777), "| 类型位:",
              oct(os.stat(f).st_mode & 0o170000))
```

**追问**:1) os.stat 对悬空符号链接会怎样?——跟随目标抛 FileNotFoundError,而 lstat 对链接本身永远成功;「这个链接存在吗」要用 lstat/os.path.lexists。2) st_mode 的判断工具?——stat.S_ISDIR/S_ISREG/S_ISLNK 按位掩码解析;mode 按位与权限位(S_IRUSR 等);三函数分工:stat 跟随目标、lstat 链接本身、fstat 已打开 fd。3) TOCTOU 竞态?——stat 与 open 之间目标可能被替换;安全敏感路径用 open(O_NOFOLLOW) 或先 fd 后 fstat;检查与使用要原子化。4) 生产陷阱?——悬空链接让「存在性检查」误判;符号链接跟随被用于路径逃逸(安全);跨平台权限位语义差异。
