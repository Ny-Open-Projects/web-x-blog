---
title: "[Q5726] logging 的线程安全边界：记录级锁与多进程各自为政"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5726 · logging 的线程安全边界：记录级锁与多进程各自为政

难度：P6 ｜ 标签：logging、线程安全、handler 锁、RotatingFileHandler、多进程竞争、QueueHandler

**问**：都说 logging 是线程安全的，它到底保证了什么——多线程写同一个日志文件，一条记录会不会被撕成两半？锁加在哪一层？多个进程共用同一个 RotatingFileHandler 写同一文件为什么会出现文件错乱，正确做法是什么？

**答**：
结论：logging 的线程安全是**记录级不撕裂**，不是"无竞争"。①**锁的位置**：每个 Handler 实例自带一把 `createLock()`，在 `emit()` 内 acquire/release——同进程内多线程调用 `log.info()` 时，同一条记录的格式化结果会**完整地**写入流，不会出现"半条 A + 半条 B"；②**锁的粒度**：格式化（`formatter.format`）发生在拿锁**之前**（`handle()` 先 format 再 `emit`），所以大记录的构造成本仍是并发的，锁只保护最后的写动作；③**多进程无此保证**：锁是进程内的，两个进程各持一个 RotatingFileHandler 写同一文件时，谁也看不见对方的偏移和轮转状态——各自判断"该轮转了"就各自 rename，一方的文件句柄指向被改名的旧文件，日志写丢、备份文件互相覆盖；④Python 3.12 起 logging 的锁与 `threading.Lock` 集成更紧（可重入场景由 `Handler.callHandlers` 链上的逐 handler 加锁保证），但**跨进程语义从未改变**。

取舍：a) 线程场景：直接用，放心用；单条 `log.info("%s-%d", tag, i)` 一次 emit 就是一次完整的写；b) 多进程写同一文件：**禁止**裸 RotatingFileHandler——上 `QueueHandler` + `QueueListener`（单进程收口落盘）、`SocketHandler` 发给日志服务、或者干脆落 stdout 交给容器采集器（K8s 时代的默认解）；c) 性能敏感：锁在 emit 层意味着高并发下 handler 锁是瓶颈之一，先考虑异步 handler / 内存队列聚合，而不是自己加"更外面的锁"；d) 不要用 `print` 拼接当日志（Q5729 的行交错）——logging 的锁正是为这个场景准备的；e) 文件轮转本身的问题（rename 时句柄失效、logrotate 的 copytruncate）是另一个维度，别把"轮转竞态"和"行撕裂"混为一谈。

实战：事故形态是"多 worker 进程共享 RotatingFileHandler，文件到 10MB 后日志开始失踪——两个进程同时触发轮转，A 把 access.log rename 成 access.log.1，B 也 rename 了一次（把自己的句柄 rename 走），之后 B 的 write 落在被改名掉的 inode 上，日志从此消失"。修复：QueueHandler 收口到主进程统一落盘。下面演示同进程记录级完整性与多进程问题的机理。

```python
# logging 的线程安全边界: 同进程锁保护, 跨进程各自为政
import io
import logging
import threading

buf = io.StringIO()
handler = logging.StreamHandler(buf)
handler.setFormatter(logging.Formatter("%(message)s"))
log = logging.getLogger("q5726")
log.setLevel(logging.INFO)
log.handlers[:] = [handler]
log.propagate = False

print("[1] 同进程: logging 的 handler 自带锁, 多线程写同一文件句柄是行完整安全的")
def worker(tag: str) -> None:
    for i in range(200):
        log.info("%s-%03d|" + "x" * 60, tag, i)   # 单条记录一次 emit

threads = [threading.Thread(target=worker, args=(t,)) for t in "ABC"]
for t in threads:
    t.start()
for t in threads:
    t.join()

lines = buf.getvalue().splitlines()
assert len(lines) == 600, len(lines)
assert all(line.split("-")[0] in {"A", "B", "C"} for line in lines)
print("    600 条日志, 每条都是完整一行, 无交错截断")

print("[2] 多进程: 进程间没有共享锁, 同一文件上 RotatingFileHandler 各自轮转 -> 文件错乱")
print("    轮转竞态: 两个进程同时判断'该轮转了' -> 各自 rename -> 一方句柄指向被改名文件")
print("    对策: QueueHandler+QueueListener 单点落盘 / SocketHandler / 落 stdout 交采集器")

print("[3] 锁的粒度: 锁在 handler.emit 内部, 格式化在锁外 -- 大记录仍有构造成本竞争")
print("[4] 实战结论: 线程安全是'记录级不撕裂', 不是'性能无竞争'; 高并发先上异步 handler")
```

**追问一**：为什么格式化放在锁外面？这样设计有什么代价？—— 格式化（字符串拼接、`%(asctime)s` 的时间格式化）可能是记录构造中最贵的部分，放锁内会让所有线程串行化在"攒字符串"上，锁持有时长剧增；放锁外让格式化并发进行，只在最终 write 时短暂持锁。代价有二：一是**构造期间的竞争**仍在（CPU 密集的日志记录会拖慢调用线程自己）；二是如果记录对象在 format 后又被共享修改（极少见的不当用法），写入的内容可能与调用时刻不一致。另外注意锁的粒度是**每 handler 一把**：一个 logger 挂两个 handler 时各自持各自的锁，两个 handler 的输出顺序可以互不一致。

**追问二**：QueueHandler/QueueListener 方案里，日志会不会丢？队列满了怎么办？—— 会丢的路径要认清：默认的 `queue.Queue` 是**无限队列**，不丢但内存可能被日志洪峰打爆（生产者快于消费者时堆积）；如果换成有界队列并配 `block=False` 或 `put_nowait`，队列满时 `QueueHandler.emit` 会**静默丢弃**记录（这是有意的——日志系统绝不能反过来阻塞业务线程，logging 文档明确容忍日志丢失）。Listener 侧崩溃时队列里未消费的记录随进程消失。所以金融级审计日志不走这条链：审计要同步落盘（业务线程自己写，接受开销）+ 单独文件 + fsync，而诊断日志走异步可丢。

## 背诵要点
- logging 线程安全 = 记录级不撕裂：锁在每个 handler 的 emit 内；格式化在锁外，构造成本仍并发。
- 多进程共享 RotatingFileHandler 会轮转竞态+写丢：QueueHandler/QueueListener、SocketHandler 或落 stdout 交采集器。
- 高并发瓶颈在 handler 锁与格式化：先异步化/聚合，别在外面套"更锁"。

## 复盘追问
- 日志文件到阈值后日志开始失踪，根因排查路径？（多进程轮转竞态：lsof 看句柄指向的 inode 是否已被 rename 走）
- 队列满时异步日志为什么选择丢而不是阻塞？（日志不能反压业务线程；审计类日志改同步落盘）
