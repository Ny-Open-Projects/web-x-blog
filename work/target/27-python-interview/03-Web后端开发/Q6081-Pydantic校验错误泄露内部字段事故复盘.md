---
title: "[Q6081] Pydantic 校验错误泄露内部字段的事故复盘"
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6081 · Pydantic 校验错误泄露内部字段的事故复盘

难度：★★★☆☆ ｜ 标签：事故复盘 / Pydantic v2 / 信息泄露 / 错误响应设计

**问**：安全扫描发现 422 响应把 `input` 回显给客户端，里面带着用户提交的整段 SQL 和内部字段名。FastAPI 默认的校验错误响应为什么会泄数据？正确的外层错误契约怎么设计？

**答**：
- **结论**：FastAPI（基线 0.100+/Pydantic v2）校验失败走 `RequestValidationError` 处理器，默认把 Pydantic 的 `errors()` 原样序列化返回——Pydantic v2 的每条错误含 `type`（内部错误码）、`loc`（字段路径）、`msg`、**`input`（原始输入回显）**、`url`（文档链接）。`input` 回显就是反射面：攻击者提交的 payload（XSS 向量、SQL 片段、探测性超长串）会被服务端原样返回并可能被日志/前端二次渲染。修复是**覆盖异常处理器**：422 响应只输出"字段路径 + 归一化文案"，丢掉 input/url，日志侧保留完整链（内部可查）。
- **取舍**：错误信息的两难：太细（帮助开发/攻击者）vs 太粗（用户没法改请求）。业界分层：面向客户端返回"机器可读的字段错误 + 稳定错误码"（保证契约稳定，不随 Pydantic 版本漂移——`type` 值如 `string_too_long` 是 Pydantic 内部枚举，升级可能变）；面向日志/追踪保留全量。另一个坑：`model_dump` 输出响应时 `exclude_unset` 语义错用会把未填字段的 None 泄成字段存在性信号（探测用）。
- **实战**：复盘清单：1）全局覆盖 `RequestValidationError` 与 `ResponseValidationError` 两个处理器；2）错误响应进契约测试（schemathesis 思路）：断言响应体不含请求原文子串；3）`loc` 里的别名/内部字段名要映射成对外 schema 名；4）校验错误日志加 trace_id 串起内部细节。

```python
"""FastAPI 校验错误的外层契约改造（FastAPI 0.100+ / Pydantic v2 基线）"""
try:
    from fastapi import FastAPI, Request
    from fastapi.exceptions import RequestValidationError
    from fastapi.responses import JSONResponse
    from pydantic import BaseModel, Field
except ImportError:
    raise SystemExit("缺 fastapi/pydantic：pip install 'fastapi>=0.100' 'pydantic>=2'（降级方案见文末）")

app = FastAPI()

class OrderIn(BaseModel):
    user_id: int = Field(ge=1)
    memo: str = Field(max_length=32)
    internal_tag: str = Field(default="ops-only", max_length=8)

# 默认行为演示：input 回显攻击 payload
@app.post("/bad")
async def bad(item: OrderIn):
    return {"ok": True}

# 修复：覆盖处理器，剥离 input / url / 内部错误码
@app.exception_handler(RequestValidationError)
async def safe_validation_handler(request: Request, exc: RequestValidationError):
    fields = []
    for err in exc.errors():
        fields.append({
            "field": ".".join(str(p) for p in err["loc"]),   # 只留路径
            "message": err["msg"],                            # 归一化文案
        })
    # 完整错误进日志（含 input），响应不含
    print("validation detail:", exc.errors())
    return JSONResponse(status_code=422, content={"error_code": "INVALID_REQUEST", "fields": fields})

from fastapi.testclient import TestClient  # httpx 基线 0.27+
client = TestClient(app)

# 攻击 payload：input 回显 = 反射面
r = client.post("/bad", json={"user_id": -1, "memo": "x" * 100,
                              "internal_tag": "<script>alert(1)</script>"})
print("默认处理器未生效（自定义已接管）状态码:", r.status_code)
print("安全响应体:", r.json())

# 验证不回显输入原文
assert b"<script>" not in r.content, "input 回显未剥离！"
print("反射面检查通过：响应不含请求原文")

# 降级方案（无 fastapi 时）：纯 Pydantic 手动同构
from pydantic import ValidationError
try:
    OrderIn(user_id=-1, memo="y" * 100, internal_tag="<script>x</script>")
except ValidationError as e:
    print("Pydantic 原始 errors 含 input:", "input" in e.errors()[0])
    print("对外只导出 field+msg:", [{"field": ".".join(map(str, x["loc"])), "message": x["msg"]} for x in e.errors()])
```

**追问链**
1. `ResponseValidationError`（响应模型不匹配）为什么比请求侧更危险？
   1. 请求侧错误是"客户端发来的"，回显的也是它自己的数据；响应侧错误是**服务端数据**漏进错误响应（可能带内部枚举、其他用户字段），且发生在生产数据路径上——必须全局处理器兜底为 500 + 内部日志，绝不把 raw error 返回。
   2. 追问：为什么不能把 Pydantic 的 `type` 码直接当对外错误码？——它是库内部枚举（3.x 之间会增删），错误码变更即客户端破坏性变更；对外错误码必须是自有契约，映射层写测试钉死。
2. 校验错误与告警聚合怎么协同，避免"422 风暴"刷屏？
   1. 422 是客户端错误不应触发服务端告警；按 error_code 分桶计数、只对"突增的正常请求被误判"告警；日志采样保留 1%-100% 视流量，但攻击特征 payload（超长/超深）单独通道。

## 背诵要点
- FastAPI 默认 422 回显 Pydantic errors 的 input/url/type——input 是反射面，type 是库内部枚举不可对外。
- 修复：覆盖 RequestValidationError/ResponseValidationError 处理器，响应只含 field+msg+自有 error_code，全量细节进日志。
- 对外错误码必须是自有契约（不随 Pydantic 升级漂移）；响应侧校验错误一律 500 兜底。

## 复盘追问
- 契约测试如何自动断言"响应不含请求原文"？超长 payload 的比对怎么做不拖慢 CI？
- 内部字段名（如 internal_tag）出现在 loc 里算不算泄露？别名映射放在哪一层最稳？
