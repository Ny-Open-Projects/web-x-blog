---
title: [Q2929] 健康检查三件套: live/ready/startup 三探针
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2929 · 健康检查三件套: live/ready/startup 三探针

> 难度:★★☆☆ | 标签:健康检查, 编排

**问**:健康检查为什么会有 liveness、readiness、startup 三个口? 三者的判定逻辑和编排器行为分别是什么?

**答**:三个口回答三个不同问题, 混用会出事故。liveness 回答"进程还活着吗", 只查进程自身, 不碰任何依赖——依赖抖动时若把它混进来, 会触发容器重启风暴; 挂了编排器重启容器。readiness 回答"能接流量吗", 要查关键依赖, 坏了返回 503 并列出坏依赖品名, 编排器只摘流量不重启。startup 回答"启动完成了吗", 给慢启动应用一个缓冲期, 启动期返回 503 并报当前步骤与进度, 完成后翻 200 且此后恒 200, 避免慢启动应用被 readiness 在启动窗口内反复摘流。三探针的路径要与业务路由隔离, 不挂鉴权, 探针失败要能区分服务故障与探针故障。

```python
# file: code/03_Web后端开发/q2929_health_probes.py
"""健康检查三件套: liveness / readiness / startup 三探针的判定逻辑(纯标准库)。"""
import json

DEPS = {"db": False, "cache": False}
STARTUP_STEPS = ["加载配置", "连接数据库", "预热缓存", "恢复在途任务"]
startup_done = {"n": 0}


def liveness():
    """进程活着就 200, 不查任何依赖——避免依赖抖动导致容器被误杀重启。"""
    return 200, {"status": "ok"}


def readiness():
    """依赖全绿才 200; 有坏的给 503 并列出品名, 看板直接可读。"""
    bad = sorted(name for name, ok in DEPS.items() if not ok)
    if bad:
        return 503, {"status": "unavailable", "down": bad}
    return 200, {"status": "ok"}


def startup():
    """慢启动应用先 503 并报当前步骤; 全部完成后翻 200 且此后恒 200。"""
    if startup_done["n"] < len(STARTUP_STEPS):
        return 503, {"status": "starting",
                     "step": STARTUP_STEPS[startup_done["n"]],
                     "progress": "%d/%d" % (startup_done["n"], len(STARTUP_STEPS))}
    return 200, {"status": "ok"}


def probe(fn):
    status, body = fn()
    return status, json.dumps(body, ensure_ascii=False, sort_keys=True)


# 1. 进程刚拉起: 活着但不就绪, 启动探针报进度
print("启动期 live ->", probe(liveness))
print("启动期 ready ->", probe(readiness))
print("启动期 startup ->", probe(startup))
assert probe(liveness)[0] == 200
assert probe(readiness)[0] == 503
assert probe(startup)[0] == 503

# 2. 依赖陆续就绪, 启动步骤推进
DEPS["db"] = True
print("db 就绪后 ready ->", probe(readiness))
startup_done["n"] = 2
assert probe(startup)[0] == 503, "步骤未完仍 503"
DEPS["cache"] = True
startup_done["n"] = len(STARTUP_STEPS)
s3, b3 = probe(startup)
r3 = json.loads(b3)
assert s3 == 200 and r3 == {"status": "ok"}
print("全就绪 ready ->", probe(readiness))
print("启动完成 startup ->", (s3, b3))

# 3. 运行期缓存抖动: ready 503 但 live 仍 200, 编排器不该重启只该摘流量
DEPS["cache"] = False
s_live, _ = probe(liveness)
s_ready, b_ready = probe(readiness)
print("缓存抖动期 live=%s ready=%s body=%s" % (s_live, s_ready, b_ready))
assert (s_live, s_ready) == (200, 503)
assert json.loads(b_ready)["down"] == ["cache"]
DEPS["cache"] = True

# 4. 编排器视角的裁决表: 三探针组合决定行为
def orchestrate(live, ready, startup):
    if live != 200:
        return "重启容器"
    if startup != 200:
        return "等待启动完成"
    if ready != 200:
        return "摘除流量不重启"
    return "接入流量"

table = [(200, 200, 200), (200, 503, 200), (200, 200, 503), (500, 503, 503)]
for live, ready, st in table:
    print("live=%s ready=%s startup=%s -> %s" % (live, ready, st, orchestrate(live, ready, st)))
assert orchestrate(200, 503, 200) == "摘除流量不重启"
assert orchestrate(500, 503, 503) == "重启容器"
print("健康检查三件套演示通过")
```

**追问**:
- startup 与 readiness 都可能 503, 为什么必须分开?——startup 503 是"还没起完"等它, readiness 503 是"坏了"摘流量, 语义不同动作不同。
- 健康口要不要鉴权?——探针路径与业务路由隔离且内网可达即可, 挂鉴权会让探针失败被误判成服务故障。
