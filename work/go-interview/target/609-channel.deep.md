# 609 channel 底层深挖

## 思路与架构
hchan 全景＝**环形缓冲(buf)** ＋ **计数/容量(qcount/dataqsiz)** ＋ **环形下标(sendx/recvx)** ＋ **两等待队列(recvq/sendq，waitq of sudog，FIFO)** ＋ **锁(lock, mutex)**。一次收发有四条路径：
- ① 无缓冲 handoff：发送方直接把值拷给 recvq 队首 sudog（不经过 buf）；
- ② 有缓冲且未满：写 `buf[sendx]`、sendx 环形+1；
- ③ 缓冲满(发送)/空(接收)：封装 sudog 挂入 sendq/recvq，`gopark` 阻塞；
- ④ 关闭 channel：`close` 置 `closed` 并唤醒全部等待者（接收者 success=false、读到零值）。

## 方案取舍
- **channel vs mutex/atomic**：channel 适合"传递数据所有权、协调协程生命周期、流水线扇入扇出"；但每次收发都有**加锁 + 可能 gopark/goready 调度**的代价。高频计数器、标志位、状态机用 `atomic`/`sync.Mutex` 更轻——别把 channel 当万能锁。
- **自旋 vs 挂起**：抢 hchan.lock 时，短临界区自旋省上下文切换，长等待自旋纯耗 CPU，runtime 会 fallback 到挂起。

## 答题技巧
1. **先画 hchan 四部分**：环形缓冲 / 计数容量 / 等待队列 / 锁。
2. **纠正"双向链表"误传**：数据是环形缓冲(sendx/recvx 模运算)，sudog 链表只管理阻塞等待者。
3. **FIFO 等待队列**保证公平：早阻塞的接收者先拿到数据。
4. **反直觉点**：① 无缓冲是 handoff 而非"缓冲为 1"；② 向 **nil channel 收发永久阻塞**（hchan 为 nil）；③ 关闭 channel 唤醒等待者且 `success=false`；④ 自旋锁≠mutex，只适合短临界区。
5. **版本锚点**：hchan 结构长期稳定（`runtime/chan.go`）；Go 1.9 重构了 mutex 内部实现但不影响 channel 语义；`select` 多 case 时走 `selectnbrecv`/`selectsend` 等专用路径，但底层仍是同一套 sudog 机制。
