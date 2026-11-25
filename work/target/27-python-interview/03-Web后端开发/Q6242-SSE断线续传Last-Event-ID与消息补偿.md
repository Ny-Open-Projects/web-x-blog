---
title: "[Q6242] SSE 断线续传：Last-Event-ID、消息补偿与重放窗口"
date: 2026-11-24
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6242 · SSE 断线续传：Last-Event-ID、消息补偿与重放窗口

难度：P6 ｜ 标签：SSE、Last-Event-ID、断线续传、消息补偿、重放窗口、EventSource、at-least-once、环形缓冲

**问**：SSE 断线重连时客户端怎么不丢消息——`id:` 字段与 `Last-Event-ID` 请求头的协商机制是什么？服务端的"重放窗口"怎么设计（全量重放 vs 环形缓冲截断）？消息 ID 怎么生成才安全（单调、可校验、不泄露内部序号）？at-least-once 的重复消息在客户端怎么去重？

**答**：
结论：SSE 的续传协议内建于规范：服务端每条消息带 `id: <序号>` 字段，客户端 EventSource **自动**记录最后收到的 id，断线重连时在 `Last-Event-ID` 请求头里带回——服务端从该 id 之后重放缺失消息。这套机制要真正"不丢"，服务端必须回答三个设计问题：①**重放来源**——内存环形缓冲（进程内，worker 重启即丢）必须升级为共享存储（Redis List/Stream、DB），因为多 worker 部署（Q6005 会话粘性靠不住）与重启场景下"断线前的消息在另一个进程内存里"；②**重放窗口**——环形缓冲只保留最近 N 条（如 1000 条/5 分钟），客户端 id 落在窗口外时明确拒绝（`retry` 提示 + 客户端走全量快照接口重新拉基线再订阅增量），**不要假装能补**——假装能补等于静默丢消息；③**ID 设计**——单调递增是硬约束（续传按序比较），但**不能直接暴露全局自增**（业务量泄露，Q6240 同理）：用"流分区序号 + 随机盐 hash"或"每连接独立的透明游标"，服务端能解出内部序号即可。消息语义是 **at-least-once**：重连瞬间可能重复（断线时已收到但客户端没来得及持久化 id 的消息会重放一次），客户端按 id 去重（`seen = max(seen, id)` 与幂等业务处理双保险）。配套：`retry:` 字段建议重连间隔、`event:` 字段分类型、心跳注释行（`: ping`）防 LB 空闲超时杀连接（Q6177/Q6071 的反代缓冲堆积与超时错配是 SSE 的两大运维坑）。

取舍：a) 重放窗口大小：窗口越大补偿越强、内存/存储成本越高——按"客户端最长可容忍的断线时长"定（移动端 10 分钟、桌面 1 分钟），窗口外兜底走快照+增量协议（与游标分页 Q1352 的契约同构）；b) 全量重放 vs 增量：小流量通知类直接重放最近 N 条；数据同步类用"快照版本号 + SSE 增量"两段式（客户端断线久 → GET /snapshot?version= → SSE 订阅 version 之后的增量）；c) ID 与多流：一个连接订阅多个主题时，Last-Event-ID 只有一个——按"主题+序号"编码进单个 id 字符串（`topic1:42;topic2:17`）或每主题独立连接（连接数成本），主流做法是复合 id；d) 服务端实现：`StreamingResponse`/nginx 的 `X-Accel-Buffering: no` 关缓冲（Q6071 事故必配）、心跳注释行 15-30s 一次、连接级背压（慢客户端丢弃+踢除，Q1606 思路）；e) 与 WebSocket 的分工：需要服务端单向下发+自动重连语义选 SSE（HTTP 原生、代理友好），双向选 WS（Q393 的选型矩阵，Q735 落地）。

实战：事故形态是"行情推送服务重启后，EventSource 自动重连但 Last-Event-ID 指向的序号在**新进程内存里不存在**——服务端从 0 开始重发，客户端把旧消息当新消息处理，重复下单 3 笔。修复为：消息台账迁 Redis Stream（`XADD` 自然带单调 id，`XREAD` 支持 from-id 语义正好匹配 Last-Event-ID）、id 编码为分区+流内序号、窗口外返回 `event: resync` 让客户端走快照、客户端按 id 幂等去重；重复下单归零"。下面实现重放窗口与 Last-Event-ID 协商的核心逻辑。

```python
# SSE 断线续传: Last-Event-ID 协商、环形重放窗口与幂等去重
import json

class SSEHub:
    """共享台账(Redis Stream 的教学替身) + 重放窗口 + Last-Event-ID 协商"""

    def __init__(self, window: int = 5) -> None:
        self.log: list = []                 # (stream_id, payload); 生产用 Redis Stream
        self.window = window                # 只保留最近 window 条

    def publish(self, payload: str) -> int:
        sid = len(self.log) + 1
        self.log.append((sid, payload))
        if len(self.log) > self.window + 2:  # 环形窗口: 台账只保留最近 window 条
            self.log = self.log[-self.window:]
        return sid

    def replay(self, last_event_id: int | None):
        """按客户端上报的 Last-Event-ID 重放; 窗口外返回 resync 指令"""
        if last_event_id is None:
            return [self._frame(sid, p) for sid, p in self.log], "full"
        available_min = self.log[0][0] if self.log else None
        if available_min is not None and last_event_id + 1 < available_min:
            return [self._resync(available_min)], "resync"   # 断线太久: 明确要求快照重建
        missed = [(sid, p) for sid, p in self.log if sid > last_event_id]
        return [self._frame(sid, p) for sid, p in missed], "delta"

    @staticmethod
    def _frame(sid: int, payload: str) -> str:
        return f"id: {sid}\nevent: message\ndata: {json.dumps(payload, ensure_ascii=False)}\n\n"

    @staticmethod
    def _resync(from_id: int) -> str:
        return f"event: resync\ndata: {json.dumps({'from': from_id})}\n\n"

hub = SSEHub(window=5)
for i in range(1, 9):                       # 8 条消息, 窗口只留 4-8
    hub.publish(f"tick-{i}")

print("[1] 正常续传: 客户端收到过 id=6, 断线后带 Last-Event-ID: 6 重连")
frames, mode = hub.replay(last_event_id=6)
print(f"    模式={mode}, 重放 {len(frames)} 条:")
for f in frames:
    print("   ", f.replace("\n", " | "))

print("[2] 幂等去重: at-least-once 下重连瞬间可能重放已处理消息")
client_seen = 6                             # 客户端已处理到的 id
for f in frames:
    sid = int(f.split("id: ")[1].split("\n")[0])
    if sid > client_seen:
        print(f"    处理 id={sid} (新消息)")
    else:
        print(f"    跳过 id={sid} (重复: 断线窗口内的 at-least-once 重放)")

print("[3] 窗口外: 明确 resync, 不假装能补")
frames2, mode2 = hub.replay(last_event_id=2)
print(f"    Last-Event-ID=2 (早于窗口起点 4) -> 模式={mode2}")
print("   ", frames2[0].replace("\n", " | "))
print("[rule ] 续传=共享台账+单调 id+窗口外 resync; 重放是 at-least-once, 客户端按 id 幂等")
```

**追问一**：为什么"进程内存台账 + EventSource 自动重连"在多 worker 部署下必然出事？完整的共享台账方案（Redis Stream）怎么对齐 SSE 协议？—— 必然出事的三个场景：①**粘性失效**——EventSource 重连可能被 LB 分到另一个 worker（Q6005），新 worker 内存里没有旧 id 之前的消息，要么从 0 重发（重复）要么从"我这里最新"发（静默丢）；②**重启**——进程重启内存台账清零，Last-Event-ID 无处对账；③**回放竞争**——同 id 消息在两个 worker 各有一份副本。Redis Stream 对齐方案：`XADD topic * payload k v` 生成 `ms-seq` 形态的**天然单调 id**（时间戳毫秒+同毫秒序号，跨重启单调不重复）；重放 = `XREVRANGE`/`XRANGE (id +` 按 Last-Event-ID 之后读取；窗口 = `XTRIM MAXLEN ~ N`（近似修剪不阻塞）；窗口外 resync 判定 = 客户端 id 早于流内最小 id。三个对齐细节：①SSE 的 `id:` 直接用 stream id 的字符串形态（可解序比较）；②多主题场景每主题一个 Stream，SSE id 编码 `topic:stream-id` 复合值；③发布与推送解耦——worker 只负责 `XREAD BLOCK` 消费后转发 SSE，发布方（业务进程）与推送方（连接进程）分离，重启只影响连接不影响消息留存。这套就是"行情/通知类 SSE 的标准底座"。

**追问二**：SSE id 里直接暴露全局自增序号有什么问题？"每连接透明游标"方案怎么实现，与幂等去重的配合关系是什么？—— 直接暴露全局序号的问题（Q6240 家族）：①**规模泄露**——外部观察者对比两个连接的 id 差值推算平台消息速率；②**跨用户对齐攻击**——A 用户断线前的 id 与 B 用户当前 id 比对，推断"我们之间收到了多少同批消息"，配合时间戳可做订阅规模画像；③**与内部系统耦合**——id 直接映射 DB 自增，暴露分库分表路由规律。"每连接透明游标"：服务端为每个 SSE 连接生成随机游标键（`cursor_id = token_urlsafe`），内部维护 `cursor -> 全局序号` 映射（带 TTL），SSE 帧里给客户端的 id 是**这个连接自己的游标值**（不可跨连接比较、不可推导全局速率）；重连时按游标解回全局序号重放——代价是**重连必须回到同一服务端实例或有共享映射存储**（Redis TTL 映射即可），且游标过期后走 resync。与幂等去重的配合：透明游标仍是单调的（按该连接的序），客户端按"游标值 > 已见最大值"去重依然成立；**业务级幂等**（消息携带业务事件 id，客户端按事件 id 幂等处理）是双保险——传输层游标管"不重复处理同一条 SSE 帧"，业务层幂等管"重放窗口外的边界情况"，两层各管一段，单独任何一层都可能漏。

## 背诵要点
- SSE 续传协议：帧带 `id:`，EventSource 断线自动重连并携带 Last-Event-ID 头，服务端重放该 id 之后的消息；`retry:` 建议重连间隔，心跳注释行防 LB 超时。
- 不丢消息三件套：共享台账（Redis Stream 的 XADD 单调 id / XRANGE from-id 天然匹配续传）、重放窗口（窗口外明确 resync 走快照，不假装能补）、id 不暴露全局自增（复合编码或每连接透明游标）。
- 重放是 at-least-once：客户端按 id 去重 + 业务事件 id 幂等双保险；多 worker 下内存台账必出事（粘性失效/重启/副本竞争）。

## 复盘追问
- 重启后客户端 Last-Event-ID 指向的序号不存在会怎样、怎么根治？（内存台账失效→重复或丢失；迁 Redis Stream，XADD 天然单调 id，窗口外 resync 快照重建）
- 为什么 SSE id 不能用全局自增、透明游标怎么工作？（规模泄露与跨用户对齐画像；每连接随机游标映射内部序号，重连需共享映射存储，游标过期走 resync）
