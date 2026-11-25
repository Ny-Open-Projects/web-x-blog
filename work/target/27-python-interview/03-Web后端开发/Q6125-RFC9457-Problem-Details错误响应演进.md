---
title: [Q6125] RFC 9457 Problem Details：错误响应的演进
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6125 · RFC 9457 Problem Details：错误响应从各自为政到标准化

> 难度:★★★☆☆ | 标签:版本演进, 错误设计, API 规范

**问**:"每个服务一套错误 JSON 结构"的痛点是什么？RFC 7807→9457 定义了哪些标准字段、解决了什么？`type` URI 该怎么设计、扩展字段放哪？Python 服务怎么落一套统一 problem+json？

**答**:结论：RFC 7807（2016）→ **RFC 9457（2023 取代）** 定义了机器可读的错误响应：`application/problem+json` + 必选 `type/title/status`，可选 `detail/instance`，扩展字段平铺在顶层或用 `$schema` 化的自定义成员——目标是让客户端**写一次解析器**、让网关/监控按统一字段聚合错误率。落地要点：a) `type` 用"文档锚点"URI（如 `https://api.example.com/errors/insufficient-fund`），type:about:blank 表示"status 就是语义"；b) **不要把堆栈/内部字段塞进 problem**——它是面向客户端的契约，内部诊断信息走 traceId 引用（`instance` 指向可查的位置）；c) 与 HTTP 语义对齐：validation 错误用 422 + 扩展 `errors[]` 数组，重试类用 `Retry-After` 头而非扩展字段；d) Python 侧做一个 Starlette/FastAPI 异常处理器统一出口，业务代码只抛带 code 的领域异常。

```python
# 基线: 纯标准库实现 problem+json 生成器（框架接入见降级说明）

class Problem(Exception):
    """领域异常: 业务层只管抛, 出口统一转 problem+json (RFC 9457)。"""
    def __init__(self, status, code, title, detail=None, **ext):
        super().__init__(detail or title)
        self.status, self.code, self.title = status, code, title
        self.detail, self.ext = detail, ext

BASE = "https://api.example.com/errors/"

def to_problem(p: Problem, instance: str) -> dict:
    body = {
        "type": BASE + p.code,          # 机器可读的'错误类型'锚点
        "title": p.title,               # 短句, 与 status 语义一致
        "status": p.status,
        "detail": p.detail,             # 面向人的解释, 不含内部信息
        "instance": instance,           # 本请求的追踪锚点
    }
    body.update(p.ext)                  # 扩展成员平铺顶层(9457 允许)
    return body

# ---- 1) 领域异常 -> problem+json ----
try:
    raise Problem(422, "insufficient-fund", "余额不足",
                  detail="账户 A 余额 3.20, 需 10.00", balance=3.20)
except Problem as p:
    import json
    body = to_problem(p, instance="/trace/req-8812")
    print(json.dumps(body, ensure_ascii=False, indent=2))
    print("Content-Type:", "application/problem+json")

# ---- 2) 统一出口(Starlette 风格伪接入, 缺库降级为说明) ----
HANDLER = """
# FastAPI/Starlette 统一注册:
from starlette.responses import JSONResponse
async def problem_handler(request, exc: Problem):
    return JSONResponse(to_problem(exc, f"/trace/{request.state.trace_id}"),
                        status_code=exc.status,
                        media_type="application/problem+json")
app.add_exception_handler(Problem, problem_handler)
"""
print("框架接入模板:", HANDLER)

# ---- 3) 反面清单: 哪些不该进 problem ----
bad = {"stack": "Traceback ...", "sql": "select * from user", "secret": "sk-..."}
print("禁止项: 堆栈/SQL/密钥 -> 属内部诊断, 走日志与 instance 引用, 不进客户端契约")

# ---- 4) 网关侧聚合收益: 统一 type 计数 ----
from collections import Counter
seen = [Problem(422, "insufficient-fund", "t"), Problem(409, "conflict", "t"),
        Problem(422, "insufficient-fund", "t")]
print("按 type 聚合错误率:", Counter(p.code for p in seen))
```

**追问一层**:`type: about:blank` 什么时候用？（status 码本身已完整表达语义（如 404），无需自定义类型；客户端可按"空白类型=看 status"降级解析，保证旧客户端兼容）。
**追问二层**:9457 相对 7807 增加了什么？（`Content-Type` 允许 `application/json` 携带 problem 结构、明确了扩展成员的注册与安全考量、澄清多语言/字符处理——升级 mostly 平滑，但要处理 7807 严格派的 media type 校验）。
**追问三层**:错误文档站怎么和 `type` URI 联动？（`type` 指向可版本化文档页并要求 200 响应；CI 校验"代码里每个 code 都有对应文档"，防止 type 变成死链）。

## 背诵要点
- RFC 7807→9457：problem+json 统一字段 type/title/status(/detail/instance)，客户端一次解析、网关按 type 聚合。
- type 是文档锚点 URI（about:blank 表示纯 status 语义）；扩展平铺顶层；内部诊断只走 instance 引用。
- 落地：领域异常类 + 全局异常处理器一个出口；堆栈/SQL/密钥绝不入契约。

## 复盘追问
- 三个服务三套错误结构，请给出收敛到 problem+json 的迁移步骤（双头过渡期如何兼容旧客户端）？
- 安全评审发现某接口的 problem 返回了内部表名，除了删字段还应补什么机制防止再犯？
