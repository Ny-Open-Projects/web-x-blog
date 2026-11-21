---
title: [Q141] 幂等接口设计:Idempotency-Key
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q141 · 幂等接口设计:Idempotency-Key

> 难度:★★★ | 标签:幂等性, 分布式

**问**:支付下单这类非幂等 POST 如何保证网络重试不重复扣款?

**答**:标准做法是 Idempotency-Key:客户端为每笔业务操作生成唯一键(如 UUID)随请求发送;服务端以键为锁/缓存——首次请求执行业务并存储"键 → 响应结果",重试命中则直接返回已存结果,不重复执行;处理中的重复请求可返回 409 或挂起等待。实现要点:键需带过期时间与租户隔离,结果存储与业务写入要在同一事务或用 Redis SETNX + 消息表保证原子性。

```python
# file: code/03_Web后端开发/q141_idempotency_key.py
try:
    from fastapi import FastAPI, Header, HTTPException
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()
results: dict[str, dict] = {}          # 生产用 Redis + TTL

@app.post('/payments')
def create_payment(amount: int,
                   idempotency_key: str = Header(...)):
    if idempotency_key in results:      # 重试:返回首次结果
        return results[idempotency_key]
    if amount <= 0:
        raise HTTPException(400, 'amount must be positive')
    # 实际: 在同一事务中写入订单 + 存储幂等记录
    resp = {'order_id': f'pay-{len(results) + 1:04d}', 'amount': amount}
    results[idempotency_key] = resp
    return resp
# 客户端: 相同 Idempotency-Key 重发 N 次,服务端只扣款一次
```

**追问**:
- 与数据库唯一索引去重的区别?——唯一索引是最终防线,幂等键在入口层提前返回一致响应,两者通常叠加使用。
- 幂等键的结果存多久、按什么隔离?——带 TTL(覆盖最大重试窗口)且键空间含租户/用户维度;全局唯一键会被碰撞误命中。
- 处理中的重复请求怎么办?——SETNX 标记 processing,后来的返回 409 或轮询等待;完成态写回后重试者拿到原响应。
- Redis 记录和 DB 写入不一致怎么办?——同一事务做不到就「先 DB 后 Redis + 消息表补偿」;以 DB 唯一约束为最终防线。
