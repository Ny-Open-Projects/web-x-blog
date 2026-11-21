---
title: [Q555] print 的缓冲与 flush:输出顺序疑难
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q555 · print 的缓冲与 flush:输出顺序疑难

> 难度:★★☆☆ | 标签:IO, 缓冲

**问**:为什么重定向到文件后日志顺序乱了、进度条不见了?stdout 与 stderr 的缓冲策略差异?

**答**:stdout 接终端时是行缓冲(换行即刷),重定向到文件/管道时变成块缓冲(攒满才刷)——进度条(不换行)与「输出顺序」疑难都源于此:print 不加 flush 时内容滞在缓冲,程序崩溃或与 stderr 交错时顺序错乱。stderr 默认无缓冲(立即写),所以错误总是先出现。解决:关键输出 print(..., flush=True);重定向运行用 python -u(全不缓冲);程序内设置 sys.stdout.reconfigure(line_buffering=True)。交互式进度条的正确工具是带 \r 的 flush 输出或专门库。

```python
# file: code/01_语言核心与底层/q555_print_flush.py
import sys
import time

if __name__ == "__main__":
    print("stdout is a tty:", sys.stdout.isatty())
    print("redirecting changes buffering to block mode")

    print("progress 0", end="", flush=True)
    time.sleep(0.05)
    print(" -> 50", end="", flush=True)
    time.sleep(0.05)
    print(" -> 100", flush=True)          # 每步强制刷出

    print("stdout first")
    sys.stderr.write("stderr written\n")  # stderr 默认无缓冲
    print("done")
```

**追问**:1) 用 python a.py 2>&1 | tee log 时为什么 stdout 全在最后?——stdout 进管道变块缓冲,程序结束才一次刷出,而 stderr 实时——顺序颠倒;加 -u 或 flush 可修复。2) 缓冲的三种状态?——stdout 连 TTY 是行缓冲,连管道/文件是块缓冲(约 8KB);stderr 基本无缓冲(直写);这就是「日志顺序错乱」的全部根源。3) 缓冲的层次?——Python io 层缓冲、C stdio 缓冲、OS 页缓存三层;python -u 让 io 层无缓冲;print(flush=True) 单次强制刷出。4) 生产陷阱?——容器里日志延迟采集(设 PYTHONUNBUFFERED=1);崩溃前最后几条 print 丢失(块缓冲没刷);print 与 logging 混用顺序错乱——logging 默认走 stderr,统一出口。
