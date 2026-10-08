# 911 channel 传递与语义全景（深卡，结构层见 609）

> 分类：Go 并发 | 难度：L4 | 题型：体系题 | 频率：高 | 关键词：**复制语义**/**同步异步**/**CSP**/**send/recv 算法**/**与 609 边界**

> 原文锚点：第 9~62 段「channel 实现原理全节」

## 思路与架构
channel 这条线分两层：**结构层归 `609-channel.deep.md`（hchan = 环形 buf + 计数 + recvq/sendq + lock，四路径）**；本卡只串**语义/算法/设计层**，按「复制语义 → 同步异步 → send/recv 算法 → CSP 设计」四层：
- 复制语义层：值必复制、经 buf 两次、只复制直接值部（对应 `911-channel-data-copy.md`）。
- 同步异步层：无缓冲=rendezvous、有缓冲=解耦、阻塞在满/空（对应 `911-channel-sync-async.md`）。
- 算法层：收发都「抢锁→判对向等待队列→handoff/buf/park」，recvq/sendq 优先于 buf（见 sync-async 卡）。
- 设计层：CSP 名言、传所有权、适用边界（对应 `911-channel-csp-design.md`）。

## 方案取舍
- **结构问题交给 609**：被问「hchan 长啥样 / 四路径 / nil channel / 关闭唤醒」直接引 `609-channel.deep.md`，本卡不重画结构。
- **复制问题给 data-copy 卡**：强调「两次复制」与「大结构体传指针」是 609 没覆盖的痛点。
- **同步异步给 sync-async 卡**：把 609 的四路径展开成「算法步骤 + 优先级」，更贴近手写推理。
- **设计观给 csp 卡**：CSP 名言 + 适用边界，避免「channel 万能」误区。

## 答题技巧
1. 开场点题：channel 是 CSP 模型落地，「通过通信共享内存」。
2. 结构一嘴带过（引 609），重点展开语义：复制几次、同步还是异步。
3. 手写 send/recv 算法时按「锁 → 对向队列 → buf → park」顺序，别漏 recv 遇 sendq 非空的分支。
4. 收尾落到取舍：channel 适合传所有权/流水线，高频状态用 atomic/mutex。
5. 反直觉提醒：无缓冲是 handoff 不是「缓冲为 1」；经 buf 的值被复制两次。
