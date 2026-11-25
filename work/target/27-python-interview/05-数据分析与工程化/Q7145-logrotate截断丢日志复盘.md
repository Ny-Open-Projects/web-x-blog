---
title: [Q7145] logrotate 截断丢日志复盘
date: 2026-11-21
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7145 · logrotate 截断丢日志复盘

难度：P6-P7 | 标签：logging、logrotate、事故复盘

**问**：运维配了 logrotate 用 `copytruncate` 轮转应用日志，之后每天凌晨轮转点附近总有一批日志"消失"。为什么 copytruncate 会丢日志？与 `postrotate+reopen` 方案怎么选？

**答**：结论：copytruncate 的流程是"复制旧文件→把原文件截断为 0"，**复制与截断之间的窗口里应用写入的内容直接丢失**；且高 QPS 应用写文件时，截断后旧的文件偏移量（应用持有的 fd 指针继续前移）会产生稀疏大文件与乱序。正确姿势是**信号重开**：应用在收到 USR1/SIGHUP（或 logging 内部 RotatingFileHandler）后 reopen 文件，logrotate 用 `mv` 原子改名 + `postrotate killall -USR1 app`——没有任何写入窗口会丢。

实战要点：
1. 判别法：应用是否持有日志 fd 一直写？是→必须走"改名+reopen"；仅短命进程按次写文件才可接受 copytruncate。
2. Python 侧落地：`logging.handlers.WatchedFileHandler` 会自动检测 inode 变化并重开，是对接 logrotate `create/mv` 模式的标配；自己管理 fd 则要在信号处理器里 `handler.reopen()`。
3. 容器里不该用 logrotate：日志进 stdout，交给采集器（Q7127 管道背压另算），文件轮转是宿主机时代的方案。

```python
"""WatchedFileHandler 对 inode 轮转的自愈（标准库，可运行）"""
import logging
import logging.handlers
import os
import tempfile
from pathlib import Path

d = Path(tempfile.mkdtemp())
log_path = d / "app.log"

# WatchedFileHandler：检测文件被 mv/create 后自动重开 fd
h = logging.handlers.WatchedFileHandler(log_path)
logger = logging.getLogger("demo")
logger.setLevel(logging.INFO)
logger.addHandler(h)
logger.propagate = False

logger.info("before rotate")

# 模拟 logrotate 的 mv + create：inode 变了
rotated = d / "app.log.1"
os.rename(log_path, rotated)
log_path.touch()

logger.info("after rotate")  # handler 自动发现 inode 变化 -> 写进新文件

print("rotated file:", rotated.read_text().strip())
print("current file:", log_path.read_text().strip())

# copytruncate 的丢窗口示意：复制期间新增写入 = 丢失量
def copytruncate_loss(lines_during_copy: int) -> str:
    return f"copy 期间写入 {lines_during_copy} 行 -> 永久丢失"

print(copytruncate_loss(120))
```

**追问 1**：为什么 copytruncate 在低流量应用里"看起来没问题"？
**提示**：复制-截断窗口通常毫秒级，低 QPS 下窗口内无写入就无丢失——问题是它随流量线性放大，流量涨了才爆。

**追问 2**：SIGUSR1 处理器里 reopen 日志有什么线程安全注意点？
**提示**：信号处理在主线程中断执行，logging 内部有锁，重入可能死锁；稳妥做法是信号处理器只置 flag，由主循环/专用线程执行 reopen。

## 背诵要点
- copytruncate 丢日志窗口=复制到截断之间的写入；正确方案是 mv 原子改名+信号 reopen。
- Python 对接 logrotate 用 WatchedFileHandler（inode 检测自动重开）。
- 容器环境不该有 logrotate：日志走 stdout+采集器。

## 复盘追问
- 如何量化"每天丢了多少行"：比对应用侧写入计数与采集器接收计数？
- 为什么凌晨轮转点丢日志最明显？（轮转与大促/批处理流量重叠？）
