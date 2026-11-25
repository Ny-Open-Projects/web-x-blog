---
title: "[Q5200] hashlib.file_digest：大文件摘要不必 read() 全量进内存"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5200 · hashlib.file_digest：大文件摘要不必 read() 全量进内存

难度：P6 ｜ 标签：hashlib、file_digest、流式摘要、内存水位、文件校验

**问**：上传回调里校验文件完整性，代码写的是 `sha256(open(path, "rb").read())`，2GB 的包直接把容器内存打爆。为什么 `read()` 会整块进内存？Python 3.11 的 `hashlib.file_digest` 解决了什么？它和手写 `while chunk := f.read(8192)` 有区别吗？有什么前提条件容易踩？

**答**：
结论：`f.read()` 不带参数会把整个文件读成 `bytes`，摘要函数再持有一份，峰值约为文件大小的 1.5～2 倍（读缓冲 + 摘要输入），2GB 文件足以触发 OOM。3.11 新增的 `hashlib.file_digest(fileobj, digest_name)` 内部用固定大小的缓冲循环 `readinto`，内存是常数级，且省掉 Python 层的循环开销。它与手写分块逻辑等价，但更快、更少出错（不需要自己处理短读、缓冲大小、`update` 顺序）。

取舍：a) 一次性小文件（几 MB 以内）直接 `read()` 最简单；b) 大文件用 `file_digest`，代码最短、无额外依赖；c) 需要"边读边解析"（比如解压同时校验）时手写 `read(chunk)` + `update`，因为 `file_digest` 会把文件读到 EOF，不能与解析共享同一次读取；d) 需要校验"传输中的流"（socket/请求体）时也只能手写 `update`。前提条件：文件对象必须是**二进制模式**，且摘要从**当前位置**开始算到 EOF——如果之前读过一段，结果不是全文件摘要；`file_digest` 也不关闭文件，谁 open 谁 close。

实战：事故形态是"夜间对账任务对 200 个 2GB 的备份包做 SHA256，串行跑时内存逐次上涨，最后被 OOM killer 杀掉，任务重跑又从头开始"。下面演示三种写法结果一致、`file_digest` 从当前位置起算，以及二进制/文本模式的差异。

```python
import hashlib
import os
import tempfile

data = b"payload-" * 100000
path = tempfile.mktemp(suffix=".bin")
with open(path, "wb") as f:
    f.write(data)

try:
    with open(path, "rb") as f:
        one_shot = hashlib.file_digest(f, "sha256").hexdigest()

    manual = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            manual.update(chunk)

    print("[1] file_digest 与分块一致:", one_shot == manual.hexdigest())
    print("[2] 与一次性 read 一致:", one_shot == hashlib.sha256(data).hexdigest())

    with open(path, "rb") as f:
        f.read(16)                                  # 先消费一段
        partial = hashlib.file_digest(f, "sha256").hexdigest()
    print("[3] 从当前位置起算，不等于全文件:", partial != one_shot)

    with open(path, "rb") as f:
        f.seek(0)
        print("[4] seek 回 0 后恢复全文件摘要:", hashlib.file_digest(f, "sha256").hexdigest() == one_shot)

    with open(path, "r", encoding="utf-8") as f:
        try:
            hashlib.file_digest(f, "sha256")
        except ValueError as e:
            print("[5] 文本模式不可用:", e)
finally:
    os.unlink(path)
```

**追问一**：`file_digest` 支持哪些摘要名？—— 任何 `hashlib.new(name)` 支持的名字都行（`"sha256"`、`"blake2b"`、`"md5"`……），底层会先 `hashlib.new()` 再流式喂数据。在 FIPS 模式下 `md5` 会被禁用，需要 `usedforsecurity=False` 才能用于非安全用途——但 `file_digest` 的签名没有这个开关，FIPS 环境要手写 `hashlib.new("md5", usedforsecurity=False)` + 分块 `update`。

**追问二**：为什么不用 `mmap` + `hashlib` 一次算？—— `mmap` 省掉用户态复制，但摘要仍然要顺序扫完整块内存，收益主要在"反复随机访问同一文件"；对"只读一遍算摘要"，页缓存已经让 `read` 足够快，`mmap` 反而多一层缺页与 SIGBUS 风险（文件被并发截断时）。大文件一次性摘要的最优解就是固定缓冲流式读，`file_digest` 把它做进了标准库。

## 背诵要点
- `read()` 无参 = 整文件进内存，峰值可达文件大小 2 倍；大文件必须流式摘要。
- `hashlib.file_digest(f, "sha256")` 是 3.11+ 的常数内存实现，等价于固定缓冲 `update` 循环，从当前位置算到 EOF。
- 必须二进制模式；不关闭文件；FIPS 下 md5 要 `usedforsecurity=False`（`file_digest` 不支持，需手写）。

## 复盘追问
- 对账任务逐个算 2GB 文件 SHA256 时内存爆掉，如何改？（`file_digest` / `read(chunk)` 循环）
- `file_digest` 算出的摘要与全文件不一致，可能是什么原因？（从当前位置起算、文本模式、文件被并发写）
