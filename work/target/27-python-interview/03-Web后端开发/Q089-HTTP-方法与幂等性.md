---
title: [Q089] HTTP 方法与幂等性
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q089 · HTTP 方法与幂等性

> 难度:★☆☆ | 标签:HTTP, 幂等性

**问**:说说常用 HTTP 方法的语义,哪些是幂等的、哪些是安全的?

**答**:GET 读取资源(安全且幂等)、PUT 全量替换(幂等)、DELETE 删除(幂等)、POST 创建/触发动作(不幂等)、PATCH 部分更新(不保证幂等)、HEAD/OPTIONS 安全。幂等指同一请求执行一次和多次,对资源状态的影响一致——这是接口设计和重试机制的基础:网络重试时只有幂等接口可以安全重发。

```python
# file: code/03_Web后端开发/q089_idempotent_check.py
store = {}  # key -> value,模拟资源

def handle(method: str, key: str, value=None):
    if method == 'GET':
        return store.get(key)
    if method == 'PUT':          # 幂等:覆盖式写入
        store[key] = value
        return value
    if method == 'POST':         # 非幂等:每次追加,结果不同
        store.setdefault(key, []).append(value)
        return store[key]
    if method == 'DELETE':       # 幂等:删除多次结果一致
        return store.pop(key, None)

for _ in range(3):
    handle('PUT', 'a', 1)
    handle('POST', 'log', 'x')
print(store)  # {'a': 1, 'log': ['x', 'x', 'x']}
```

**追问**:
- POST 如何做到幂等?——客户端携带唯一 Idempotency-Key,服务端去重(详见 Q141)。
- PATCH 默认不幂等怎么补救?——约定提交绝对值而非增量,或携带版本号/条件更新(IF-Match ETag)使重复提交可检测。
- GET 为什么「安全」还要防滥用?——安全指不改变服务端状态,不代表免费:重查询 GET 一样打垮数据库,限流照上。
- DELETE 返回 204 还是 200?——无响应体用 204;要返回被删资源快照用 200;团队统一即可。
