---
title: [Q6013] Webhook 可靠投递：签名、重试与对账
date: 2026-11-19
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6013 · Webhook 可靠投递

> 难度:★★★ | 标签:Webhook, 可靠性, 签名

**问**：向第三方推 Webhook，对方 500 怎么办——「至少一次」投递要配什么：签名（HMAC vs JWT）、重试策略、事件顺序、接收方幂等，以及对账兜底？

**答**：① **签名**：HMAC-SHA256（共享密钥对 body 签名 + 时间戳防重放）优于 JWT——webhook 签名要的是「验证发送方且 body 未篡改」，JWT 引入颁发/过期复杂度且默认无 body 绑定（除非手动加 hash claim）；头部形如 `X-Signature: t=1699,v1=...`，接收方校验 `时间戳±5min` + HMAC 常数时间比较。② **投递语义**：至少一次（at-least-once）——重试必带同一 `event_id`，接收方**必须幂等**（event_id 去重表 + 唯一约束，同 A102 模式）；③ **重试**：指数退避（1m/5m/30m/2h/6h…），N 次失败进死信；连续失败触发**地址熔断**（对方宕机时别把重试队列打满）；④ **顺序**：Webhook 天然可能乱序（重试并发），事件体带 `sequence`/`version`，接收方按业务实体版本号丢弃旧序事件；⑤ **对账兜底**：推送只是加速通道，真相在拉取端——提供分页拉取 API + 每日对账任务比对「已推事件 vs 对方已确认」，漏的补推。

```python
# 全部标准库（hmac/hashlib）；demo 实现签名/验签 + 幂等接收 + 重试调度
import hmac, hashlib, time, json

def sign(secret: str, body: bytes, ts: int) -> str:
    msg = f"{ts}.".encode() + body          # 时间戳拼进签名防重放（Stripe 风格）
    return hmac.new(secret.encode(), msg, hashlib.sha256).hexdigest()

def verify(secret: str, body: bytes, header: str, tolerance: int = 300) -> str:
    """header 形如 't=1699999999,v1=abc...'；返回事件 id 或抛异常。"""
    parts = dict(p.split("=", 1) for p in header.split(","))
    ts = int(parts["t"])
    assert abs(time.time() - ts) <= tolerance, "时间戳超窗，疑似重放"
    expect = sign(secret, body, ts)
    assert hmac.compare_digest(expect, parts["v1"]), "签名不匹配"   # 常数时间比较
    return json.loads(body)["event_id"]

class Inbound:
    """接收方幂等：event_id 唯一去重（demo 用 set，生产用 DB 唯一约束）。"""
    def __init__(self):
        self.seen: set[str] = set()
    def handle(self, event_id: str, payload: dict) -> str:
        if event_id in self.seen:
            return "duplicate-ignored"       # 至少一次投递 → 接收方幂等是契约的一部分
        self.seen.add(event_id)
        return f"processed:{payload.get('type')}"

RETRY_SCHEDULE = [60, 300, 1800, 7200, 21600]     # 指数退避秒数
def schedule_retries(failures: int) -> float:
    return RETRY_SCHEDULE[min(failures, len(RETRY_SCHEDULE) - 1)] if failures else 0

if __name__ == "__main__":
    secret = "whsec_demo"
    body = json.dumps({"event_id": "evt_1", "type": "order.paid"}).encode()
    header = f"t={int(time.time())},v1={sign(secret, body, int(time.time()))}"
    eid = verify(secret, body, header)
    box = Inbound()
    print(box.handle(eid, {"type": "order.paid"}))
    print(box.handle(eid, {"type": "order.paid"}), "← 重投递被幂等挡下")
    print("重试间隔表:", [schedule_retries(n) for n in range(1, 6)])
    # 注意：verify 用 compare_digest 防时序侧信道；body 必须用原始字节（不能先 parse 再重序列化）
```

**追问**：1) 为什么验签必须用**原始 body 字节**？——先 `json.loads` 再重序列化会改变空白/键序，HMAC 对字节敏感，必然验不过；框架里要在 body middleware 之前读 raw。2) 时间戳在签名里的作用？——绑定签名到时间窗，抓包重放超过容忍窗直接拒绝；单纯 HMAC body 无法防重放。3) 事件乱序的另一种解法？——「最终状态」语义：每条 webhook 带**实体最新完整状态**（而非增量 delta），接收方直接覆盖，天然对乱序免疫；代价是消息变大。

## 背诵要点
1. 签名 = HMAC-SHA256(时间戳.body) + 常数时间比较 + ±5min 重放窗；验证用原始 body 字节。
2. 至少一次投递 ⇒ 接收方 event_id 幂等是契约；重试指数退避 + 地址熔断 + 死信。
3. 乱序两解：事件带版本号丢弃旧序，或推「实体最新完整状态」；对账拉取 API 是最终兜底。

## 复盘追问
1. 对方要求「我们收到才算投递成功」，架构怎么变？（提示：推送+拉取双通道，推送失败只影响时效不影响最终一致）
2. webhook 密钥轮换怎么做不中断？（提示：双密钥并行验签过渡期，头部带 key id）
