---
title: [Q6037] CORS 预检的成本账与 Access-Control-Max-Age
date: 2026-11-20
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6037 · CORS 预检的成本账与 Access-Control-Max-Age

> 难度:★★★ | 标签:成本工程, CORS, OPTIONS, 容量

**问**：为什么每个跨域"自定义头"请求前都有一个 OPTIONS 预检？预检的成本有多大？`Access-Control-Max-Age` 各浏览器真实支持多少？服务端怎么处理这些"零业务价值"的请求？

**答**：跨域请求凡携带自定义头（Authorization、X-Request-Id）或非简单方法/Content-Type，浏览器先发 OPTIONS 预检，拿到允许清单才发真请求。成本账：预检是**完整 HTTP 往返**（排队+RTT+服务端处理），真请求被顺延一个 RTT——内网 1ms 无感，公网 50-200ms/请求直接翻倍；QPS 账上预检请求也占 worker 与限流配额（它通常被限流键误伤，因为无 token 无 body）。`Max-Age`：预检结果可被浏览器缓存，规范无上限，Chrome 上限 2 小时（7200s）、Firefox 24 小时、Safari 只缓存**很短甚至不缓存**（约 0-180s）——所以 Safari 用户会反复预检，这也是"为什么只有部分用户慢"的经典谜底。服务端处置：1) **短路**——ASGI/Django 中间件里识别 OPTIONS+预检头直接 204 返回（不进路由/无权限检查/不落业务日志），成本降到微秒；2) **Max-Age 给足**——`Access-Control-Max-Age: 86400`，同时保证预检响应头（Allow-Origin/Headers/Methods）内容稳定，变了缓存不失效反而踩坑；3) **架构减法**——同域反代统一网关入口消灭跨域（治本），Authorization 用 Cookie 会话回归"简单请求"也是减法之一（各有安全取舍 Q132/Q6009）。

```python
# file: code/03_Web后端开发/q6037_cors_preflight_cost.py
"""预检短路的中间件形态与成本对比. 标准库模拟 ASGI 中间件逻辑."""
import time

ALLOWED_ORIGIN = "https://app.example.com"
ALLOWED_HEADERS = "authorization,x-request-id,content-type"
MAX_AGE = 86400

def is_preflight(method: str, headers: dict) -> bool:
    """预检特征: OPTIONS + Origin + Access-Control-Request-Method."""
    return (method == "OPTIONS"
            and "origin" in headers
            and "access-control-request-method" in headers)

def preflight_response(headers: dict) -> tuple[int, dict]:
    return 204, {
        "Access-Control-Allow-Origin": ALLOWED_ORIGIN,
        "Access-Control-Allow-Headers": ALLOWED_HEADERS,
        "Access-Control-Allow-Methods": "GET,POST,PUT,DELETE,OPTIONS",
        "Access-Control-Max-Age": str(MAX_AGE),   # Chrome<=7200, Firefox 24h, Safari 极短
        "Vary": "Origin",
    }

# --- 短路中间件: 不进路由/权限/业务日志 ---
class PreflightShortCircuit:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response) -> list:  # WSGI 形态示意
        headers = {k.lower(): v for k, v in environ.items() if isinstance(v, str)}
        if is_preflight(environ.get("REQUEST_METHOD", ""), headers):
            status, resp_headers = preflight_response(headers)
            start_response(f"{status} No Content",
                           [(k, v) for k, v in resp_headers.items()])
            return [b""]
        return self.app(environ, start_response)

def full_stack_preflight(headers: dict) -> None:
    """反面教材: 预检也走全栈(路由/权限/日志)."""
    time.sleep(0.002)                     # 模拟依赖注入+权限检查

def bench(fn, reps: int = 5) -> float:
    best = float("inf")
    for _ in range(reps):
        t0 = time.perf_counter()
        fn()
        best = min(best, time.perf_counter() - t0)
    return best * 1000

if __name__ == "__main__":
    hdrs = {"origin": ALLOWED_ORIGIN, "access-control-request-method": "POST"}
    print("is_preflight:", is_preflight("OPTIONS", hdrs),
          "| 响应:", preflight_response(hdrs))
    t_short = bench(lambda: preflight_response(hdrs))
    t_full = bench(lambda: full_stack_preflight(hdrs))
    print(f"短路 {t_short:.3f}ms vs 全栈 {t_full:.2f}ms "
          f"(真实差距还要加路由/DB/日志)")
    print("浏览器缓存上限: Chrome 2h / Firefox 24h / Safari 几乎不缓存 -> Safari 用户反复预检")
    print("治本减法: 同域网关入口消灭跨域; 或降回简单请求(取舍见 Q132)")
```

**追问**：1) 预检响应为什么必须带 `Vary: Origin`？——CDN/浏览器按 (URL, Origin) 缓存预检结果，不标 Vary 会把 A 站的允许头缓存给 B 站共享，跨域放行错乱；这是"配置了 CORS 但偶发失效"的头号根因。2) 限流层为什么要把 OPTIONS 排除？——预检请求无 Authorization（浏览器规范不附凭证），按 token 限流会漏过（配额穿透），按 IP 限流又会误伤正常用户；正确做法是短路在限流之前，预检不占配额。3) WebSocket 升级请求算预检吗？——不算，但同样受 CORS/Origin 校验（Q2936 的握手校验），Origin 白名单逻辑要独立于 HTTP CORS 实现。

## 背诵要点
- 自定义头/非简单方法触发 OPTIONS 预检 = 多一个完整 RTT + 占 worker 与限流配额。
- Max-Age 现实：Chrome 7200s、Firefox 24h、Safari 几乎不缓存——"只有 Safari 慢"的谜底。
- 服务端短路（中间件 204，不进路由/限流/日志）+ 响应带 Vary: Origin；治本是同域网关减法。

## 复盘追问
- 你的 CORS 中间件现在排在限流之后还是之前？顺序错了的攻击/浪费面分别是什么？
- 网关层统一同域后，还有哪些路径绕不开跨域（第三方嵌入、iframe）？这些路径的预检预算怎么管？
