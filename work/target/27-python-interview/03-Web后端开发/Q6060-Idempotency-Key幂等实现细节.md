---
title: [Q6060] Idempotency-Key 幂等键的实现细节
date: 2026-11-20
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6060 · Idempotency-Key 幂等键的实现细节

> 难度:★★★★ | 标签:幂等, Idempotency-Key, 分布式, 工程实践

**问**：支付接口要求幂等，第一版用"数据库唯一索引挡重复"挡住了请求却没返回原结果，客户端收到 409 后自己重试又造成二次下单。完整的 Idempotency-Key 机制该怎么实现？并发同 key 怎么处理？存储和过期怎么管？

**答**：幂等的完整语义是**同 key 返回同结果**，不只是"拒绝重复"。标准流程五步：a) 客户端带 `Idempotency-Key`（UUID）且**请求体指纹**参与校验——同 key 不同 body 必须拒绝（422），防止"键复用"造成错单；b) 查存储：命中且已成功 → **重放缓存的原响应**（含原状态码），这是第一版缺的那步；c) 未命中 → 抢占：插入"进行中"记录（唯一索引/SETNX），抢不到说明**并发同 key**在执行 → 返回 409/425 让客户端稍后重试（或挂起等待），绝不并发执行两份；d) 执行业务 + **响应体持久化**到幂等记录；e) 记录带 TTL（行业惯例 24h，Stripe 语义），过期可清理，执行中的记录要有超时兜底（进程崩溃后"进行中"卡死，需要定时释放）。存储选型：Redis（SETNX+TTL，快但持久性弱，响应体大时内存贵）vs 数据库（唯一索引+行锁，强一致但慢）——金融类选 DB，一般业务 Redis+DB 双写。响应重放要注意：**错误响应是否重放**按业务定（4xx 一般不重放，让客户端改了再试；5xx 已扣款的可重放），要在协议里写清楚。

```python
# file: code/03_Web后端开发/q6060_idempotency.py
import threading, time

store = {}        # key -> 响应缓存 (生产: DB 表 or Redis, 带 TTL)
inflight = {}     # key -> 执行中标记 (生产: 唯一索引/SETNX)
lock = threading.Lock()
results = []

def handle(key, fingerprint, work):
    with lock:
        if key in store:
            if store[key]["fp"] != fingerprint:
                results.append(("422-键同体不同", None)); return
            results.append(("replay", store[key]["resp"])); return   # 重放原响应
        if key in inflight:
            results.append(("409-并发同key", None)); return            # 不并发执行
        inflight[key] = True
    try:
        resp = work()
        with lock:
            store[key] = {"fp": fingerprint, "resp": resp}             # 响应体持久化
            results.append(("executed", resp))
    finally:
        with lock:
            inflight.pop(key, None)

def charge():
    time.sleep(0.02)
    return {"id": "pay-1", "amount": 100}

# 1) 并发同 key: 只执行一次, 其余 409
ts = [threading.Thread(target=handle, args=("K1", "fp-A", charge)) for _ in range(4)]
for t in ts: t.start()
for t in ts: t.join()
print("并发同 key 结果:", results)

# 2) 后续重试: 重放缓存响应, 不再执行
results.clear()
handle("K1", "fp-A", charge)
print("重试重放:", results)

# 3) 同 key 不同 body: 拒绝
results.clear()
handle("K1", "fp-B", charge)
print("键同体不同:", results)
print("生产: store 带 TTL(24h), inflight 加超时释放(防崩溃卡死), 错误响应是否重放进协议文档")
```

**追问**：1) 没带 Idempotency-Key 的请求怎么办？——按不可幂等处理（每次真执行），或在网关/服务端按"请求指纹哈希"自动生成短 TTL 幂等（收益有限且有误伤，通常明确要求客户端必带并在文档写死；缺失直接 400）。2) 幂等键的作用域怎么定？——全局 vs 每 API key 每 endpoint：全局键复用风险高，推荐 scope=(client_id, endpoint, key)，同 key 打到不同接口不冲突，存储主键三元组。3) "执行成功但响应未持久化就崩溃"怎么办？——窗口不可避免，靠**结果查询接口**（GET /payments/{idempotency_key} 或业务单号）兜底：客户端拿 5xx 后先查再重试，协议层面给"不确定态"留出口。

## 背诵要点
- 幂等 = 同 key 返回同结果：校验（key+body 指纹，不一致 422）→ 命中重放缓存响应 → 未命中抢占执行 → 响应体持久化。
- 并发同 key：唯一索引/SETNX 抢占，抢不到返回 409/425 绝不并发执行；执行中记录要超时释放防崩溃卡死。
- 存储：DB 唯一索引（金融）或 Redis SETNX+TTL（24h 惯例）；未带 key 明确 400；崩溃窗口用结果查询接口兜底。

## 复盘追问
- 你们支付/下单接口的幂等现在挡在哪一层？返回给客户端的是"原结果"还是"错误码"？（提示：复盘 409 重试造成二次下单的链路，对照五步流程找缺口）
- 幂等记录的 TTL、清理与"进行中超时释放"谁在管？（提示：后台任务 + 监控 inflight 卡死时长；演练 kill -9 后的重试路径）
