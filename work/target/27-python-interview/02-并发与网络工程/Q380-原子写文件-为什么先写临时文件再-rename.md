---
title: [Q380] 原子写文件:为什么先写临时文件再 rename
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q380 · 原子写文件:为什么先写临时文件再 rename

> 难度:★★★ | 标签:文件 IO, 原子性, fsync

**问**:直接 `open(path, "w")` 覆盖配置文件有什么风险?如何原子地写文件?

**答**:写一半时进程崩溃/断电,文件就是截断的半成品,读它的进程会挂。原子写姿势:①写到同目录临时文件(保证同一文件系统);②`flush` + `os.fsync` 落盘;③`os.replace(tmp, path)`——rename 在 POSIX 上是原子操作,读者要么看到旧文件要么看到新文件。注意必须用 `os.replace` 而非 `os.rename`(Windows 跨设备/覆盖行为不同,replace 跨平台语义正确)。

```python
# file: code/02_并发与网络工程/q380_atomic_write.py
"""原子写文件:tempfile + fsync + os.replace。"""
import json
import os
import tempfile


def atomic_write(path, data: str, encoding="utf-8"):
    dir_ = os.path.dirname(os.path.abspath(path)) or "."
    fd, tmp = tempfile.mkstemp(dir=dir_, prefix=".tmp_")
    try:
        with os.fdopen(fd, "w", encoding=encoding) as f:
            f.write(data)
            f.flush()
            os.fsync(f.fileno())  # 强制落盘,防断电丢数据
        os.replace(tmp, path)     # 原子替换,读者不会看到半成品
    except BaseException:
        os.unlink(tmp)            # 失败清理临时文件
        raise


if __name__ == "__main__":
    path = "/tmp/app_config.json"
    atomic_write(path, json.dumps({"version": 1, "host": "db-1"}))
    with open(path) as f:
        print("read back:", f.read())
    # 重复原子写,模拟更新
    atomic_write(path, json.dumps({"version": 2, "host": "db-2"}))
    with open(path) as f:
        print("updated  :", f.read())
```

**追问**:
- 为什么临时文件必须和目标同目录?`os.replace` 的原子性只在同一文件系统内成立,跨文件系统会退化为拷贝+删除。
- 追加写是原子的吗?小于 PIPE_BUF 的 append 在 POSIX 下对并发写基本原子,但更大写入可能交错,多进程写同一日志建议进程各写各文件或加锁。
