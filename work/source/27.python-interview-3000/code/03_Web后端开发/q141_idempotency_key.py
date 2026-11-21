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
