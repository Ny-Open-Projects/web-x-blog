---
title: [Q2611] pyc 的失效判定:mtime、size 与 PEP 552 头部
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2611 · pyc 的失效判定:mtime、size 与 PEP 552 头部

> 难度:★★★☆☆ | 标签:pyc, import, 字节码缓存

**问**:Python 怎么知道 `.pyc` 缓存还能不能用?缓存失效的判定依据是什么?

**答**:每个 pyc 文件开头有 16 字节头部(PEP 552):4 字节 magic number、4 字节 flags、4 字节源文件 mtime、4 字节源文件大小。默认 flags 为 0,走时间戳校验:import 时比较头部记录的 mtime 和 size 与源文件当前 `stat` 结果,任一不符就重新编译并回写,否则直接加载缓存字节码。这套机制解释了几个常见现象:只改文件内容但字节数恰好相同且 mtime 未变,理论上可能吃到陈旧缓存(mtime 精度问题,少见);`PYTHONDONTWRITEBYTECODE=1` 只是不写缓存,读取不受影响;顶层脚本永不走 pyc,只有被 import 的模块才缓存。若 flags 置位走 PEP 552 的 hash-based 校验,则直接比较源内容哈希,mtime 无关,适合 mtime 不可靠的构建系统。

```python
# file: code/01_语言核心与底层/q2611_pyc_header.py
"""pyc 失效判定:解析 16 字节头部,对照源文件 stat。"""
import importlib.util
import os
import py_compile
import struct
import tempfile


def read_pyc_header(pyc_path):
    raw = open(pyc_path, "rb").read(16)
    magic, flags, src_mtime, src_size = struct.unpack("<IIII", raw)
    return magic, flags, src_mtime, src_size


if __name__ == "__main__":
    tmp = tempfile.mkdtemp()
    src = os.path.join(tmp, "m.py")
    with open(src, "w") as f:
        f.write("VALUE = 1\n")

    pyc = py_compile.compile(src)
    magic, flags, src_mtime, src_size = read_pyc_header(pyc)
    st = os.stat(src)

    print("缓存路径:", pyc)
    print("magic 匹配解释器:",
          magic == struct.unpack("<I", importlib.util.MAGIC_NUMBER)[0])
    print("flags(0 即时间戳校验):", flags)
    print("mtime 一致:", src_mtime == int(st.st_mtime))
    print("size 一致:", src_size == st.st_size)

    # 模拟源文件变更:mtime 后移,头部立刻过期
    old = st.st_mtime
    os.utime(src, (old - 1000, old - 1000))
    _, _, src_mtime, _ = read_pyc_header(pyc)
    print("源文件回拨后 mtime 一致:",
          src_mtime == int(os.stat(src).st_mtime), "-> 触发重编译")
```

**追问**:1) 为什么 Python 不直接缓存哈希而默认用 mtime?——stat 一次比读全文算哈希便宜得多,对绝大多数工作流 mtime 已足够;hash-based 模式是给 mtime 不可信的场景(如可重现构建)留的开关。2) PEP 552 的三种模式?——默认 mtime+size;unchecked hash(源码哈希,信任输入);checked hash(每次导入验哈希,防篡改,用于只读部署/可重现构建);PYTHONDONTWRITEBYTECODE 禁写。3) 部署相关性?——同 mtime 部署(打 tar 保时间)会让旧 pyc 活着;CI 与生产的 PYTHONPYCACHEPREFIX 缓存分离;3.13 后 __pycache__ 加速更明显但机制不变。4) 生产陷阱?——mtime 相同的旧 pyc 被加载(诡异行为来源);只读容器没预编译 pyc 启动慢;checked-hash 开销误用于开发环境。
