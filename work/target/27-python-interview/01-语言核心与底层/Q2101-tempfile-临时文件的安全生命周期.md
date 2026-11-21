---
title: [Q2101] tempfile:临时文件的安全生命周期
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2101 · tempfile:临时文件的安全生命周期

> 难度:★★☆☆☆ | 标签:tempfile, 临时文件, 资源管理

**问**:为什么不要自己用 open("/tmp/xx") 建临时文件?tempfile 的三种姿势怎么选?

**答**:自建临时文件有可预测文件名撞车与权限过宽两个安全问题,tempfile 的家族函数全部随机命名且默认 0600 权限(只有属主可读)。三种姿势按生命周期选:TemporaryDirectory 配 with,目录及内容在块结束自动递归清理,是批处理任务的默认选择;NamedTemporaryFile 单文件、with 结束即删,注意 Windows 上关闭后重打开受限,跨平台任务要小心;mkstemp 最底层,返回 (fd, path) 让你完全掌控生命周期——fd 要自己 os.fdopen 包装、文件要自己删,适合「临时文件要活过当前函数」的场景,demo 里 finally 里的 os.remove 就是自管生命周期的代价与责任。原则:能交给 with 就别手动管。

```python
# file: code/01_语言核心与底层/q2101_tempfile_lifecycle.py
"""tempfile:临时资源的安全生命周期与自动清理。"""
import os
import pathlib
import tempfile


if __name__ == "__main__":
    with tempfile.TemporaryDirectory(prefix="job-", suffix=".d") as tmp:
        work = pathlib.Path(tmp) / "out.txt"
        work.write_text("hello", encoding="utf-8")
        print("目录内写入:", work.read_text())
    print("with 结束自动清理:", not pathlib.Path(tmp).exists())

    fd, path = tempfile.mkstemp(suffix=".json")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write("{}")
        print("mkstemp 需自管生命周期:", pathlib.Path(path).stat().st_size, "字节")
    finally:
        os.remove(path)
    print("手动删除后:", not os.path.exists(path))

    with tempfile.NamedTemporaryFile("w+", suffix=".log", delete=True) as nf:
        nf.write("log line")
        nf.flush()
        print("NamedTemporaryFile 随 with 结束删除:", nf.name)
```

**追问**:1) 为什么 mkstemp 更底层却更常用于库代码?——返回 fd 让调用方决定包装与生命周期,避开 NamedTemporaryFile 在 Windows 上重打开受限的问题;临时文件权限?——默认 0600,防共享目录下的信息泄露,自建 open 给不出这个保证。2) 安全三要素?——唯一文件名(防预测竞态)、0600 权限(防共享目录泄露)、确定性清理(TemporaryDirectory 上下文或 try/finally unlink)。3) 生命周期管理?——with TemporaryDirectory() 自动清;mkstemp 配 os.close + os.unlink;进程崩溃残留靠启动期清理目录。4) 生产陷阱?——固定文件名临时文件(符号链接攻击/竞态);忘 unlink 堆积;tmp 目录跨进程共享时权限错;Windows 重开限制。
