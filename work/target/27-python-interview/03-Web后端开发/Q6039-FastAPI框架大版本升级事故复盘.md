---
title: [Q6039] FastAPI/Starlette 大版本升级的事故复盘
date: 2026-11-20
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6039 · FastAPI/Starlette 大版本升级的事故复盘

> 难度:★★★★ | 标签:版本演进, FastAPI, Starlette, 事故复盘

**问**：FastAPI 0.x 的"版本地狱"是什么（为什么小版本升级也会炸）？Starlette 独立升级破坏了什么？框架升级的正确形态（锁定策略、试金石清单）怎么建？

**答**：FastAPI 0.x 时代**没有 SemVer 承诺**：小版本（0.9x→0.10x）也可能移除参数、改默认行为，而且它对 Starlette/Pydantic 的版本范围声明宽泛——**Starlette 或 Pydantic 被其他依赖抬升一个版本，FastAPI 的运行时行为就变了**，这是"我只升了 A 库怎么 B 崩了"的典型来源。经典事故面：1) **Starlette 破坏性变更**——BaseHTTPMiddleware 的 contextvars 传播与 background 任务语义多次变化（contextvars 丢失 → 日志 trace_id 断链 Q822）；TestClient 底层从 requests 换 httpx 后测试语义漂移；2) **FastAPI 行为变化**——依赖缓存语义（同一依赖在子依赖中的 use_cache 行为）、响应模型默认序列化收紧、OpenAPI 生成差异导致契约测试（Q851）全红；3) **隐式锁太松**——`requirements.txt` 写 `fastapi` 无上限，CI 突然拉进不兼容新版本。升级正确形态：a) **三层锁定**——应用层 lockfile（uv/pip-tools，Q7015 思路）+ 框架对框架的版本断言（启动时校验 `starlette.__version__` 在允许区间）+ 依赖矩阵 CI（每周一次"允许范围内最新"的自动升级 PR）；b) **试金石清单**——启动自检（OpenAPI schema diff、contextvars 贯通测试、TestClient 冒烟）打包成升级门禁；c) **灰度**——框架升级与业务发布解耦，按 worker 灰度观察错误率（Q6026 运行时升级同款流程）。

```python
# file: code/03_Web后端开发/q6039_framework_upgrade.py
"""框架版本断言自检 + OpenAPI 契约 diff 门禁(标准库实现, FastAPI 可选)."""
import json
import re
import sys

# --- 1) 启动期版本断言: 防依赖抬升偷换 ---
def parse_version(v: str) -> tuple:
    return tuple(int(x) for x in re.findall(r"\d+", v)[:3])

def assert_compatible(name: str, got: str, min_v: str, max_v: str) -> bool:
    ok = parse_version(min_v) <= parse_version(got) < parse_version(max_v)
    print(f"{name}: {got} in [{min_v}, {max_v}) -> {'OK' if ok else 'BREAKING'}")
    return ok

if __name__ == "__main__":
    try:
        import fastapi
        import starlette
        assert_compatible("fastapi", fastapi.__version__, "0.100", "1.0")
        assert_compatible("starlette", starlette.__version__, "0.27", "0.60")
    except ImportError:
        print("(fastapi 未安装, 降级演示断言逻辑)")
        assert_compatible("starlette(示意)", "0.37.2", "0.27", "0.60")

    # --- 2) OpenAPI 契约 diff 门禁: 升级前后 schema 对比 ---
    baseline = {
        "/orders": {"get": {"params": ["page", "size"],
                            "resp": {"id": "int", "amount": "float"}}},
    }
    after = {
        "/orders": {"get": {"params": ["page", "size", "cursor"],   # 新增: 安全
                            "resp": {"id": "int", "amount": "string"}}},  # 类型变化: 破坏!
    }

    def contract_diff(old: dict, new: dict) -> list[str]:
        breaking = []
        for path, ops in old.items():
            for method, spec in ops.items():
                for p in spec.get("params", []):
                    if p not in new.get(path, {}).get(method, {}).get("params", []):
                        breaking.append(f"参数移除 {path}:{method}:{p}")
                for field, typ in spec.get("resp", {}).items():
                    ntyp = new.get(path, {}).get(method, {}).get("resp", {}).get(field)
                    if ntyp is None:
                        breaking.append(f"响应字段移除 {path}:{method}:{field}")
                    elif ntyp != typ:
                        breaking.append(f"响应类型变更 {path}:{method}:{field} "
                                        f"{typ}->{ntyp}")
        return breaking

    breaks = contract_diff(baseline, after)
    print("契约破坏项:", breaks or "无")
    exit_code = 1 if breaks else 0
    print("CI 门禁退出码:", exit_code, "(破坏项>0 即拒绝升级 PR)")

    # --- 3) contextvars 贯通试金石(升级最易断的链) ---
    import contextvars
    trace_var = contextvars.ContextVar("trace_id", default="-")

    def middleware_suspect() -> str:
        return trace_var.get()                    # 升级后若为 '-', 链已断

    trace_var.set("trace-123")
    print("contextvars 试金石 trace_id:", middleware_suspect())
    print("python:", sys.version_info[:3])
```

**追问**：1) 为什么"启动时版本断言"比只靠 lockfile 多一层？——lockfile 锁的是应用直接依赖，而传递依赖（某工具库 import starlette）可能绕过 lockfile 场景（docker 镜像重建、`pip install -U`），启动断言把兼容前提变成运行时事实。2) OpenAPI diff 里哪些变化不是破坏？——新增参数（带默认值）、新增响应字段、枚举值新增（消费方按未知处理时）都是兼容扩展；diff 分级要区分 breaking/compatible（Q1627 的 diff 分级）。3) BaseHTTPMiddleware 的 contextvars 事故怎么防？——升级清单里固定一条"trace_id 贯通测试"：mock 请求打中间件链，断言日志与响应头里 trace_id 一致；它比读 release notes 可靠得多。

## 背诵要点
- FastAPI 0.x 无 SemVer：小版本可移除参数；Starlette/Pydantic 被传递依赖抬升即行为漂移。
- 升级形态：lockfile + 启动期版本断言 + 依赖矩阵自动升级 PR + 契约 diff 门禁。
- 试金石三条：OpenAPI schema diff、contextvars trace 贯通、TestClient 冒烟；升级与业务发布解耦灰度。

## 复盘追问
- 你的项目里谁"看住"Starlette 版本？如果答案是没人，第一次炸会以什么表象出现（日志断链/契约测试全红/运行时 TypeError）？
- 依赖矩阵自动升级 PR 每周跑一次，门禁里哪三条测试权重最高？
