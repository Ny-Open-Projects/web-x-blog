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
