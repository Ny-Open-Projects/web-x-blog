---
title: "[Q5190] os.replace 原子替换与目录 fsync：0 字节配置文件事故"
date: 2026-11-23
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5190 · os.replace 原子替换与目录 fsync：0 字节配置文件事故

难度：P7 ｜ 标签：os.replace、fsync、原子写、崩溃一致性、inode

**问**：配置热更新直接 `open(path, "w").write(...)`，为什么会出现"读到半截 JSON"甚至"文件变成 0 字节"？改成"写临时文件 + `os.replace`"是不是就万无一失了？为什么还要 fsync 目录？已经在跑的服务读到的是新内容还是旧内容？

**答**：
结论：原地写会先 truncate 再写，两步之间读者看到的可能是空文件或半截内容，进程在写完前被杀就留下 0 字节。`os.replace` 在同文件系统内是一次 rename 系统调用，**可见性**上原子：任何时刻 open 都只会拿到旧的完整文件或新的完整文件。但原子 ≠ 持久：a) 临时文件内容没 `fsync` 时，掉电后可能"新文件名指向未落盘的数据"，表现为 0 字节或垃圾；b) rename 改了父目录的目录项，目录项本身没 `fsync` 时，崩溃后这次 rename 可能"回滚"，看起来像更新没发生。所以完整套路是：写临时文件 → `fsync(文件)` → `os.replace` → `fsync(目录)`。

取舍：fsync 的代价是真实 IO 延迟（机械盘几 ms、云盘可能几十 ms），热路径上每次写都 fsync 会拖慢；折中是"关键状态（配置/账本）必须 fsync，可重建的缓存文件可以不"。跨文件系统时 rename 会 `EXDEV`，必须先复制再替换，且不再原子；临时文件必须与目标同目录（同 mount），放 `/tmp` 常踩这个坑。

实战：事故形态是"配置中心下发后，两个 pod 一个读到新配置、一个读到 0 字节，重启后自愈；日志里有一瞬间的 JSONDecodeError"。旧进程的行为也常被误解：已打开旧 inode 的读者会**继续读旧内容**，因为 rename 只是把目录项指向新 inode，老 fd 不受影响——所以热更新必须配合"重开文件/发信号"的通知机制。下面演示替换的原子性、旧句柄读旧内容、inode 更换、以及三步 fsync 的写法。

```python
import os
import tempfile

d = tempfile.mkdtemp()
target = os.path.join(d, "config.json")

with open(target, "w", encoding="utf-8") as f:
    f.write('{"version": 1}')
old_fd = os.open(target, os.O_RDONLY)  # 已经打开的旧文件句柄
ino_before = os.stat(target).st_ino

tmp = os.path.join(d, ".config.tmp")
fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
os.write(fd, b'{"version": 2}')
os.fsync(fd)                # 1) 数据真正落盘，否则 rename 后可能读到 0 字节
os.close(fd)

os.replace(tmp, target)     # 2) 同目录 rename：原子替换，读者只会看到旧版或新版
dir_fd = os.open(d, os.O_RDONLY)
os.fsync(dir_fd)            # 3) 目录项也要 fsync，否则崩溃后 rename 可能"没发生"
os.close(dir_fd)

print("旧句柄仍读旧内容:", os.read(old_fd, 64))
os.close(old_fd)
with open(target, encoding="utf-8") as f:
    print("新 open 读新内容:", f.read())
print("临时文件已消失:", not os.path.exists(tmp))
print("inode 已更换:", os.stat(target).st_ino != ino_before)
```

**追问一**：`os.rename` 和 `os.replace` 有什么区别，为什么统一用后者？—— POSIX 上 rename 本来就会覆盖目标，两者等价；Windows 上 `rename` 在目标存在时抛 `FileExistsError`，`replace` 才覆盖。要写跨平台的原子替换，一律 `os.replace`。另外替换前要把临时文件权限设对（`os.open(..., 0o600)` 或 `os.chmod`），否则可能把 0644 的配置换成 0600，服务重启后读不了。

**追问二**：只 fsync 文件不 fsync 目录，最坏会怎样？—— 掉电后可能观察到三种状态：旧的完整文件、新的完整文件、以及"目标存在但大小为 0"（数据未落盘而目录项已更新）。最隐蔽的是第三种：程序看到文件存在、读到空内容，如果代码把"空"当合法值（比如空配置 / 空账本），就会静默丢一轮数据。监控上表现为"版本号回退"而不是报错，只能靠"写入前后记录版本 + fsync 后校验"来兜。

## 背诵要点
- 原地写 = truncate + write，非原子；`os.replace` 同 mount 内原子（读者只见旧或新），跨 mount 直接 EXDEV。
- 持久化三步：`fsync(临时文件)` → `os.replace` → `fsync(目录)`；缺任一都可能得到 0 字节或 rename 回滚。
- 已打开旧 inode 的进程继续读旧内容，热更新必须显式重开/通知。

## 复盘追问
- 热更新后偶发 0 字节配置，如何用 truncate、fsync、目录项三层解释并给出正确写入序列？（原子写 + 两次 fsync）
- 为什么 `os.replace` 之后老进程还在用旧配置？（inode 语义、fd 指向、通知机制）
